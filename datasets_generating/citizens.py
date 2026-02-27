import datetime
from faker import Faker
import numpy as np
import pandas as pd

SEED = 42

rng = np.random.default_rng(seed=SEED)
fake = Faker()
today_date = datetime.date.today()


def random_citizen() -> object:

    # Time and ID
    age_day = int(rng.integers(1, 91 * 365))
    birth_date = today_date - datetime.timedelta(days=age_day)
    age_year = today_date.year - birth_date.year
    if today_date.month < birth_date.month or (
        today_date.month == birth_date.month and today_date.day < birth_date.day
    ):
        age_year -= 1
    id = f"{birth_date.year}{birth_date.month:02d}{birth_date.day:02d}{rng.integers(10000):04d}"

    # Name and sex
    sex, name = (
        ("male", fake.name_male())
        if rng.random() < 0.5
        else ("female", fake.name_female())
    )

    return {
        "id": id,
        "name": name,
        "sex": sex,
        "birthday": f"{birth_date.year}-{birth_date.month:02d}-{birth_date.day:02d}",
        "age": age_year,
    }
