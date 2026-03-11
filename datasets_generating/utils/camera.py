import numpy as np
import os
import pandas as pd

from location import random_location, address_name

SEED_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
N = 20000


def random_camera():
    lon, lat = random_location()
    address = address_name(lon, lat)
    return {"lon": lon, "lat": lat, "address": address}


cameras = []
for i in range(N):
    camera = {"id": i + 1}
    camera.update(random_camera())
    cameras.append(camera)
cameras_pd = pd.DataFrame(data=cameras)
cameras_pd = cameras_pd.groupby("address").head(5)
cameras_pd.sort_values(by="address", inplace=True)
cameras_pd["id"] = np.arange(cameras_pd.shape[0]) + 1
cameras_pd.to_csv(os.path.join(SEED_DIR, "camera.csv"), index=False)
