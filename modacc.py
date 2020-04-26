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


def modify():
    flag=True
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        for item in oldlist :
            if item.accno == int(e1.get()) :
                item.name=e2.get()
                item.type=e3.get()
                flag=False
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb') 
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
    if flag:
        call(["python","noaccountfound.py"])
    else:
        call(["python","accountmodify.py    "])
ROOT= Tk()
Label(ROOT,text='Account No').grid(row=0)
Label(ROOT,text='Name : ').grid(row=1)
Label(ROOT,text='Account Type [C/S} :').grid(row=2)
e1=Entry(ROOT)
e2=Entry(ROOT)
e3=Entry(ROOT)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
Button(ROOT,text = 'Modify',width=20,command = modify).grid(row=3)
Button(ROOT,text = 'Exit' ,width=20,command = ROOT.destroy).grid(row=3,column=1)


ROOT.mainloop()