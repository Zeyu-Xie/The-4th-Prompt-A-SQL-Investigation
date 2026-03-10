import numpy as np

RNG_SEED = 42
LON_RANGE = [80.583, 80.650]
LAT_RANGE = [28.300, 28.584]

rng = np.random.default_rng(seed=RNG_SEED)


def random_location():
    lon = rng.uniform(LON_RANGE[0], LON_RANGE[1])
    lat = rng.uniform(LAT_RANGE[0], LAT_RANGE[1])
    return lon, lat
