import sqlite3 
from schedule import Schedule

conn = sqlite3.connect("schedule.db") 

c = conn.cursor()


def newschedule(time, name, what_it_will_print):
    newschedule = Schedule(time, name, what_it_will_print)

def printall():
    c.execute("SELECT * FROM schedule")
    print(c.fetchall())
    conn.commit()

# def deleteschedule(row):
#     pass

conn.close()