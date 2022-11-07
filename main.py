from datetime import date
from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI, Path
from employee_details import emp_data

app = FastAPI()


class NewData(BaseModel):
    id: int
    name: str
    date_of_birth: date


@app.get("/emp_data/{emp_id}")
def get_emp_data(emp_id: int = Path(None, description="Enter the id")):
    return emp_data[emp_id]


@app.post("/add_data")
def update_emp_data(data: NewData):
    print(f"data is: {data}")
    emp_data.append(data)
    return emp_data
