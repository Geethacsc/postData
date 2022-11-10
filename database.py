from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Employee

engine = create_engine(
    "postgresql://myuser:mypass@localhost/mydb",
    echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

