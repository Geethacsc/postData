import re
from datetime import date

from fastapi import FastAPI, Body, HTTPException
from starlette.responses import Response

import models
from database import session, Session
from employee_details import emp_list, emp_id_map, emp_name_map, Item, Year, regex
from models import Employee

app = FastAPI()


@app.get("/v2/all_employees")
def get_all_employees():
    return session.query(Employee).all()


# @app.get("/v2/employee")
# def get_employee_by_id(emp_id: int):
#     return session.query(Employee).filter_by(id=emp_id).first()
# the abelow method can be performed using the above /v2/employee in comments

@app.get("/v2/employee")
def get_employee_by_id(emp_id: int):
    if emp_id >= 4:
        raise HTTPException(status_code=404, detail="employee id not found")
    return session.query(Employee).filter(Employee.id == emp_id).first()


# Handle Errors using IF STATEMENT
@app.put("/v2/update_employee")
def update_data(emp: Year):
    with session.begin():
        session.query(Employee).filter(Employee.yob == 1990). \
            update({Employee.yob: emp.yob}, synchronize_session=False)
        session.commit()
    return session.query(Employee).filter(Employee.yob == emp.yob).all()


# Handle Errors Using Try Catch Block
@app.post("/v2/update_employees")
def update_database(old_yob: int = Body(..., embed=True), new_yob: int = Body(..., embed=True)):
    try:
        today = date.today()
        if new_yob > today.year:
            return Response("Bad Request", status_code=400)
        else:
            with session.begin():
                rowcount = session.query(Employee).filter(Employee.yob == old_yob). \
                    update({Employee.yob: new_yob}, synchronize_session=False)
                session.commit()

            return session.query(Employee).filter(Employee.yob == new_yob).all()
    except Exception as e:
        print("Error occured: ", e)
        return Response("Year not Found", status_code=404)
    finally:
        session.close()


@app.patch("/v2/delete_employee")
def delete_data(year: int):
    with session.begin():
        session.query(Employee).filter(Employee.yob == year). \
            delete(synchronize_session=False)
        session.commit()
    return session.query(Employee).all()


@app.post("/v2/update_email")
def update_email(emp_id: int = Body(..., embed=True), email: str = Body(..., embed=True)):
    try:
        if re.fullmatch(regex, email):
            with session.begin():
                session.query(Employee).filter(Employee.id == emp_id). \
                    update({Employee.email_id: email}, synchronize_session=False)
            session.commit()
            session.close()
            return session.query(Employee).filter(Employee.email_id == email).all()
    except:
        return Response('Enter Valid email id', status_code=400)
    finally:
        session.close()


@app.get("/ping")
def print_str():
    return "pong"


@app.get("/all_employees/")
def get_emp_data():
    return emp_list


@app.get("/employee/")
def get_emp_data(emp_id: int):
    return emp_id_map[emp_id]


@app.get("/employee_by_name/")
def get_emp_data(name: str):
    return emp_name_map[name]


@app.post("/update_emp_data/")
def update_emp_data(data: Item):
    emp_list.append(data.dict())
    return {"updated list": emp_list}
