import requests
import pprint
import pandas as pd
import sqlalchemy as db

response = requests.get(f"https://api.github.com/users")
characters_data = response.json()

df = pd.DataFrame(characters_data)
engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    r = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
    print(pd.DataFrame(r))
