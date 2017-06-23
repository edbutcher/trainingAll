import sqlite3
import json

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

with open('data.json') as data_file:
    data = json.load(data_file)
    data = data['data']

for d in data:
    a, b, c = (d['region']), (d['town']), (d['value'])
    cur.execute('INSERT INTO charter_database (region, town, value) VALUES (?, ?, ?)', (a, b, c))
conn.commit()
