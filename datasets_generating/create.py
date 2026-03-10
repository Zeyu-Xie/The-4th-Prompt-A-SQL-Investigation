import numpy as np
import os
import pandas as pd

from utils.citizen import *
from utils.id_card import *

TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")
NUM_CITIZENS = 121

# citizens.csv
citizens = [random_citizen() for _ in range(NUM_CITIZENS)]
citizens_pd = pd.DataFrame(data=citizens)
citizens_pd.to_csv(os.path.join(TABLES_DIR, "citizens.csv"), index=False)

# id_cards.csv
id_cards = []
for citizen in citizens:
    id_cards.extend(random_id_cards(citizen_id=citizen["id"]))
id_cards_pd = pd.DataFrame(data=id_cards)
id_cards_pd.to_csv(os.path.join(TABLES_DIR, "id_cards.csv"), index=False)
