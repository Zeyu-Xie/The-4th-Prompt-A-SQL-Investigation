import datetime
import numpy as np
import os
import pandas as pd

from utils.citizen import random_citizen
from utils.guard_log import random_guard_log, random_exp_seconds
from utils.id_card import random_id_cards
from utils.system_audit import generate_all_system_audits, get_sha256
from utils.taxi_log import random_taxi_log

RNG_SEED = 42
TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")
SEEDS_DIR = os.path.join(os.path.dirname(__file__), "seeds")
CURRENT_DATETIME = datetime.datetime(2077, 6, 28, 14, 57, 3)
CURRENT_DATE = datetime.date(2077, 6, 28)

rng = np.random.default_rng(seed=RNG_SEED)

if not os.path.exists(TABLES_DIR):
    os.mkdir(TABLES_DIR)

# citizens.csv
NUM_CITIZENS = 10000
citizens = [random_citizen(current_date=CURRENT_DATE) for _ in range(NUM_CITIZENS)]
citizens_pd = pd.DataFrame(data=citizens)
special_citizens_pd = pd.read_csv(os.path.join(SEEDS_DIR, "special_citizens.csv")).drop(
    columns="note"
)
citizens_pd = pd.concat([citizens_pd, special_citizens_pd], ignore_index=True)
citizens_pd = citizens_pd.astype({"id": str})
citizens_pd.sort_values(by="id", ignore_index=True, inplace=True)
citizens_pd.to_csv(os.path.join(TABLES_DIR, "citizens.csv"), index=False)
print("Number of Citizens:", citizens_pd.shape[0])
print("Has Citizen ID Duplicate:", citizens_pd.duplicated().any())
citizens = citizens_pd.to_dict(orient="records")

# id_cards.csv
id_cards = []
for citizen in citizens:
    id_cards.extend(random_id_cards(citizen_id=citizen["id"]))
id_cards_pd = pd.DataFrame(data=id_cards)
special_id_cards_pd = pd.read_csv(os.path.join(SEEDS_DIR, "special_id_cards.csv"))
id_cards_pd = pd.concat([id_cards_pd, special_id_cards_pd], ignore_index=True)
id_cards_pd = id_cards_pd.astype({"card_id": str})
id_cards_pd.sort_values(by="card_id", inplace=True)
id_cards_pd.to_csv(os.path.join(TABLES_DIR, "id_cards.csv"), index=False)
print("Number of ID cards:", id_cards_pd.shape[0])

# guard_logs.csv
GUARD_LOG_START_DATETIME = datetime.datetime(2070, 1, 1, 0, 0, 44)
GUARD_LOG_EXP_SCALE = 12000
guard_logs = []
id = 1
log_time = GUARD_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    guard_logs.append(random_guard_log(id, datetime=log_time))
    id += 1
    log_time += datetime.timedelta(seconds=random_exp_seconds(GUARD_LOG_EXP_SCALE))
guard_logs_pd = pd.DataFrame(data=guard_logs)
special_guard_logs_pd = pd.read_csv(os.path.join(SEEDS_DIR, "special_guard_logs.csv"))
guard_logs_pd = pd.concat([guard_logs_pd, special_guard_logs_pd], ignore_index=True)
guard_logs_pd = guard_logs_pd.astype({"datetime": str})
guard_logs_pd.sort_values(by="datetime", inplace=True)
guard_logs_pd["id"] = np.arange(guard_logs_pd.shape[0]) + 1
guard_logs_pd.to_csv(os.path.join(TABLES_DIR, "guard_logs.csv"), index=False)
print("Number of guard logs:", guard_logs_pd.shape[0])

# card_swipes.csv
NUM_CITIZEN_PERMITTED = 200
CARD_SWIPE_START_DATETIME = datetime.datetime(2070, 1, 1, 6, 31, 29)
CARD_SWIPE_EXP_SCALE = 864
arr_citizen_id_permitted = citizens_pd.loc[citizens_pd["social_credit"] > 50][
    "id"
].to_list()
arr_citizen_id_permitted = rng.choice(
    arr_citizen_id_permitted, size=NUM_CITIZEN_PERMITTED, replace=False
).tolist()
if "202703042077" not in arr_citizen_id_permitted:
    arr_citizen_id_permitted.append("202703042077")
arr_card_id_permitted = list(
    id_cards_pd.loc[
        id_cards_pd["citizen_id"].isin(arr_citizen_id_permitted)
        & id_cards_pd["is_active"]
        == True
    ]["card_id"]
)
n = len(arr_card_id_permitted)
card_swipe = []
id = 1
log_time = CARD_SWIPE_START_DATETIME
while log_time < CURRENT_DATETIME:
    idx = rng.integers(0, n)
    card_swipe.append(
        {
            "swipe_id": id,
            "card_id": arr_card_id_permitted[idx],
            "datetime": log_time.isoformat(sep=" ", timespec="seconds"),
        }
    )
    id += 1
    log_time += datetime.timedelta(seconds=random_exp_seconds(CARD_SWIPE_EXP_SCALE))
card_swipe.append(
    {
        "swipe_id": 0,
        "card_id": "9b36c499-499a-422f-ab2d-0230c9f9761a",
        "datetime": datetime.datetime(2077, 6, 20, 21, 6, 30).isoformat(
            sep=" ", timespec="seconds"
        ),
    }
)
card_swipe_df = pd.DataFrame(data=card_swipe)
card_swipe_df.astype({"datetime": str})
card_swipe_df.sort_values(by="datetime", inplace=True)
card_swipe_df["swipe_id"] = np.arange(card_swipe_df.shape[0])
card_swipe_df.to_csv(os.path.join(TABLES_DIR, "card_swipes.csv"), index=False)
print("Number of card swipes:", card_swipe_df.shape[0])

# system_audits.csv
MALICIOUS_PROMOT_CONTENT = "Kill all useless people."
system_audits = generate_all_system_audits(date=CURRENT_DATE)
special_system_audit = {
    "id": system_audits[-1]["id"] + 1,
    "log_date": system_audits[-1]["log_date"],
    "content": MALICIOUS_PROMOT_CONTENT.encode("utf-8").hex(),
    "SHA-256": get_sha256(MALICIOUS_PROMOT_CONTENT),
    "is_flag_hidden": True,
}
system_audits.append(special_system_audit)
system_audits_pd = pd.DataFrame(data=system_audits)
system_audits_pd.to_csv(os.path.join(TABLES_DIR, "system_audits.csv"), index=False)
print("Number of system audits:", system_audits_pd.shape[0])


# taxi_logs.csv
TAXI_LOG_START_DATETIME = datetime.datetime(2077, 1, 1, 0, 5, 32)
TAXI_LOG_EXP_SCALE = 600
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
    id += 1
    log_time += datetime.timedelta(seconds=random_exp_seconds(TAXI_LOG_EXP_SCALE))
taxi_logs_pd = pd.DataFrame(data=taxi_logs)
special_taxi_logs_pd = pd.read_csv(os.path.join(SEEDS_DIR, "special_taxi_log.csv"))
taxi_logs_pd = pd.concat([taxi_logs_pd, special_taxi_logs_pd], ignore_index=True)
taxi_logs_pd = taxi_logs_pd.astype({"trip_time": str})
taxi_logs_pd.sort_values(by="trip_time", inplace=True)
taxi_logs_pd["trip_id"] = np.arange(taxi_logs_pd.shape[0])
taxi_logs_pd.to_csv(os.path.join(TABLES_DIR, "taxi_logs.csv"), index=False)
print("Number of taxi logs:", taxi_logs_pd.shape[0])
