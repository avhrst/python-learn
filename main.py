from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import datetime
import Db as db

app = FastAPI()
 
@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

## POST
@app.post("/expense")
def create_expense(title: str, amount: float, date: datetime, category: str, description: str):
    return db.add_expense(title, amount, date, category, description)      

@app.post("/income")
def create_income(title: str, amount: float, date: datetime, category: str, description: str):
    return db.add_income(title, amount, date, category, description)

## PUT
@app.put("/expense/{id}")
def update_expense(id: int, amount: float, date: datetime, category: str, description: str):
    return db.change_expense_journal_amount(id, amount, date, category, description)

@app.put("/income/{id}")
def update_income(id: int, amount: float, date: datetime, category: str, description: str):
    return db.change_income_journal_amount(id, amount, date, category, description)

## DELETE
@app.delete("/expense/{id}")
def delete_expense(id: int):
    return db.delete_expense_journal(id)

@app.delete("/income/{id}")
def delete_income(id: int):
    return db.delete_income_journal(id)

@app.delete("/clear")
def clear_balance():
    return db.clear_balance()

## GET
@app.get("/balance")
def get_balance():
    return db.get_balance()

@app.get("/journal/categories/{category}")
def get_journal_by_category(category: str):
    return db.get_journal_by_category(category)

@app.get("/statistics/income/{category}/{start_date}/{end_date}")
def get_income_by_category_and_period(category: str, start_date: datetime, end_date: datetime):
    return db.get_income_by_category_and_period(category, start_date, end_date)

@app.get("/statistics/expense/{category}/{start_date}/{end_date}")
def get_expense_by_category_and_period(category: str, start_date: datetime, end_date: datetime):
    return db.get_expense_by_category_and_period(category, start_date, end_date)


