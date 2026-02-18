#!/usr/local/bin/python3
import mysql.connector
import time

LOG_FILE = "coordinator.log"

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {msg}\n")

def connect(db_name):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="user_password",
        database=db_name,
        autocommit=False
    )


log("TXN_START")

dbs = {
    "db1": connect("database1"),
    "db2": connect("database2"),
    "db3": connect("database3")
}

cursors = {name: db.cursor() for name, db in dbs.items()}

print("PHASE 1: PREPARE")

try:
    cursors["db1"].execute(
        "UPDATE accounts SET balance = balance - 100 WHERE id = 1;"
    )
    log("VOTE db1 YES")

    cursors["db2"].execute(
        "UPDATE accounts SET balance = balance + 'abc' WHERE id = 1;"
    )
    log("VOTE db2 YES")

    cursors["db3"].execute(
        "UPDATE accounts SET balance = balance + 50 WHERE id = 1;"
    )
    log("VOTE db3 YES")

    log("PREPARED")

except Exception as e:
    print("Prepare phase failed:", e)
    log("GLOBAL_ABORT")

    for db in dbs.values():
        db.rollback()

    print("GLOBAL ROLLBACK")
    exit(1)

# Phase 2
log("GLOBAL_COMMIT")
print("\nPHASE 2: COMMIT")

for db in dbs.values():
    db.commit()

print("GLOBAL COMMIT")

# see change made
for name, cursor in cursors.items():
    cursor.execute("SELECT * FROM accounts;")
    print(name, cursor.fetchall())

for db in dbs.values():
    db.close()
