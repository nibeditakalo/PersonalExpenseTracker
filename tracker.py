from datetime import date, datetime
from collections import defaultdict
from storage import DATA_FILE
from storage import load_data, save_data

class ExpenseTracker:

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.expenses = []
        self.budgets = {"overall": 0.0}
        load_data(self)

    # ----- Core Operations ------

    def add_expense(self, category, amount, description="", exp_date=None):
        exp_date = exp_date or datetime.now().strftime("%Y-%m-%d")
        expense = {
            "date": exp_date,
            "category": category,
            "amount": round(float(amount), 2),
            "description": description
        }
        self.expenses.append(expense)
        save_data(self)
        print(f"Added: {category} - {amount} on {exp_date}")

    def view_expenses(self, month=None):
        filtered = self.expenses
        if month:
            filtered = [e for e in self.expenses if e["date"].startswith(month)]
        if not filtered:
            print("No expenses found.")
            return
        for i, e in enumerate(filtered, 1):
            print(f"{i}. {e['date']} | {e['category']:<12} | {e['amount']:>8.2f} | {e['description']}")

    def set_budget(self, amount, category="overall"):
        self.budgets[category] = float(amount)
        save_data(self)
        print(f"Budget for '{category}' set to {amount}")

    def spending_by_category(self, month=None):
        totals = defaultdict(float)
        for e in self.expenses:
            if month and not e["date"].startswith(month):
                continue
            totals[e["category"]] += e["amount"]
        return totals

    def check_budget_status(self, month=None):
        totals = self.spending_by_category(month)
        overall_spent = sum(totals.values())
        overall_budget = self.budgets.get("overall", 0.0)

        print(f"\n--- Budget Status {'for ' + month if month else ''} ---")
        print(f"Overall: spent {overall_spent:.2f} / budget {overall_budget:.2f}", end="")
        print("  [OVER BUDGET]" if overall_budget and overall_spent > overall_budget else "")

        for cat, spent in totals.items():
            cat_budget = self.budgets.get(cat)
            if cat_budget is not None:
                status = "  [OVER BUDGET]" if spent > cat_budget else ""
                print(f"{cat:<12}: spent {spent:.2f} / budget {cat_budget:.2f}{status}")