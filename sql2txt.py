import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')
query = "SELECT question_text, answer FROM questions_question"
df = pd.read_sql_query(query, conn)
conn.close()
df.to_csv('data/questions_question.txt', sep='\t', index=False)

