import datetime
import json
import numpy as np
import os

from .location import random_location

SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
RNG_SEED = 42
with open(os.path.join(SEEDS_DIR, "guard_events.json"), "r") as f:
    ARR_EVENTS = json.load(f)

rng = np.random.default_rng(seed=RNG_SEED)


def random_event_and_action() -> tuple[str, str]:
    event = rng.choice(ARR_EVENTS)
    event_type = event["event_type"]
    action_taken = rng.choice(event["action_taken"])
    return event_type, action_taken


def random_guard_log(id: int, datetime: datetime.datetime) -> dict:
    datetime = datetime.isoformat(sep=" ", timespec="seconds")
    event_type, action_taken = random_event_and_action()
    lon, lat = random_location()
    return {
        "id": id,
        "datetime": datetime,
        "event_type": event_type,
        "action_taken": action_taken,
        "lon": lon,
        "lat": lat,
    }
