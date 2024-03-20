import yaml
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

with open('credentials.yaml') as file:
    data = yaml.safe_load(file)

engine = create_engine(f"{data['RDS_DATABASE_TYPE']}+{data['RDS_DBAPI']}://{data['RDS_USER']}:{data['RDS_PASSWORD']}@{data['RDS_HOST']}:{data['RDS_PORT']}/{data['RDS_DATABASE']}")

new_engine = engine.connect()

loan_payments = pd.read_sql_table('loan_payments', new_engine)    