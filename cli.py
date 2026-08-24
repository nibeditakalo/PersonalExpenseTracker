from tracker import ExpenseTracker

def run():

    tracker = ExpenseTracker()

    menu = """
===== Personal Expense Tracker =====
1. Add expense
2. View all expenses
3. View expenses for a specific month (YYYY-MM)
4. Set overall monthly budget
5. Set category budget
6. Check budget status
7. Exit
======================================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            category = input("Category (e.g. Food, Rent, Travel): ").strip()
            amount = input("Amount: ").strip()
            description = input("Description (optional): ").strip()
            try:
                tracker.add_expense(category, amount, description)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ").strip()
            tracker.view_expenses(month)

        elif choice == "4":
            amount = input("Enter overall monthly budget: ").strip()
            try:
                tracker.set_budget(amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "5":
            category = input("Category: ").strip()
            amount = input("Budget amount for this category: ").strip()
            try:
                tracker.set_budget(amount, category)
            except ValueError:
                print("Invalid amount.")

        elif choice == "6":
            month = input("Month to check (YYYY-MM), or leave blank for all time: ").strip()
            tracker.check_budget_status(month if month else None)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
