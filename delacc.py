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


def delete():
    flag=True
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accno != int(e1.get()) :
                newlist.append(item)
            else:
                flag=False
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
    if flag:
        call(["python","noaccountfound.py"])
    else:
        call(["python","accountdeleted.py"])
        ROOT.destroy()
ROOT= Tk()
Label(ROOT,text='Account No').grid(row=0)e1=Entry(ROOT)
e1.grid(row=0,column=1)
Button(ROOT,text = 'Delete',width=20,command = delete).grid(row=2)
Button(ROOT,text = 'Exit' ,width=20,command = ROOT.destroy).grid(row=2,column=1)


ROOT.mainloop()
