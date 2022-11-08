from pydantic.main import BaseModel

ravin_data = {"id": 1, "name": "Ravin", "position": "MD"}
chandu_data = {"id": 2, "name": "Chandu", "position": "Intern"}
geetha_data = {"id": 3, "name": "geetha", "position": "Intern"}
emp_list = [ravin_data, chandu_data, geetha_data]

emp_id_map = {}
emp_name_map = {}
for employee in emp_list:
    emp_id_map[employee["id"]] = employee
    emp_name_map[employee["name"]] = employee

print(emp_id_map)
print(emp_name_map)


class Item(BaseModel):
    id: int
    name: str
    position: str
