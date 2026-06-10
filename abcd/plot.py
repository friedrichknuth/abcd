import contextily as cx
import geopandas as gpd


def plot_glaciers(gdf: gpd.GeoDataFrame):
    """Plot a glacier GeoDataFrame interactively with a Swisstopo basemap."""
    provider = cx.providers.SwissFederalGeoportal.SWISSIMAGE
    return gdf.explore(tiles=provider)
