from tkinter import *
from time_spans import *
window = Tk()
window.geometry('400x600')

But1 = Button(window,text = 'День',command = day)
But2 = Button(window,text = 'Неделя',command = week)
But3 = Button(window,text = 'Месяц',command = month)
But1.place(x = 0,y=0, anchor = 'nw',width = 400,height = 200)
But2.place(x = 0,y=200, anchor = 'nw',width = 400,height = 200)
But3.place(x = 0,y=400, anchor = 'nw',width = 400,height = 200)

window.mainloop()
