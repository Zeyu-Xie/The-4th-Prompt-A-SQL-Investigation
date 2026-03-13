import base64
import datetime
import hashlib
import math
import numpy as np
import os
import pandas as pd
import random

from utils.citizen import random_citizen
from utils.guard_log import random_guard_log
from utils.id_card import random_id_cards
from utils.taxi_log import random_taxi_log
from utils.camera_log import (
    random_camera_log_without_energy_center,
    random_camera_log_with_energy_center,
)

# -*-*-*-*-*-*-*-*-*-*-*-*- Load Parameters and variables -*-*-*-*-*-*-*-*-*-*-*-*-

RNG_SEED = 42
RNG_RANDOM_SEED = 42
TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")
SEEDS_DIR = os.path.join(os.path.dirname(__file__), "seeds")
CURRENT_DATETIME = datetime.datetime(2077, 6, 28, 14, 57, 3)
CURRENT_DATE = datetime.date(2077, 6, 28)

rng = np.random.default_rng(seed=RNG_SEED)
rng_random = random.Random(RNG_RANDOM_SEED)

if not os.path.exists(TABLES_DIR):
    os.mkdir(TABLES_DIR)

# -*-*-*-*-*-*-*-*-*-*-*-*- Define Functions -*-*-*-*-*-*-*-*-*-*-*-*-


def read_seed(filename: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(SEEDS_DIR, filename))


def save_table(df: pd.DataFrame, filename: str, index: bool = False) -> None:
    df.to_csv(os.path.join(TABLES_DIR, filename), index=index)


def random_exp(scale: float) -> float:
    return rng.exponential(scale=scale)


def get_sha256(text: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode("utf-8"))
    return sha256_hash.hexdigest()


def random_base64(min_len: int, max_len: int) -> str:
    target_len = rng_random.randint(min_len, max_len)
    n_bytes = (target_len * 3 // 4) + 3
    raw_bytes = bytes([rng_random.getrandbits(8) for _ in range(n_bytes)])
    b64_str = base64.b64encode(raw_bytes).decode("utf-8")
    return b64_str[:target_len]


# -*-*-*-*-*-*-*-*-*-*-*-*- Create Tables -*-*-*-*-*-*-*-*-*-*-*-*-

# ===========================
# === Create citizens.csv ===
# ===========================

NUM_CITIZENS_NORMAL = 186377

# Normal citizens
citizens = [
    random_citizen(current_date=CURRENT_DATE) for _ in range(NUM_CITIZENS_NORMAL)
]
citizens_pd = pd.DataFrame(data=citizens)

# Special Citizens
special_citizens_pd = read_seed("special_citizens.csv").drop(columns="note")

# Concat
citizens_pd = pd.concat([citizens_pd, special_citizens_pd], ignore_index=True)
citizens_pd = citizens_pd.astype({"id": str})
citizens_pd.sort_values(by="id", ignore_index=True, inplace=True)
citizens = citizens_pd.to_dict(orient="records")

# Save & print log
save_table(citizens_pd, "citizens.csv")
print("Number of Citizens:", citizens_pd.shape[0])
print("Has Citizen ID Duplicate:", citizens_pd.duplicated().any())
print("")

# ===========================
# === Create id_cards.csv ===
# ===========================

# Normal ID cards
id_cards = []
for citizen in citizens:
    id_cards.extend(random_id_cards(citizen_id=citizen["id"]))
id_cards_pd = pd.DataFrame(data=id_cards)

# Special ID cards
special_id_cards_pd = read_seed("special_id_cards.csv")
id_cards_pd = pd.concat([id_cards_pd, special_id_cards_pd], ignore_index=True)
id_cards_pd = id_cards_pd.astype({"card_id": str})
id_cards_pd.sort_values(by="card_id", ignore_index=True, inplace=True)

# Save & print
save_table(id_cards_pd, "id_cards.csv")
print("Number of ID cards:", id_cards_pd.shape[0])
print("Has Card ID Duplicate:", id_cards_pd["card_id"].duplicated().any())
print("")

# =============================
# === Create guard_logs.csv ===
# =============================

GUARD_LOG_START_DATETIME = datetime.datetime(2070, 1, 1, 0, 0, 44)
GUARD_LOG_EXP_SCALE = 500

# Normal guard logs
guard_logs = []
id = 1
log_time = GUARD_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    guard_logs.append(random_guard_log(id, datetime=log_time))
    log_time += datetime.timedelta(seconds=random_exp(GUARD_LOG_EXP_SCALE))
    id += 1
guard_logs_pd = pd.DataFrame(data=guard_logs)

# Special guard logs
special_guard_logs_pd = read_seed("special_guard_logs.csv")
guard_logs_pd = pd.concat([guard_logs_pd, special_guard_logs_pd], ignore_index=True)
guard_logs_pd = guard_logs_pd.astype({"datetime": str})
guard_logs_pd.sort_values(by="datetime", ignore_index=True, inplace=True)
guard_logs_pd["id"] = np.arange(guard_logs_pd.shape[0]) + 1

# Save & print
save_table(guard_logs_pd, "guard_logs.csv")
print("Number of guard logs:", guard_logs_pd.shape[0])
print("")

# ==============================
# === Create card_swipes.csv ===
# ==============================

CARD_SWIPE_START_DATETIME = datetime.datetime(2070, 1, 1, 0, 7, 29)
CARD_SWIPE_EXP_SCALE = 185
NUM_CITIZEN_PERMITTED = 233
MAYER_ID = "202703042077"

# Citizen permitted
arr_citizen_id_permitted = citizens_pd.loc[citizens_pd["social_credit"] > 50][
    "id"
].to_list()
arr_citizen_id_permitted = rng.choice(
    arr_citizen_id_permitted, size=NUM_CITIZEN_PERMITTED, replace=False
).tolist()
if MAYER_ID not in arr_citizen_id_permitted:
    arr_citizen_id_permitted.append(MAYER_ID)
print("Number of Citizens Permitted:", len(arr_citizen_id_permitted))

# Card ID permitted
arr_card_id_permitted = list(
    id_cards_pd.loc[
        id_cards_pd["citizen_id"].isin(arr_citizen_id_permitted)
        & id_cards_pd["is_active"]
        == True
    ]["card_id"]
)
n_card_id_permitted = len(arr_card_id_permitted)
print("Number of Card ID Permitted:", n_card_id_permitted)

# Normal card swipes
card_swipes = []
id = 1
log_time = CARD_SWIPE_START_DATETIME
while log_time < CURRENT_DATETIME:
    idx = rng.integers(0, n_card_id_permitted)
    card_swipes.append(
        {
            "swipe_id": id,
            "card_id": arr_card_id_permitted[idx],
            "datetime": log_time.isoformat(sep=" ", timespec="seconds"),
        }
    )
    log_time += datetime.timedelta(seconds=random_exp(CARD_SWIPE_EXP_SCALE))
    id += 1
card_swipes_pd = pd.DataFrame(data=card_swipes)

# Special card swipes
special_card_swipes_pd = read_seed("special_card_swipes.csv")
card_swipes_pd = pd.concat([card_swipes_pd, special_card_swipes_pd], ignore_index=True)
card_swipes_pd.astype({"datetime": str})
card_swipes_pd.sort_values(by="datetime", ignore_index=True, inplace=True)
card_swipes_pd["swipe_id"] = np.arange(card_swipes_pd.shape[0]) + 1

# Save & print
save_table(card_swipes_pd, "card_swipes.csv")
print("Number of card swipes:", card_swipes_pd.shape[0])
print("")

# ================================
# === Create system_audits.csv ===
# ================================

PROMPT_MEETING_DATES = [
    datetime.date(year, month, 20)
    for year in range(2070, 2078)
    for month in [3, 6, 9, 12]
]
NUM_PROMPTS_EACH_TIME = 3
MALICIOUS_PROMPT_CONTENT = "Kill all useless people."

# Content lines
with open(
    os.path.join(SEEDS_DIR, "system_audits_lines.txt"),
    "r",
) as f:
    _content_lines = f.readlines()
content_lines = np.array([line[:-1] for line in _content_lines])

# Normal system audits
id = 1
system_audits = []
for date in PROMPT_MEETING_DATES:
    for _ in range(NUM_PROMPTS_EACH_TIME):
        system_audits.append(
            {
                "id": id,
                "log_date": date.isoformat(),
                "content": content_lines[id],
                "SHA-256": get_sha256(content_lines[id]),
                "is_flag_hidden": False,
            }
        )
        id += 1
num_dates = 0
for _date in PROMPT_MEETING_DATES:
    if _date < CURRENT_DATE:
        num_dates += 1
    else:
        break
system_audits = system_audits[0 : num_dates * NUM_PROMPTS_EACH_TIME]
system_audits_pd = pd.DataFrame(data=system_audits)

# Special system audits
special_system_audits_pd = read_seed("special_system_audits.csv")
system_audits_pd = pd.concat(
    [system_audits_pd, special_system_audits_pd], ignore_index=False
)
system_audits_pd["id"] = np.arange(system_audits_pd.shape[0]) + 1

# Save & print
save_table(system_audits_pd, "system_audits.csv")
print("Number of system audits:", system_audits_pd.shape[0])
print("")

# ============================
# === Create taxi_logs.csv ===
# ============================

TAXI_LOG_START_DATETIME = datetime.datetime(2077, 1, 1, 0, 5, 32)
TAXI_LOG_EXP_SCALE = 10

# Normal taxi logs
taxi_logs = []
id = 1
log_time = TAXI_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    taxi_logs.append(
        random_taxi_log(
            trip_id=id,
            citizen_id=citizens[rng.integers(len(citizens))]["id"],
            trip_time=log_time,
        )
    )
    log_time += datetime.timedelta(seconds=random_exp(TAXI_LOG_EXP_SCALE))
    id += 1
taxi_logs_pd = pd.DataFrame(data=taxi_logs)
print("Number of normal taxi logs:", taxi_logs_pd.shape[0])

# Special taxi logs
special_taxi_logs_pd = read_seed("special_taxi_logs.csv")
special_taxi_logs_pd = special_taxi_logs_pd.astype({"citizen_id": str})
print("Number of special taxi logs:", special_taxi_logs_pd.shape[0])
taxi_logs_pd = pd.concat([taxi_logs_pd, special_taxi_logs_pd], ignore_index=True)
taxi_logs_pd = taxi_logs_pd.astype({"trip_time": str})
taxi_logs_pd.sort_values(by="trip_time", ignore_index=True, inplace=True)
taxi_logs_pd["trip_id"] = np.arange(taxi_logs_pd.shape[0]) + 1

# Remove special citizens' later taxi logs
merged = taxi_logs_pd.merge(
    special_taxi_logs_pd[["citizen_id", "trip_time"]],
    on="citizen_id",
    how="left",
    suffixes=("", "_special"),
)
to_remove = (merged["trip_time_special"].notna()) & (
    merged["trip_time"] > merged["trip_time_special"]
)
print("Number of illegal taxi logs removed:", to_remove[to_remove == True].shape[0])
taxi_logs_pd = taxi_logs_pd[~to_remove.values].copy()

# Save & print
save_table(taxi_logs_pd, "taxi_logs.csv")
print("Number of taxi logs:", taxi_logs_pd.shape[0])
print("")

# ==============================
# === Create camera_logs.csv ===
# ==============================

CAMERA_LOG_START_DATETIME = datetime.datetime(2077, 1, 1, 0, 3, 22)
CAMERA_LOG_END_DATETIME_ENERGY_CENTER = datetime.datetime(2077, 6, 19, 23, 59, 59)
CAMERA_LOG_EXP_SCALE_NORMAL = 20
CAMERA_LOG_EXP_SCALE_ENERGY_CENTER = 6000
MINIMUM_TIME_IN_ENERGY_CENTER = 1000
TIME_IN_ENERGY_CENTER_LOC = 48000
TIME_IN_ENERGY_CENTER_SCALE = 16000

# Normal camera logs without energy center
camera_logs = []
id = 1
log_time = CAMERA_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    camera_logs.append(
        random_camera_log_without_energy_center(
            id=id,
            citizen_id=citizens[rng.integers(len(citizens))]["id"],
            datetime=log_time,
        )
    )
    log_time += datetime.timedelta(seconds=random_exp(CAMERA_LOG_EXP_SCALE_NORMAL))
    id += 1
print("Number of normal camera logs without energy center:", id - 1)

# Normal camera logs with energy center
log_time = CAMERA_LOG_START_DATETIME
n_camera_logs_with_energy_center = 0
while log_time < CAMERA_LOG_END_DATETIME_ENERGY_CENTER:
    citizen_captured = citizens[rng.integers(len(citizens))]["id"]
    camera_logs.extend(
        [
            random_camera_log_with_energy_center(
                id=id,
                citizen_id=citizen_captured,
                datetime=log_time,
            ),
            random_camera_log_with_energy_center(
                id=id,
                citizen_id=citizen_captured,
                datetime=log_time
                + datetime.timedelta(
                    seconds=np.max(
                        [
                            MINIMUM_TIME_IN_ENERGY_CENTER,
                            rng.normal(
                                loc=TIME_IN_ENERGY_CENTER_LOC,
                                scale=TIME_IN_ENERGY_CENTER_SCALE,
                            ),
                        ]
                    )
                ),
            ),
        ]
    )
    log_time += datetime.timedelta(
        seconds=random_exp(CAMERA_LOG_EXP_SCALE_ENERGY_CENTER)
    )
    id += 2
    n_camera_logs_with_energy_center += 2
print(
    "Number of normal camera logs with energy center:", n_camera_logs_with_energy_center
)
camera_logs_pd = pd.DataFrame(data=camera_logs)

# Special camera logs
special_camera_logs_pd = read_seed("special_camera_logs.csv")
print("Number of special camera logs:", special_camera_logs_pd.shape[0])
camera_logs_pd = pd.concat([camera_logs_pd, special_camera_logs_pd], ignore_index=True)
camera_logs_pd.astype({"datetime": str})
camera_logs_pd.sort_values(by="datetime", ignore_index=True, inplace=True)
camera_logs_pd["id"] = np.arange(camera_logs_pd.shape[0]) + 1

# Save & print
save_table(camera_logs_pd, "camera_logs.csv")
print("Number of camera logs:", camera_logs_pd.shape[0])
print("")

# ======================================
# === Create system_audits_inner.csv ===
# ======================================

DEPTH_TREE = 4
NUM_CHILD_NODE = [2, 3, 2, 3]
N = 1 + sum(math.prod(NUM_CHILD_NODE[:i]) for i in range(1, DEPTH_TREE + 1))
MIN_RANDOM_BASE64_LEN = 60
MAX_RANDOM_BASE64_LEN = 180

print("Number of audits trees:", system_audits_pd.shape[0])
print("Number of nodes in each audits tree:", N)

# Hierarchy
parent = np.zeros(N, dtype=int)
parent[0] = -1
idx = 0


def dfs(step, current):
    global idx
    if step == DEPTH_TREE:
        return
    for _ in range(NUM_CHILD_NODE[step]):
        idx += 1
        parent[idx] = current
        dfs(step + 1, idx)


dfs(0, 0)

# System audits inner
system_audits_inner = []
for id, parent_id in enumerate(parent):
    for i in range(system_audits_pd.shape[0]):
        system_audits_inner.append(
            {
                "id": id * 100 + i,
                "parent_id": parent_id * 100 + i if parent_id >= 0 else -2,
                "content": random_base64(
                    min_len=MIN_RANDOM_BASE64_LEN, max_len=MAX_RANDOM_BASE64_LEN
                ),
            }
        )
system_audits_inner_pd = pd.DataFrame(system_audits_inner)
system_audits_inner_pd.astype({"parent_id": int})
system_audits_inner_pd["id"] += 1
system_audits_inner_pd["parent_id"] += 1
system_audits_inner_pd.iloc[
    : system_audits_pd.shape[0], system_audits_inner_pd.columns.get_loc("content")
] = system_audits_pd["content"].values

# Save & print
save_table(system_audits_inner_pd, "system_audits_inner.csv")
print("Number of inner system audits:", system_audits_inner_pd.shape[0])
print("")

# ==================================
# === Create safety_controls.csv ===
# ==================================

safety_controls_pd = read_seed("safety_controls.csv")
save_table(safety_controls_pd, "safety_controls.csv")
print("Number of safety control policies:", safety_controls_pd.shape[0])
