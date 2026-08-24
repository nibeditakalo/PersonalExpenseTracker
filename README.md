# Personal Expense Tracker

A command-line application for logging daily expenses, organizing them by category, tracking spending against monthly budgets, and persisting everything to disk between runs.

## Overview

In today's fast-paced world, individuals need to track and manage their expenses effectively. This tracker lets a user log expenses as they happen, assign each one to a category, set an overall and/or per-category monthly budget, and see at a glance how actual spending compares to that budget — all through a simple interactive menu.

## Features

- Log expenses with date, category, amount, and an optional description
- Categorize expenses (Food, Rent, Travel, etc.)
- Set an overall monthly budget and/or a budget per category
- View all expenses, or filter by a specific month
- Generate a formatted expense report showing spending by category, percentage of total, and budget status
- Automatically save data to a JSON file after every change, and reload it on startup
- Input validation throughout, so the menu loop never crashes on bad input

## Project Structure

```
personal_expense_tracker/
├── main.py              # Entry point — wires everything together and starts the app
├── models.py            # Expense data class
├── storage.py           # Reading/writing the JSON data file
├── tracker.py           # ExpenseTracker — core logic: add expenses, manage budgets, compute totals
├── cli.py               # Menu display, input validation helpers, and the main interaction loop
├── data/
│   └── expenses_data.json   # Created at runtime; holds saved expenses and budgets

```

Each module has a single responsibility: `models.py` defines what an expense *is*, `storage.py` is the only place that touches the filesystem, `tracker.py` holds the business logic, `reports.py` turns that logic into readable output, and `cli.py` is the only place that calls `input()`/`print()`. This separation keeps the core logic testable without needing to simulate user input or file I/O.

## Requirements

- Python 3.8 or later
- No external dependencies — the project uses only the standard library (`json`, `os`, `datetime`, `dataclasses`, `collections`)

## Getting Started

1. Clone or download this project.
2. From the project root, run:

   ```bash
   python main.py
   ```

3. The app will create `data/expenses_data.json` automatically the first time you save an expense or budget — no manual setup needed.

## Menu Options

```
===== Personal Expense Tracker =====
1. Add expense
2. View all expenses
3. View expenses for a specific month (YYYY-MM)
4. Set overall monthly budget
5. Set category budget
6. Check budget status
7. Display expense report
8. Exit
======================================
```

- **Add expense** — prompts for category, amount, an optional description, and a date (defaults to today if left blank).
- **View all expenses** — lists every logged expense with its date, category, amount, and description.
- **View expenses for a specific month** — same as above, filtered to a `YYYY-MM` month.
- **Set overall monthly budget** — sets a single budget figure covering all spending.
- **Set category budget** — sets a budget limit for one specific category (e.g. Food).
- **Check budget status** — shows spend-vs-budget for the overall total and any category with a budget set, flagging anything over budget.
- **Display expense report** — a formatted summary: totals per category, percentage of overall spend, and remaining budget, sorted by highest spend first.
- **Exit** — saves and closes the application.

## Data Storage

All data is stored in a single JSON file at `data/expenses_data.json`:

```json
{
  "expenses": [
    {
      "date": "2026-08-01",
      "category": "Food",
      "amount": 25.5,
      "description": "Groceries"
    }
  ],
  "budgets": {
    "overall": 1000.0,
    "Food": 300.0
  }
}
```

The file is written after every add-expense or set-budget action, and read back automatically the next time the app starts, so no data is lost between sessions.

## Example Report Output

```
==================================================
              Expense Report for 2026-08
==================================================
Food          150.00  ( 60.0%) ############  | budget 300.00, left 150.00
Rent          100.00  ( 40.0%) ########
--------------------------------------------------
TOTAL         250.00

Overall budget : 1000.00
Remaining      : 750.00
Budget used    : 25.0%
==================================================
```

## Possible Enhancements

- Edit or delete an existing expense
- Export a report to CSV or PDF
- Switch storage from JSON to SQLite for larger datasets
- Color-coded terminal output for over-budget warnings
