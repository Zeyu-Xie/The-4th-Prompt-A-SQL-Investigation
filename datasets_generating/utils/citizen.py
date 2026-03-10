import datetime
from faker import Faker
import numpy as np

RNG_SEED = 42
FAKER_SEED = 42
AREA_CODE = "en_US"
AGE_DAY_FROM = 1
AGE_DAY_TO = 365 * 91
SOCIAL_CREDIT_LOC = 50.0
SOCIAL_CREDIT_SCALE = 15.0

rng = np.random.default_rng(seed=RNG_SEED)
fake = Faker(AREA_CODE)
Faker.seed(FAKER_SEED)


def random_birthday(
    age_day_from: int, age_day_to: int, current_date: datetime.date
) -> datetime.date:
    age_day = int(rng.integers(age_day_from, age_day_to))
    birthday = current_date - datetime.timedelta(days=age_day)
    return birthday


def calc_age_year(birthday: datetime.date, current_date: datetime.date) -> int:
    n = current_date.year - birthday.year
    if current_date.month < birthday.month or (
        current_date.month == birthday.month and current_date.day < birthday.day
    ):
        return n - 1
    return n


def random_id(birthday: datetime.date) -> str:
    return f"{birthday.year}{birthday.month:02d}{birthday.day:02d}{rng.integers(10000):04d}"


def random_sex() -> str:
    return "male" if rng.random() < 0.5 else "female"


def random_first_name(sex: str) -> str:
    return fake.first_name_male() if sex == "male" else fake.first_name_female()


def random_last_name() -> str:
    return fake.last_name()


def random_social_credit(loc: float, scale: float) -> int:
    raw = int(rng.normal(loc=loc, scale=scale))
    if raw < 0:
        return 0
    if raw > 100:
        return 100
    return raw


def random_citizen(current_date: datetime.date) -> object:

    # Time and ID
    birthday = random_birthday(
        age_day_from=AGE_DAY_FROM, age_day_to=AGE_DAY_TO, current_date=current_date
    )
    age_year = calc_age_year(birthday, current_date=current_date)
    id = random_id(birthday)

    # Name and sex
    sex = random_sex()
    first_name = random_first_name(sex)
    last_name = random_last_name()

    # Social credit
    social_credit = (
        random_social_credit(loc=SOCIAL_CREDIT_LOC, scale=SOCIAL_CREDIT_SCALE)
        if age_year >= 18
        else None
    )

    return {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "sex": sex,
        "birthday": f"{birthday.year}-{birthday.month:02d}-{birthday.day:02d}",
        "age": age_year,
        "social_credit": social_credit,
    }
