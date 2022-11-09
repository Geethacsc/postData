# from sqlalchemy import Table, Integer, String, Column, MetaData, create_engine
#
# engine = create_engine('sqlite:///company.db', echo=True)
# meta = MetaData()
#
# employees = Table(
#     'employee', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('position', String),
# )
# meta.create_all(engine)
# insert_data=employees.insert()
# insert_data = employees.insert().values(name='Paul')
# str(insert_data)
# connection=engine.connect()
# result=connection.execute(insert_data)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://myuser:password@localhost/mydb",
    echo=True
)
Session = sessionmaker(bind=engine)
session = Session()
