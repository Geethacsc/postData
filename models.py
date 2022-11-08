from sqlalchemy import Table, Integer, String, Column, MetaData, create_engine

engine = create_engine('sqlite:///company.db', echo=True)
meta = MetaData()

employees = Table(
    'employee_data', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('position', String),
)
meta.create_all(engine)
insert_data=employee_data.insert()
insert_data = employee_data.insert().values(name='Paul')
str(insert_data)
connection=engine.connect()
result=connection.execute(insert_data)