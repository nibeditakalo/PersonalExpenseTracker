import json
import os

DATA_FILE = "data/expenses_data.json"

def load_data(tracker):
    if os.path.exists(tracker.filename):
        data = json.load(tracker.filename)
        tracker.expenses = data.get("expenses", [])
        tracker.budgets = data.get("budgets", {"overall": 0.0})
    else:
        tracker.expenses = []
        tracker.budget = {"overall": 0.0}


def save_data(tracker):
    data = {"expenses": tracker.expenses, "budgets": tracker.budgets}
    with open(tracker.filename, "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved..")