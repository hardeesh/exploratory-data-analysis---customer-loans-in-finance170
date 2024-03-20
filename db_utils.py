import yaml
import pandas as pd
from sqlalchemy import create_engine

with open('credentials.yaml') as file:
    data = yaml.safe_load(file)

class RDSDatabaseConnector:
    def __init__(self, data):
        self.data = data
        self.engine = self.using_engine(self.data)
        self.extraction()
         
    def using_engine(self, data):
        self.engine = create_engine(f"{data['RDS_DATABASE_TYPE']}+{data['RDS_DBAPI']}://{data['RDS_USER']}:{data['RDS_PASSWORD']}@{data['RDS_HOST']}:{data['RDS_PORT']}/{data['RDS_DATABASE']}")
        engine = self.engine.connect()
        return engine
    
    def extraction(self):
        loan_payments = pd.read_sql_table('loan_payments', self.engine)
        loan_payments.to_csv(r"C:\Users\harde\Documents\AiCore\Customer Loans in Finance/loan_payments.csv", index=False)
        print(loan_payments)

final_extraction = RDSDatabaseConnector(data)



    



