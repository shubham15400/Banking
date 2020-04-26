import pickle
import os
import pathlib


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

        
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        while(searchAccount(self.accNo)):
            print("Account already exists")
            self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")

        while(self.type!='C' and self.type!='S' and self.type!='c' and self.type!='s'):
            print("Enter C or S only")
            self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount (>=500 for Saving and >=1000 for current) :"))
        while((self.type=='C' or self.type =='c') and self.deposit<1000):
            print("Enter sufficient initial amount")
            self.deposit=int(input("Enter Amount"))
        while((self.type=='S' and self.type=='s') and deposit<500):
            print("Enter sufficient initial amount")
            self.deposit=int(input("Enter Amount"))
        print("\n\n\nAccount Created")
    
    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    input("Enter any botton to continue")


def searchAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        fdata = open('accounts.data','rb')
        data = pickle.load(fdata)
        for i in data:
            if(i.accNo==num):
                return True
    else:
        return False


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your account Balance is = ", item.deposit)
                found = True
    else:
        print("No records to Search")
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2:
                    flag = True
                    while (flag):
                        amount = int(input("Enter the amount to withdraw : "))
                        if amount < item.deposit:
                            if item.type == 'S' or item.type == 's':
                                if (item.deposit - amount >= 500):
                                    item.deposit -= amount
                                    flag = False
                            elif item.type == 'C' or item.type == 'c':
                                if (item.deposit - amount >= 1000):
                                    item.deposit -= amount
                                    flag = False
                        if flag:
                            print("You cannot withdraw larger amount")
                            ch = ''
                            ch = input('Want to withdraw(y/n)? :')
                            if ch == 'N' or ch == 'n':
                                flag = False
                    print("Amount Withdrawn")
    else:
        print("No records to Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

if __name__=="__main__":
    ch = ''
    num = 0
    intro()

    while ch != 8:
        # system("cls");
        print("\tMAIN MENU")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. ALL ACCOUNT HOLDER LIST")
        print("\t6. CLOSE AN ACCOUNT")
        print("\t7. MODIFY AN ACCOUNT")
        print("\t8. EXIT")
        print("\tSelect Your Option (1-8) ")
        ch = input("Enter your choice(1-8) : ")
        # system("cls");

        if ch == '1':
            writeAccount()
        elif ch == '2':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 1)
        elif ch == '3':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 2)
        elif ch == '4':
            num = int(input("\tEnter The account No. : "))
            displaySp(num)
        elif ch == '5':
            displayAll()
        elif ch == '6':
            num = int(input("\tEnter The account No. : "))
            deleteAccount(num)
        elif ch == '7':
            num = int(input("\tEnter The account No. : "))
            modifyAccount(num)
        elif ch == '8':
            print("\tThanks for using bank managemnt system")
            break
        else:
            print("Invalid choice")