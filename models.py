from dataclasses import dataclass

@dataclass
class Expense:
  date: str
  category: str
  amount: str
  description: str