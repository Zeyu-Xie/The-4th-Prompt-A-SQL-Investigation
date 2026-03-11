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
print("Citizen ID Duplicate:", citizens_pd.duplicated().any())
citizens = citizens_pd.to_dict(orient="records")

# id_cards.csv
id_cards = []
for citizen in citizens:
    id_cards.extend(random_id_cards(citizen_id=citizen["id"]))
id_cards_pd = pd.DataFrame(data=id_cards)
id_cards_pd.to_csv(os.path.join(TABLES_DIR, "id_cards.csv"), index=False)
print("Number of ID cards:", id_cards_pd.shape[0])

# guard_logs.csv
GUARD_LOG_START_DATETIME = datetime.datetime(2070, 1, 1, 0, 0, 44)
EXP_SCALE = 12000
guard_logs = []
id = 1
log_time = GUARD_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    guard_logs.append(random_guard_log(id, datetime=log_time))
    id += 1
    log_time += datetime.timedelta(seconds=random_exp_seconds(EXP_SCALE))
guard_logs_pd = pd.DataFrame(data=guard_logs)
guard_logs_pd.to_csv(os.path.join(TABLES_DIR, "guard_logs.csv"), index=False)
print("Number of guard logs:", guard_logs_pd.shape[0])

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
EXP_SCALE = 600
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
    log_time += datetime.timedelta(seconds=random_exp_seconds(EXP_SCALE))
taxi_logs_pd = pd.DataFrame(data=taxi_logs)
taxi_logs_pd.to_csv(os.path.join(TABLES_DIR, "taxi_logs.csv"), index=False)
