import requests
import pandas as pd
import sqlalchemy

api_url = 'http://api.coincap.io/v2/assets'
api_header = {"Content-Type": "application/json","Accept-Encoding":"Deflate"}

api_response = requests.get(api_url,headers=api_header)

df = pd.json_normalize(api_response.json(),'data')

#create connection string
engine = sqlalchemy.create_engine('mssql+pyodbc://DESKTOP-09QD1EI\\SQLEXPRESS/sanjay_db?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
df.to_sql(name='factcrypto',con=engine,index=False,if_exists='fail')