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


def wdraw():
    flag=False
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accno == int(e1.get()) :
                flag = True
                amount = int(e2.get())
                if amount < item.amt:
                    if item.type == 'S' or item.type == 's':
                        if (item.amt - amount >= 500):
                            item.amt -= amount
                            flag = False
                    elif item.type == 'C' or item.type == 'c':
                        if (item.amt - amount >= 1000):
                            item.amt -= amount
                            flag = False
                if flag:
                    call(["python","cannotwithdraw.py"])
    else :
        call(["python","newaccountfound.py"])
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data'   )
    if not flag:
        call(["python","accountupdate.py"])
        ROOT.destroy()
    
ROOT= Tk()
Label(ROOT,text='Account No').grid(row=0)
Label(ROOT,text = 'Amount').grid(row=1)
e1=Entry(ROOT)
e1.grid(row=0,column=1)
e2=Entry(ROOT)
e2.grid(row=1,column=1)
Button(ROOT,text = 'Withdraw',width=20,command = wdraw).grid(row=2)
Button(ROOT,text = 'Exit' ,width=20,command = ROOT.destroy).grid(row=2,column=1)


ROOT.mainloop()