from tkinter import *
from subprocess import call

def new_account():
    call(["python", "newaccount.py"])

def Deposit():
    call(["python","deposit.py"])

def Withdraw():
    call(["python","withdraw.py"])

def Checkbal():
    call(["python","checkbal.py"])

def Deleteacc():
    call(["python","delacc.py"])

def modaccount():
    call(["python","modacc.py"])

ROOT = Tk()
SIZE = "340x400"
WIDTH = 20
CENTER_X = 100
CENTER_Y = 30
ROOT.geometry(SIZE)
btn1 = Button(ROOT,text = 'New Account',command = new_account,width=WIDTH)
btn2 = Button(ROOT,text='Deposit',command=Deposit,width=WIDTH)
btn3 = Button(ROOT,text='Withdraw',command = Withdraw,width=WIDTH)
btn4 = Button(ROOT,text='Check Balance',command = Checkbal,width=WIDTH)
btn5 = Button(ROOT,text='Delete Account',command = Deleteacc,width=WIDTH)
btn6 = Button(ROOT,text='Modify Account',command = modaccount,width=WIDTH)
btn8 = Button(ROOT,text='Exit',command = ROOT.destroy,width=WIDTH)

btn1.place(x=CENTER_X,y=CENTER_Y*1)
btn2.place(x=CENTER_X,y=CENTER_Y*2)
btn3.place(x=CENTER_X,y=CENTER_Y*3)
btn4.place(x=CENTER_X,y=CENTER_Y*4)
btn5.place(x=CENTER_X,y=CENTER_Y*5)
btn6.place(x=CENTER_X,y=CENTER_Y*6)
btn8.place(x=CENTER_X,y=CENTER_Y*8)

ROOT.mainloop()