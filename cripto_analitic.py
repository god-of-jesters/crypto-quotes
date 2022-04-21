import sqlite3
from tkinter import *
import datetime
import matplotlib.pyplot as plt
window = Tk()
window.geometry('400x600')

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
    while q[-i] != f"{dt.day-1}.{dt.month}.{dt.year}" and len(q)-1 >= i:
        i += 1
        t.append(t2[-i][0])
        l.append(c[-i][0])
    plt.plot(t[0:-1],l[0:-1])
    plt.show()
def week():
    pass
def month():
    pass

But1 = Button(window,text = 'День',command = day)
But2 = Button(window,text = 'Неделя',command = week)
But3 = Button(window,text = 'Месяц',command = month)
But1.place(x = 0,y=0, anchor = 'nw',width = 400,height = 200)
But2.place(x = 0,y=200, anchor = 'nw',width = 400,height = 200)
But3.place(x = 0,y=400, anchor = 'nw',width = 400,height = 200)

con = sqlite3.connect('cripto')
cursor = con.cursor()
window.mainloop()
