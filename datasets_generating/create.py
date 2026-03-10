import numpy as np
import os
import pandas as pd

from utils.citizen import *
from utils.guard_log import *
from utils.id_card import *

TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")
CURRENT_DATETIME = datetime.datetime(2077, 6, 28, 14, 57, 3)
CURRENT_DATE = datetime.date(2077, 6, 28)

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
GUARD_LOG_START_DATETIME = datetime.datetime(2077, 1, 1, 0, 44, 7)
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
