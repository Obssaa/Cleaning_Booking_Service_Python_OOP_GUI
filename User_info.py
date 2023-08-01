from tkinter import messagebox
import random
import fileinput
class User:
    """class to represent the user"""

    # constructor

    def __init__(self, uname ="ferid", fname ="", password ="", address ="", pnumber = "", acctype = "R", balance = 0, points = 0):
        self.user_name = uname
        self.full_name = fname
        self.password = password
        self.address = address
        self.phone_number = pnumber
        self.account_type = acctype
        self.balance = balance
        self.points = points
        self.purchases = []
        self.usercode = ''

    def setUserName(self, userName):
        self.user_name = userName

    def getUserName(self):
        return self.user_name

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setFullname(self, fullname):
        self.full_name = fullname

    def getFullname(self):
        return self.full_name

    def setAddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setPhoneNum(self, phone):
        self.phone_number = phone

    def getPhoneNum(self):
        return self.phone_number

    def setAccountType(self, accountType):
        self.account_type = accountType

    def getAccountType(self):
        return self.account_type
    def setbalance(self, bal):
        self.balance = bal
    def getbalance(self):
        return self.balance

    def setpoints(self, points):
        self.points = points
    def getpoints(self):
        return self.points

    def setPurchasedService(self, ser):
        self.purchasedSerivces = ser

    def getPurchasedService(self):
        return self.purchasedSerivces


    def registerrecods(self, fname , uname, password, addi, pnumber, acctype):
        self.setFullname(fname)
        self.setUserName(uname)
        self.setPassword(password)
        self.setAddress(addi)
        self.setPhoneNum(pnumber)
        self.setAccountType(acctype)
        self.usercode = f"{self.getUserName()[0:3]}{random.randint(1000000000, 9999999999)}"

        self.userrecord = {
            'code': self.usercode,
            'fname': self.getFullname(),
            'uname': self.getUserName(),
            'passw': self.getPassword(),
            'addi':  self.getaddress(),
            'pnum': self.getPhoneNum(),
            'balance': self.getbalance(),
            "points": 0,
            'acctype': self.getAccountType()
        }

        with open("webuser.txt", 'a') as user:
            self.webuser = {
                "usercode": self.userrecord['code'],
                "username": self.userrecord["uname"],
                "userpassword": self.userrecord['passw']
            }
            user.write('\n')
            user.write(str(self.webuser))


        with open("Records.txt", "a") as allrecords:
            allrecords.write('\n')
            allrecords.write(str(self.userrecord))

    def login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        with open("webuser.txt", 'r') as openfile:
            self.loginintro = openfile.readlines()
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo['username'] == str(self.getUserName()) and self.logininfo["userpassword"] == \
                        str(self.getPassword()):
                    self.usercode = self.logininfo['usercode']
                    global usercode
                    usercode = self.usercode

        with open('Records.txt', 'r') as fileopen:
            readfile = fileopen.readlines()
            for i in readfile:
                readline = eval(i)
                if readline["code"] == self.usercode:
                    self.setFullname(readline['fname'])
                    self.setUserName(readline['uname'])
                    self.setPassword(readline['passw'])
                    self.setAddress(readline['addi'])
                    self.setPhoneNum(readline['pnum'])
                    self.setAccountType(readline['acctype'])

    def updateinfo(self, name, uname, passw, addi, num):
        file = open('Records.txt', 'r+')
        readfile = file.readlines()
        for i in readfile:
            readline = eval(i)
            if readline["code"] == self.usercode:
                readline['fname'] = name
                self.setFullname(name)
                readline['uname'] = uname
                self.setUserName(uname)
                readline['passw'] = passw
                self.setPassword(passw)
                readline['addi'] = addi
                self.setAddress(addi)
                readline['pnum'] = num
                self.setPhoneNum(num)
        list1 = {
            'code': self.usercode,
            'fname': self.getFullname(),
            'uname': self.getUserName(),
            'passw': self.getPassword(),
            'addi': self.getaddress(),
            'pnum': self.getPhoneNum(),
            "balance": self.getbalance(),
            "points": self.getpoints(),
            'acctype': self.getAccountType()
        }
        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            global logintro
            logintro = self.loginintro
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo["code"] == self.usercode:
                    self.loginintro[self.loginintro.index(i)] = str(list1)
            with open("Records.txt", 'w') as rewritefile:
                for j in logintro:
                    self.loginintroeval = eval(j)
                    if self.loginintroeval['code'] == self.usercode:
                        rewritefile.write(j)
                        rewritefile.write('\n')
                    else:
                        rewritefile.write(j)
        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            with open("webuser.txt", 'w') as rewritefile:
                for i in self.loginintro:
                    self.userlogin = eval(i)
                    list2 ={
                        "usercode": self.userlogin["code"],
                        "username": self.userlogin["uname"],
                        "userpassword": self.userlogin ["passw"]
                    }
                    rewritefile.write(str(list2))
                    rewritefile.write("\n")


    def topupmoney(self, amount):
        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            global topintro
            topintro = self.loginintro
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo["code"] == usercode:
                    totalbalance = float(self.logininfo['balance']) + amount
                    self.setbalance(totalbalance)
                    self.logininfo["balance"] = self.getbalance()
                    self.loginintro[self.loginintro.index(i)] = self.logininfo
            with open('Records.txt', 'w') as rewrite:
                for j in self.loginintro:
                    self.logininfo = eval(str(j))
                    if self.logininfo["code"] == usercode:
                        rewrite.write(str(j))
                        rewrite.write('\n')
                    else:
                        rewrite.write(str(j))

    def updatingtobalance(self):
        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    self.setbalance(self.logininfo["balance"])

    def updatepoints1(self):
        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    self.setpoints(self.logininfo["points"])


    def balancecheck(self, totalprice):
        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["balance"] >= totalprice:
                        self.setpoints(int(totalprice))
                        return True
                        break

    def discount(self, totalprice):
        if self.manger():
            return totalprice - (totalprice*0.27)
        if self.golden():
            return totalprice - (totalprice*0.25)
        if self.employee():
            return totalprice - (totalprice*0.17)
        if self.silver():
            return totalprice - (totalprice*0.15)
        else:
            return totalprice




    def updatepoints(self, totalprice):

        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo["code"] == usercode:
                    self.setpoints(totalprice)
                    self.logininfo["points"] = self.getpoints()
                    self.loginintro[self.loginintro.index(i)] = self.logininfo
            with open('Records.txt', 'w') as rewrite:
                for j in self.loginintro:
                    self.logininfo = eval(str(j))
                    if self.logininfo["code"] == usercode:
                        rewrite.write(str(j))
                        rewrite.write('\n')
                    else:
                        rewrite.write(str(j))

    def golden(self):

        with open('Records.txt', 'r') as rewrite:
            for j in self.loginintro:
                self.logininfo = eval(str(j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["points"] >= 900:
                        return True
    def silver(self):

        with open('Records.txt', 'r') as rewrite:
            for j in self.loginintro:
                self.logininfo = eval(str(j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["points"] >= 500:
                        return True

    def regular(self):

        with open('Records.txt', 'r') as rewrite:
            for j in self.loginintro:
                self.logininfo = eval(str(j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["points"] < 500 or self.logininfo['acctype'] == "R":
                        return True
    def manger(self):

        with open('Records.txt', 'r') as rewrite:
            self.loginintro = rewrite.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["acctype"] == "M":
                        return True

    def employee(self):

        with open('Records.txt', 'r') as rewrite:
            self.loginintro = rewrite.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["acctype"] == "E":
                        return True
    def rate(self):

        if self.manger():
            return 0.27
        if self.golden():
            return 0.25
        if self.employee():
            return 0.17
        if self.silver():
            return 0.15
        else:
            return 0



    def servicedetail(self, services, price):
        details = {
            "usercode": "",
            "services": services,
            "totalPrice": price
        }

        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    details["usercode"] = usercode
                    with open("Services &Purchase.txt", "a") as appendservice:
                        appendservice.write(str(details))
                        appendservice.write('\n')

    def list(self):

        with open('Records.txt', 'r+') as read:
            list1 = []
            self.loginintro = read.readlines()
            for i in self.loginintro:
                list1.append(i)
                list1.append("\n")
        return (list1)

    def deleteaccounts(self):

        with open('Records.txt', 'w') as read:
            read.write("")

        with open("webuser.txt", 'w') as overwrite:
            overwrite.write("")













class RegularUser (User):

    def __init__(self, uname ="", fname ="", password ="", address ="", pnumber = "", acctype ={}):
        User.__init__(self, uname, fname , password , address , pnumber , acctype)


class Employee (User):

    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        User.__init__(self, uname, fname , password , address , pnumber , acctype)


class RegularEmployee (Employee):

    """class to represent the reqular employees"""

    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        Employee.__init__(self, uname, fname , password , address , pnumber , acctype)
    #functions



class Manager (Employee):

    """class to represent the manager"""
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        Employee.__init__(self, uname, fname , password , address , pnumber , acctype)

    # functions


class PayingSystem:

    """A class to represent the paying system"""

    # constructor

    def __init__(self, cname = "" , cnumber = '', camount = 0):

        self.card_name = cname
        self.card_number = cnumber
        self.card_amount = camount

    def setcname(self, name):
        self.card_name = name
    def getcname(self):
        return self.card_name
    def setcnumber(self, num):
        self.card_number = num
    def getcnumber(self):
        return self.card_number
    def setcamount(self, amount):
        self.card_amount = amount
    def getcamount(self):
        self.card_amount





