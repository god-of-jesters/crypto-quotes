import datetime
import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect('cripto')
cursor = con.cursor()

def day():
    i = 1
    t,l = [],[]
    dt = datetime.datetime.now()
    dat = f"{dt.day}.{dt.month}.{dt.year}"
    cursor.execute('Select dat from crip3;')
    q = list(cursor.fetchall())
    cursor.execute('Select curs from crip3;')
    c = list(cursor.fetchall())
    cursor.execute('Select time from crip3;')
    t2 = list(cursor.fetchall())
    while q[-i] != f"{dt.day - 1}.{dt.month}.{dt.year}" and len(q) - 1 >= i:
        i += 1
        t.append(t2[-i][0])
        l.append(c[-i][0])
    plt.plot(t[0:-1], l[0:-1])
    plt.show()

def week():
    pass