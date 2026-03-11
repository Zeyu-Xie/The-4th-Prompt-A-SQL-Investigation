import math
import numpy as np
import os
import pandas as pd

SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
RNG_SEED = 42
LON_RANGE = [80.583, 80.650]
LAT_RANGE = [28.300, 28.584]

rng = np.random.default_rng(seed=RNG_SEED)

mid_lon = (LON_RANGE[0] + LON_RANGE[1]) / 2
mid_lat = (LAT_RANGE[0] + LAT_RANGE[1]) / 2
dis_per_lon = math.cos(mid_lat * math.pi / 180) * math.pi * 6371 / 180
dis_per_lat = 111.12

special_address_pd = pd.read_csv(os.path.join(SEEDS_DIR, "special_addresses.csv"))


def random_location():
    lon = rng.uniform(LON_RANGE[0], LON_RANGE[1])
    lat = rng.uniform(LAT_RANGE[0], LAT_RANGE[1])
    return lon, lat


def relative_location(lon: float, lat: float, dis_scale: float) -> tuple[float, float]:
    return lon + rng.normal(loc=0, scale=dis_scale / dis_per_lon), lat + rng.normal(
        loc=0, scale=dis_scale / dis_per_lat
    )


def distance(A: tuple[float, float], B: tuple[float, float]) -> float:
    return math.sqrt(
        ((A[0] - B[0]) * dis_per_lon) ** 2 + ((A[1] - B[1]) * dis_per_lat) ** 2
    )


def address_name(lon: float, lat: float) -> str:
    mask = (
        (special_address_pd["lon_from"] <= lon)
        & (special_address_pd["lon_to"] > lon)
        & (special_address_pd["lat_from"] <= lat)
        & (special_address_pd["lat_to"] > lat)
    )
    possible_address_pd = special_address_pd.loc[mask]
    return (
        possible_address_pd.iloc[0]["address"]
        if possible_address_pd.shape[0] >= 1
        else "default"
    )
