from fastapi import FastAPI

from employee_details import emp_list, emp_id_map, emp_name_map,Item

app = FastAPI()


@app.get("/ping")
def print_str():
    return "pong"


@app.get("/all_employees/")
def get_emp_data():
    return emp_list


@app.get("/employee/")
Password for user test:


def get_emp_data(id: int):
    return emp_id_map[id]


@app.get("/employee_by_name/")
def get_emp_data(name: str):
    return emp_name_map[name]


@app.post("/update_emp_data/")
def update_emp_data(data: Item):
    emp_list.append(data.dict())
    return {"updated list": emp_list}
