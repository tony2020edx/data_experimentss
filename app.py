import pandas as pd
import sqlite3

data_path = "/Users/tony/Desktop/datarepo/generativeAI/generativeai.csv"  #the path to the csv file
df = pd.read_csv(data_path)


#write the data to a sqlite database file

conn = sqlite3.connect('generativeai.db')
cursor = conn.cursor()

df.to_sql('generativeai_indeed', conn, if_exists='replace', index=False)
conn.close()