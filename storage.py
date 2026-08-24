import json
import os

DATA_FILE = "data/expenses_data.json"

def load_data(tracker):
    if not os.path.exists(tracker.filename):
        tracker.expenses = []
        tracker.budgets = {"overall": 0.0}
        return

    with open(tracker.filename, "r") as f:
        data = json.load(f)

    tracker.expenses = data.get("expenses", [])
    tracker.budgets = data.get("budgets", {"overall": 0.0})


def save_data(tracker):
    data = {"expenses": tracker.expenses, "budgets": tracker.budgets}
    with open(tracker.filename, "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved..")