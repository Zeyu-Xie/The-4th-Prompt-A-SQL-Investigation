import datetime
import numpy as np

from utils.location import *

RNG_SEED = 42
ARR_EVENTS = [
    {
        "event_type": "traffic accident",
        "action_taken": [
            "info exchanging",
            "towing",
            "rescuing",
            "tracing",
            "alcohol testing",
            "sorting",
            "containment",
        ],
    },
    {
        "event_type": "public disturbance",
        "action_taken": [
            "mediating",
            "dispersing",
            "warning",
            "de-escalating",
            "patrolling",
        ],
    },
    {
        "event_type": "criminal activity",
        "action_taken": [
            "apprehending",
            "handcuffing",
            "searching",
            "interrogating",
            "crime-scene guarding",
        ],
    },
    {
        "event_type": "emergency aid",
        "action_taken": [
            "first-aiding",
            "wellness checking",
            "evacuating",
            "counseling",
            "entry forcing",
        ],
    },
    {
        "event_type": "property crime",
        "action_taken": [
            "fingerprinting",
            "CCTV reviewing",
            "itemizing",
            "canvassing",
            "recovering",
        ],
    },
]

rng = np.random.default_rng(seed=RNG_SEED)


def random_exp_seconds(scale: float) -> float:
    return rng.exponential(scale=scale)


def random_event_and_action() -> tuple[str, str]:
    event = rng.choice(ARR_EVENTS)
    event_type = event["event_type"]
    action_taken = rng.choice(event["action_taken"])
    return event_type, action_taken


def random_guard_log(id: int, datetime: datetime.datetime):
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
