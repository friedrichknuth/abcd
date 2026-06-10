import io
import zipfile

import geopandas as gpd
import requests


def read_sgi2023_glaciers(name_filter: str = "Birch") -> gpd.GeoDataFrame:
    """Read SGI 2023 glacier inventory and filter by name substring."""
    url = "https://doi.glamos.ch/data/inventory/inventory_sgi2023_r2026.zip"
    response = requests.get(url)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        shp_files = [f for f in zf.namelist() if f.endswith(".shp")]
        target = next(f for f in shp_files if "SGI_2023_glaciers" in f)

        # Extract all sidecar files (.dbf, .shx, .prj, etc.) alongside the .shp
        prefix = target[: target.rfind(".")]
        members = [f for f in zf.namelist() if f.startswith(prefix)]
        zf.extractall(members=members, path="/tmp")

    gdf = gpd.read_file(f"/tmp/{target}")
    return gdf[gdf["name"].str.contains(name_filter, na=False)]
