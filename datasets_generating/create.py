import datetime
import numpy as np
import os
import pandas as pd

from utils.citizen import random_citizen
from utils.guard_log import random_guard_log, random_exp_seconds
from utils.id_card import random_id_cards
from utils.system_audit import generate_all_system_audits
from utils.taxi_log import random_taxi_log

RNG_SEED = 42
TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")
CURRENT_DATETIME = datetime.datetime(2077, 6, 28, 14, 57, 3)
CURRENT_DATE = datetime.date(2077, 6, 28)

rng = np.random.default_rng(seed=RNG_SEED)

# citizens.csv
NUM_CITIZENS = 121
citizens = [random_citizen(current_date=CURRENT_DATE) for _ in range(NUM_CITIZENS)]
citizens_pd = pd.DataFrame(data=citizens)
citizens_pd.to_csv(os.path.join(TABLES_DIR, "citizens.csv"), index=False)

# id_cards.csv
id_cards = []
for citizen in citizens:
    id_cards.extend(random_id_cards(citizen_id=citizen["id"]))
id_cards_pd = pd.DataFrame(data=id_cards)
id_cards_pd.to_csv(os.path.join(TABLES_DIR, "id_cards.csv"), index=False)

# guard_logs.csv
GUARD_LOG_START_DATETIME = datetime.datetime(2077, 1, 1, 0, 0, 44)
EXP_SCALE = 600
guard_logs = []
id = 1
log_time = GUARD_LOG_START_DATETIME
while log_time < CURRENT_DATETIME:
    guard_logs.append(random_guard_log(id, datetime=log_time))
    id += 1
    log_time += datetime.timedelta(seconds=random_exp_seconds(EXP_SCALE))
guard_logs_pd = pd.DataFrame(data=guard_logs)
guard_logs_pd.to_csv(os.path.join(TABLES_DIR, "guard_logs.csv"), index=False)

# system_audits.csv
system_audits = generate_all_system_audits(date=CURRENT_DATE)
system_audits_pd = pd.DataFrame(data=system_audits)
system_audits_pd.to_csv(os.path.join(TABLES_DIR, "system_audits.csv"), index=False)

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
