from tkinter import Tk
from tkinter import mainloop
from tkinter import Label
from tkinter import Button

window = Tk()
Label(window,text='Hello',font=28,foreground='white',background='blue').pack()
Label(window,text='Welcome to this application',font=28,foreground='white',background='blue').pack()
window.resizable(height=False,width=False)
def go_to_activity():
    print('hello')

btn = Button(window)
btn.configure(text='go to original activity',background='red',foreground='white',command=go_to_activity)
btn.pack()
window.minsize(500,500)
window.mainloop()