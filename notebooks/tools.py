import contextily as cx
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import rioxarray
from matplotlib_scalebar.scalebar import ScaleBar


def read_sgi2023_glaciers(name_filter: str = "Birch") -> gpd.GeoDataFrame:
    """Read SGI 2023 glacier inventory directly from remote ZIP."""
    # Prefixing with zip+ triggers GDAL's virtual file system
    url = "zip+https://doi.glamos.ch/data/inventory/inventory_sgi2023_r2026.zip"

    # Read directly; specifying the layer targets the exact shapefile inside the archive
    gdf = gpd.read_file(url, layer="SGI_2023_glaciers")
    return gdf[gdf["name"].str.contains(name_filter, na=False)]

def plot_glaciers(gdf: gpd.GeoDataFrame):
    """Plot a glacier GeoDataFrame interactively with a Swisstopo basemap."""
    provider = cx.providers.SwissFederalGeoportal.SWISSIMAGE
    return gdf.explore(tiles=provider)