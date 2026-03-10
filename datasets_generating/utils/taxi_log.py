import datetime

from location import random_location, relative_location, distance

DIS_OFFSET_SCALE = 0.05


def random_taxi_log(
    trip_id: int, citizen_id: str, trip_time: datetime.datetime
) -> object:
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
