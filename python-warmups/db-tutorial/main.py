import sqlite3
con = sqlite3.connect("tutorial.db")

def create_table():
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")

def insert_data(data):
    cur = con.cursor()
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()
    
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

insert_data(data)