import sqlite3
import pandas as pd
import glob
import os

# Parameters
TABLE_DIR = os.path.join(os.path.dirname(__file__), "tables")
DB_DIR = os.path.join(os.path.dirname(__file__), "dbs")
DB_PATH = os.path.join(DB_DIR, "OSIRIS.db")

# Folders & files preparation
if not os.path.exists(TABLE_DIR):
    raise FileNotFoundError(f"Table directory does not exist: {TABLE_DIR}. ")
if not os.path.exists(DB_DIR):
    print(f"Creating database dir {DB_DIR}... ")
    os.mkdir(DB_DIR)
csv_files = glob.glob(pathname="*.csv", root_dir=TABLE_DIR)
print("")

# Connect
print(f"Connecting to the database {DB_PATH}... ")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
print("")

# Load all csv files
for i, csv_file in enumerate(csv_files):
    table_path = os.path.join(TABLE_DIR, csv_file)
    table_name = os.path.splitext(csv_file)[0]
    print(f"[{i + 1}/{len(csv_files)}]Loading {table_path} to table [{table_name}]... ")
    df = pd.read_csv(table_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Successfully loaded {table_name}. ")
print("")

# Check loading result
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"Loading finished. There are {len(tables)} tables in the database. ")
for table in tables:
    print(f"- {table[0]}")

# Close
conn.close()
