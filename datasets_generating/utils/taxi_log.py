import datetime
import os
import pandas as pd

from .location import random_location, relative_location, distance

SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
DIS_OFFSET_SCALE = 0.05
ARR_SPECIAL_TAXI_LOG_TIME = [
    datetime.datetime(2077, 6, 21, 22, 15, 14),
    datetime.datetime(2077, 6, 24, 23, 6, 55),
    datetime.datetime(2077, 6, 26, 22, 46, 10),
    datetime.datetime(2077, 6, 27, 22, 35, 37),
    datetime.datetime(2077, 6, 27, 23, 1, 3),
    datetime.datetime(2077, 6, 28, 10, 21, 43),
]
ARR_CITIZEN_ID = [
    "202705138264",
    "202311179921",
    "201604105300",
    "203312216529",
    "204205220083",
    "205506298741",
]


def random_taxi_log(
    trip_id: int, citizen_id: str, trip_time: datetime.datetime
) -> dict:
    destination_lon, destination_lat = random_location()
    actual_dropoff_lon, actual_dropoff_lat = relative_location(
        lon=destination_lon, lat=destination_lat, dis_scale=DIS_OFFSET_SCALE
    )
    distance_offset_km = distance(
        A=[destination_lon, destination_lat], B=[actual_dropoff_lon, actual_dropoff_lat]
    )
    return {
        "trip_id": trip_id,
        "citizen_id": citizen_id,
        "trip_time": trip_time.isoformat(sep=" ", timespec="seconds"),
        "destination_lon": destination_lon,
        "destination_lat": destination_lat,
        "actual_dropoff_lon": actual_dropoff_lon,
        "actual_dropoff_lat": actual_dropoff_lat,
        "distance_offset_km": distance_offset_km,
    }


def random_special_taxi_log(
    trip_id: int, citizen_id: str, trip_time: datetime.datetime
) -> dict:
    destination_lon, destination_lat = random_location()
    actual_dropoff_lon, actual_dropoff_lat = relative_location(
        lon=80.634, lat=28.56, dis_scale=DIS_OFFSET_SCALE
    )
    distance_offset_km = distance(
        A=[destination_lon, destination_lat], B=[actual_dropoff_lon, actual_dropoff_lat]
    )
    return {
        "trip_id": trip_id,
        "citizen_id": citizen_id,
        "trip_time": trip_time.isoformat(sep=" ", timespec="seconds"),
        "destination_lon": destination_lon,
        "destination_lat": destination_lat,
        "actual_dropoff_lon": actual_dropoff_lon,
        "actual_dropoff_lat": actual_dropoff_lat,
        "distance_offset_km": distance_offset_km,
    }


# def generate_all_special_taxi_logs():
#     arr_special_taxi_logs = [
#         random_special_taxi_log(
#             trip_id=0,
#             citizen_id=ARR_CITIZEN_ID[i],
#             trip_time=ARR_SPECIAL_TAXI_LOG_TIME[i],
#         )
#         for i in range(6)
#     ]
#     return pd.DataFrame(data=arr_special_taxi_logs)


# arr_special_taxi_logs_pd = generate_all_special_taxi_logs()
# arr_special_taxi_logs_pd.to_csv(
#     os.path.join(SEEDS_DIR, "special_taxi_log.csv"), index=False
# )
