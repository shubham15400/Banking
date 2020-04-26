from tkinter import *

ROOT = Tk()
Label(ROOT,text = 'Account Modified.').grid(row=0)
Button(ROOT,text = 'Exit' ,width=10,command = ROOT.destroy ).grid(row=1)
ROOT.mainloop()