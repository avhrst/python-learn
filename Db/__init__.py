## DB imitating module
import datetime
category = set()
expense = set()
income = set()
income_journal = set()
expense_journal = set()


class Category():
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = category_max_id() + 1
        self._title = title
        
    
class Expense():
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = expense_max_id() + 1
        self._title = title
    
class Income():
    _id: int
    _title: str
    
    def __init__(self, title: str):
        self._id = income_max_id() + 1
        self._title = title
 
class IncomeJournal():
    _id: int
    _amount: float
    _date: datetime
    _category: Category 
    _description: str
    
    def __init__(self, amount: float, date: datetime, category: Category, description: str):
        self._id = income_journal_max_id() + 1
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description
@property
def amount(self):
    if self._amount < 0:
        exception = ValueError("Amount cannot be negative")
    return self._amount        
        

class ExpenseJournal():
    _id: int
    _amount: float
    _date: datetime
    _category: Category
    _description: str
    
    def __init__(self, amount: float, date: datetime, category: Category, description: str):
        self._id = expense_journal_max_id() + 1
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description
        
    @property
    def amount(self):
        if self._amount < 0:
            exception = ValueError("Amount cannot be negative")
        return self._amount    
    

# sequences 
def category_max_id():
    return max([c._id for c in category])
def expense_max_id():
    return max([e.id for e in expense])
def income_max_id():
    return max([i.id for i in income])
def income_journal_max_id():
    return max([ij.id for ij in income_journal])
def expense_journal_max_id():
    return max([ej.id for ej in expense_journal])

# entity operations

def get_category_by_title(title: str):
    for c in category:
        if c._title == title:
            return c
    return None

def add_category(title: str):    
    c = get_category_by_title(title) 
    if c:
        return c
    else:
        c = Category(title)
        category.add(c)
    return c

def get_expence_by_title(title: str):
    for e in expense:
        if e._title == title:
            return e
    return None

def add_expense(title: str):
    e = get_expence_by_title(title)
    if e:
        return e
    else:   
        e = Expense(title)
        expense.add(e)
    return e

def get_income_by_title(title: str):
    for i in income:
        if i._title == title:
            return i
    return None

def add_income(title: str):
    i = get_income_by_title(title)
    if i:
        return i
    else:
        i = Income(title)
        income.add(i)
    return i

def add_income_journal(amount: float, date: datetime, category: Category, description: str):
    ij = IncomeJournal(amount, date, category, description)
    income_journal.add(ij)
    return ij

def add_expense_journal(amount: float, date: datetime, category: Category, description: str):
    ej = ExpenseJournal(amount, date, category, description)
    expense_journal.add(ej)
    return ej

def get_category_by_id(id: int):
    for c in category:
        if c._id == id:
            return c
    return None

def get_expense_by_id(id: int):
    for e in expense:
        if e._id == id:
            return e
    return None

def get_income_by_id(id: int):
    for i in income:
        if i._id == id:
            return i
    return None

def get_income_journal_by_id(id: int):
    for ij in income_journal:
        if ij._id == id:
            return ij
    return None

def get_expense_journal_by_id(id: int):
    for ej in expense_journal:
        if ej._id == id:
            return ej
    return None

def delete_category(id: int):
    c = get_category_by_id(id)
    if c:
        category.remove(c)
        return True
    return False

def delete_expense(id: int):
    e = get_expense_by_id(id)
    if e:
        expense.remove(e)
        return True
    return False

def delete_income(id: int):
    i = get_income_by_id(id)
    if i:
        income.remove(i)
        return True
    return False

def delete_income_journal(id: int):
    ij = get_income_journal_by_id(id)
    if ij:
        income_journal.remove(ij)
        return True
    return False

def delete_expense_journal(id: int):
    ej = get_expense_journal_by_id(id)
    if ej:
        expense_journal.remove(ej)
        return True
    return False

def update_category(id: int, title: str):
    c = get_category_by_id(id)
    if c:
        c._title = title
        return c
    return None

def update_expense(id: int, title: str):
    e = get_expense_by_id(id)
    if e:
        e._title = title
        return e
    return None

def update_income(id: int, title: str):
    i = get_income_by_id(id)
    if i:
        i._title = title
        return i
    return None

def update_income_journal(id: int, amount: float, date: datetime, category: Category, description: str):
    ij = get_income_journal_by_id(id)
    if ij:
        ij._amount = amount
        ij._date = date
        ij._category = category
        ij._description = description
        return ij
    return None

def update_expense_journal(id: int, amount: float, date: datetime, category: Category, description: str):
    ej = get_expense_journal_by_id(id)
    if ej:
        ej._amount = amount
        ej._date = date
        ej._category = category
        ej._description = description
        return ej
    return None

# agregate operations
def get_sum_of_expenses():
    return sum([ej._amount for ej in expense_journal])
def get_sum_of_incomes():
    return sum([ij._amount for ij in income_journal])

def get_sum_of_expenses_by_category(category: Category):
    return sum([ej._amount for ej in expense_journal if ej._category == category])
def get_sum_of_incomes_by_category(category: Category):
    return sum([ij._amount for ij in income_journal if ij._category == category])

def get_sum_of_expenses_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return sum([ej._amount for ej in expense_journal if ej._category == category and ej._date >= start_date and ej._date <= end_date])
def get_sum_of_incomes_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return sum([ij._amount for ij in income_journal if ij._category == category and ij._date >= start_date and ij._date <= end_date])
    
def get_max_expense_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return max([ej._amount for ej in expense_journal if ej._category == category and ej._date >= start_date and ej._date <= end_date])  

def get_max_income_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return max([ij._amount for ij in income_journal if ij._category == category and ij._date >= start_date and ij._date <= end_date])   

def get_min_expense_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return min([ej._amount for ej in expense_journal if ej._category == category and ej._date >= start_date and ej._date <= end_date])
def get_min_income_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return min([ij._amount for ij in income_journal if ij._category == category and ij._date >= start_date and ij._date <= end_date])

def get_average_expense_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return sum([ej._amount for ej in expense_journal if ej._category == category and ej._date >= start_date and ej._date <= end_date]) / len([ej._amount for ej in expense_journal if ej._category == category and ej._date >= start_date and ej._date <= end_date])    
def get_average_income_by_category_and_period(category: Category, start_date: datetime, end_date: datetime):
    return sum([ij._amount for ij in income_journal if ij._category == category and ij._date >= start_date and ij._date <= end_date]) / len([ij._amount for ij in income_journal if ij._category == category and ij._date >= start_date and ij._date <= end_date])

## clear data     
def delete_all_expenses():
    expense_journal.clear()
def delete_all_incomes():
    income_journal.clear()
        
    
    ## Bussines operations
    def add_income(title: str, amount: float, date: datetime, category: Category, description: str):
        i = Income(title)
        add_income(i)
        ij = IncomeJournal(amount, date, category, description)
        add_income_journal(ij)
        return ij
    
    def add_expense(title: str, amount: float, date: datetime, category: Category, description: str):
        e = Expense(title)
        add_expense(e)
        ej = ExpenseJournal(amount, date, category, description)
        add_expense_journal(ej)
        return ej
    
    def change_expense_journal_amount(id: int, amount: float, date: datetime, category: str, description: str):
        ej = get_expense_journal_by_id(id)
        if ej:
            ej._amount = amount
            ej._date = date
            ej._category = get_category_by_title(category)
            ej._description = description
            return ej
        return None

    def change_income_journal_amount(id: int, amount: float, date: datetime, category: str, description: str):
        ij = get_income_journal_by_id(id)
        if ij:
            ij._amount = amount
            ij._date = date
            ij._category = get_category_by_title(category)
            ij._description = description
            return ij
        return None

    def delete_expense_journal(id: int):
        ej = get_expense_journal_by_id(id)
        if ej:
            delete_expense_journal(ej)
            return True
        return False
    
    def delete_income_journal(id: int):
        ij = get_income_journal_by_id(id)
        if ij:
            delete_income_journal(ij)
            return True
        return False
    
    def get_balance():
        income = get_sum_of_incomes()
        expense = get_sum_of_expenses()
        return income - expense
    
    def clear_balance():
        delete_all_incomes()
        delete_all_expenses()       
        return True
    
    def get_journal_by_category(category: str):
        ex = get_sum_of_expenses_by_category(category)
        inc = get_sum_of_incomes_by_category(category)
        d = {"expense": ex, "income": inc}
        return d
    
    def get_income_by_category_and_period(category: str, start: datetime, end: datetime):
        i_sum = get_sum_of_incomes_by_category_and_period(category, start, end)
        i_min = get_min_income_by_category_and_period(category, start, end)
        i_max = get_max_income_by_category_and_period(category, start, end)
        i_avg = get_average_expense_by_category_and_period(category, start, end)
        d = {"sum": i_sum, "min": i_min, "max": i_max, "avg": i_avg}    
        return d
    
    def get_expense_by_category_and_period(category: str, start: datetime, end: datetime):
        e_sum = get_sum_of_expenses_by_category_and_period(category, start, end)
        e_min = get_min_expense_by_category_and_period(category, start, end)
        e_max = get_max_expense_by_category_and_period(category, start, end)
        e_avg = get_average_expense_by_category_and_period(category, start, end)
        d = {"sum": e_sum, "min": e_min, "max": e_max, "avg": e_avg}    
        return d

