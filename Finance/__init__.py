# __init__.py
from pydantic import BaseModel
from datetime import datetime
import Db as db

class Category(BaseModel):
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = db.category_max_id() + 1
        self._title = title
        
    
class Expense(BaseModel):
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = db.expense_max_id() + 1
        self._title = title
    
class Income(BaseModel):
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = db.income_max_id() + 1
        self._title = title
 
class InconeJournal(BaseModel):
    _id: int
    _amount: float
    _date: datetime
    _category: Category 
    _description: str
    
    def __init__(self, amount: float, date: datetime, category: Category, description: str):
        self._id = db.income_journal_max_id() + 1
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description
@property
def amount(self):
    if self._amount < 0:
        exception = ValueError("Amount cannot be negative")
    return self._amount        
        

class ExpenseJournal(BaseModel):
    _id: int
    _amount: float
    _date: datetime
    _category: Category
    _description: str
    
    def __init__(self, amount: float, date: datetime, category: Category, description: str):
        self._id = db.expense_journal_max_id() + 1
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description
        
    @property
    def amount(self):
        if self._amount < 0:
            exception = ValueError("Amount cannot be negative")
        return self._amount    
    
    
    ## Bussines operations
    def add_income(title: str, amount: float, date: datetime, category: Category, description: str):
        i = Income(title)
        db.add_income(i)
        ij = InconeJournal(amount, date, category, description)
        db.add_income_journal(ij)
        return ij
    
    def add_expense(title: str, amount: float, date: datetime, category: Category, description: str):
        e = Expense(title)
        db.add_expense(e)
        ej = ExpenseJournal(amount, date, category, description)
        db.add_expense_journal(ej)
        return ej
    
    def change_expense_journal_amount(id: int, amount: float, date: datetime, category: str, description: str):
        ej = db.get_expense_journal_by_id(id)
        if ej:
            ej._amount = amount
            ej._date = date
            ej._category = db.get_category_by_title(category)
            ej._description = description
            return ej
        return None

    def change_income_journal_amount(id: int, amount: float, date: datetime, category: str, description: str):
        ij = db.get_income_journal_by_id(id)
        if ij:
            ij._amount = amount
            ij._date = date
            ij._category = db.get_category_by_title(category)
            ij._description = description
            return ij
        return None

    def delete_expense_journal(id: int):
        ej = db.get_expense_journal_by_id(id)
        if ej:
            db.delete_expense_journal(ej)
            return True
        return False
    
    def delete_income_journal(id: int):
        ij = db.get_income_journal_by_id(id)
        if ij:
            db.delete_income_journal(ij)
            return True
        return False
    
    def get_balance():
        income = db.income_total()
        expense = db.expense_total()
        return income - expense
    
    def clear_balance():
        db.delete_all_incomes()
        db.delete_all_expenses()       
        return True
    
    def get_journ_by_categiry(category: str):
        ex = db.get_sum_of_expenses_by_category(category)
        inc = db.get_sum_of_incomes_by_category(category)
        d = {"expense": ex, "income": inc}
        return d
    
    def get_income_by_category_and_period(category: str, start: datetime, end: datetime):
        i_sum = db.get_sum_of_incomes_by_category_and_period(category, start, end)
        i_min = db.get_min_income_by_category_and_period(category, start, end)
        i_max = db.get_max_income_by_category_and_period(category, start, end)
        i_avg = db.get_average_expense_by_category_and_period(category, start, end)
        d = {"sum": i_sum, "min": i_min, "max": i_max, "avg": i_avg}    
        return d
    
    def get_expense_by_category_and_period(category: str, start: datetime, end: datetime):
        e_sum = db.get_sum_of_expenses_by_category_and_period(category, start, end)
        e_min = db.get_min_expense_by_category_and_period(category, start, end)
        e_max = db.get_max_expense_by_category_and_period(category, start, end)
        e_avg = db.get_average_expense_by_category_and_period(category, start, end)
        d = {"sum": e_sum, "min": e_min, "max": e_max, "avg": e_avg}    
        return d
    
    
        
    
    