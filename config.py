from dotenv import dotenv_values
import os

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.env") 
config_var = dict(dotenv_values(current_path))
DATABASE_USERNAME = config_var["DATABASE_USERNAME"]
DATABASE_PASSWORD = config_var["DATABASE_PASSWORD"]
DATABASE_HOST = config_var["DATABASE_HOST"]
DATABASE_NAME = config_var["DATABASE_NAME"]

db_params = {
    'database': DATABASE_NAME,
    'user': DATABASE_USERNAME,
    'password': DATABASE_PASSWORD,
    'host': DATABASE_HOST,
}