import datetime
import numpy as np
import os
import pandas as pd

SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
RNG_SEED = 42

rng = np.random.default_rng(RNG_SEED)

cameras_pd = pd.read_csv(os.path.join(SEEDS_DIR, "cameras.csv"))
cameras_id_without_energy_center = list(
    cameras_pd.loc[cameras_pd["address"] != "energy center"]["id"]
)
cameras_id_with_energy_center = list(
    cameras_pd.loc[cameras_pd["address"] == "energy center"]["id"]
)


def random_camera_id_without_energy_center():
    return rng.choice(cameras_id_without_energy_center)


def random_camera_id_with_energy_center():
    return rng.choice(cameras_id_with_energy_center)


def random_camera_log_without_energy_center(
    id: int, citizen_id: str, datetime: datetime.datetime
) -> dict:
    return {
        "id": id,
        "camera_id": random_camera_id_without_energy_center(),
        "citizen_id": citizen_id,
        "datetime": datetime.isoformat(sep=" ", timespec="seconds"),
    }


def random_camera_log_with_energy_center(
    id: int, citizen_id: str, datetime: datetime.datetime
) -> dict:
    return {
        "id": id,
        "camera_id": random_camera_id_with_energy_center(),
        "citizen_id": citizen_id,
        "datetime": datetime.isoformat(sep=" ", timespec="seconds"),
    }
