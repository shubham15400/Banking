from tkinter import *
import pathlib
import os
import pickle
from subprocess import call
class Account:
    def __init__(self,no,name,typ,amt):
        self.accno=no
        self.name=name
        self.type=typ
        self.amt=amt

def searchAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        fdata = open('accounts.data','rb')
        data = pickle.load(fdata)
        for i in data:
            if(i.accno==num):
                return True
    else:
        return False

def writeAccount():
    AccNo=int(e1.get())
    Name = e2.get()
    AccType = e3.get()
    print(AccType)
    Amt = int(e4.get())
    flag = True
    if(searchAccount(AccNo)):
        flag = False
    if(AccType!='C' and AccType!='S' and AccType!='c' and AccType!='s'):
        falg = False
    if((AccType=='C' or AccType=='c') and Amt<1000):
        flag = False
    if((AccType=='S' or AccType=='s') and Amt<500):
        flag = False
    
    if(flag):
        a =Account(AccNo,Name,AccType,Amt)
        file = pathlib.Path("accounts.data")
        if file.exists():   
            infile = open('accounts.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(a)
            infile.close()
            os.remove('accounts.data')
        else:
            oldlist = [a]
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        call(["python","S.py"])
        master.destroy()
    else:
        call(["python","f.py"])


master = Tk() 
var = IntVar()
Label(master, text='Account No').grid(row=0) 
Label(master, text='Account Holder Name').grid(row=1)
Label(master, text='Account Type [C/S]').grid(row=2)
Label(master, text='Initial Amount').grid(row=3)
e1 = Entry(master) 
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
b = Button(master,text = 'Submit',width=20,command = writeAccount)
b1 = Button(master,text = 'Exit' ,width=20,command = master.destroy )
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1)
b.grid(row=4,column=0)
b1.grid(row=4,column=1)
mainloop()