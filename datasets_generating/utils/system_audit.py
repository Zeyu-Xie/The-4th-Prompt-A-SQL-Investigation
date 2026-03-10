import datetime
import hashlib
import numpy as np
import os


def get_sha256(text):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode("utf-8"))
    return sha256_hash.hexdigest()


# Lines
with open(os.path.join(os.path.dirname(__file__), "system_audit.txt"), "r") as f:
    lines = f.readlines()
lines = np.array([line[:-1] for line in lines])

# Dates
dates = [
    datetime.date(year, month, 20)
    for year in range(2070, 2078)
    for month in [3, 6, 9, 12]
]

# All
id = 0
system_audits = []
for date in dates:
    for _ in range(3):
        system_audits.append(
            {
                "id": id + 1,
                "log_date": date.isoformat(),
                "content": lines[id],
                "SHA-256": get_sha256(lines[id]),
                "is_flag_hidden": False,
            }
        )
        id += 1


# Select
def generate_all_system_audits(date: datetime.date) -> list[object]:
    num_dates = 0
    for _date in dates:
        if _date < date:
            num_dates += 1
        else:
            break
    return system_audits[0 : num_dates * 3]
