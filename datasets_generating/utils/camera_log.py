import datetime
import numpy as np
import os
import pandas as pd

RNG_SEED = 42
SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")

rng = np.random.default_rng(RNG_SEED)

cameras_pd = pd.read_csv(os.path.join(SEEDS_DIR, "cameras.csv"))
n_cameras = cameras_pd.shape[0]


def random_camera_id_without_energy_center():
    r = rng.integers(1, n_cameras - 1)
    if r >= 7:
        return r + 2
    return r

def random_camera_id_with_energy_center():
    r = rng.integers(0, 2) + 7
    return r

def random_camera_log_without_energy_center(
    id: int, citizen_id: str, datetime: datetime.datetime
) -> object:
    return {
        "id": id,
        "camera_id": random_camera_id_without_energy_center(),
        "citizen_id": citizen_id,
        "datetime": datetime.isoformat(sep=" ", timespec="seconds"),
    }

def random_camera_log_with_energy_center(
    id: int, citizen_id: str, datetime: datetime.datetime
) -> object:
    return {
        "id": id,
        "camera_id": random_camera_id_with_energy_center(),
        "citizen_id": citizen_id,
        "datetime": datetime.isoformat(sep=" ", timespec="seconds"),
    }