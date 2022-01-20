# Create database and table using SQLAlchemy and Python module
from app import * 
try:
    db.create_all()#SQLAlchemy内置函数
    print("Database successfully created.")
except Exception as e:
    print("Exception occurred.",e)
