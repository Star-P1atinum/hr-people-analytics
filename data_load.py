import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('/Users/kathir/Downloads/portfolio3/WA_Fn-UseC_-HR-Employee-Attrition.csv', encoding='latin1')
print(len(df), list(df.columns))

engine = create_engine('mysql+mysqlconnector://root:kathir%40sql25@localhost/hr_analysis')

with engine.connect() as conn:
    df.to_sql('hr_attrition', con=conn, if_exists='replace', index=False)

print("Done. Rows:", len(df))