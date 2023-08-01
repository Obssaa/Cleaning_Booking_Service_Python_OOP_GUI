import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from User_info import User



class logintodb:

    def __init__(self, user = User()):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Login Page")
        self.root.resizable(0, 0)
        uname = ""
        self.wn_user = user

        # Defining the first row
        self.username_lable = tk.Label(self.root, text="Username -", font='sans 16 bold', bg = "#3B3C46", fg = "white")
        self.username_lable.place(x=100, y=200, width = 110)

        self.username = tk.Entry(self.root, width=35, bd = 0)
        self.username.place(x=220, y=203, width=300)

        self.password_lable = tk.Label(self.root, text="Password -", font='sans 16 bold', bg = "#3B3C46", fg = "white")
        self.password_lable.place(x=100, y=250, width = 110)

        self.password = tk.Entry(self.root, width=35, bd= 0)
        self.password.place(x=220, y=253, width=300)

        self.submitbtn = tk.Button(self.root, text="Login", font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.gotohomepage)
        self.submitbtn.place(x=210, y=350, width=80, height = 30)

        self.singupbtn = tk.Button(self.root, text="Sign Up", font='sans 16 bold',
                              highlightbackground='black', highlightthickness=0, fg="white", command = self.gotosignuppage)
        self.singupbtn.place(x=410, y=350, width=80, height = 30)

        self.root.mainloop()

    def gotosignuppage(self):
        self.root2 = Toplevel(self.root)
        self.wn_singup = SignUp(self.root2, self.root)
        self.root.withdraw()

    def gotohomepage(self):
        if self.username.get() and self.password.get():
            if self.paswordcheck():
                self.wn_user.login(self.username.get(), self.password.get())
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                messagebox.showerror("Welcom", f"Welcome Home {self.logininfo['username']}")
                self.root2 = Toplevel(self.root)
                global uname
                uname = f"{self.logininfo['username']}"
                self.wn_homepage = Homepage(self.root2, self.root, self.wn_user)
                self.root.withdraw()
            else:
                messagebox.showerror("Error", "Login Information Is Incorrect")

        else:
             messagebox.showerror("Error", "Please fill the login info")
    def paswordcheck(self):
        with open("webuser.txt", 'r') as openfile:
            self.loginintro = openfile.readlines()
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo['username'] == str(self.username.get()) and self.logininfo["userpassword"] == str(
                    self.password.get()):
                    return True
                    break
            else:
                return False


class SignUp:

    def __init__(self, parent, log = logintodb, user = User()):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Sign Up Page")
        self.root.resizable(0,0)
        self.wn_login = log
        self.webuser = user

        self.lable = tk.Label(self.root, text=" Sign Up For HCS", font='time 22 bold italic', bg="#3B3C46", fg="white")
        self.lable.place(x=70, y=50, width=450, height = 65)

        self.fname_lable = tk.Label(self.root, text="Full Name:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.fname_lable.place(x=80, y=150, width=110, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height = 30)

        self.uname_lable = tk.Label(self.root, text="Username:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.uname_lable.place(x=80, y=200, width=110, height = 30)

        self.uname = tk.Entry(self.root, width=35, bd=0)
        self.uname.place(x=200, y=200, width=300, height = 30)

        self.pass_lable = tk.Label(self.root, text="Password:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.pass_lable.place(x=80, y=250, width=110, height = 30)

        self.passw = tk.Entry(self.root, width=35, bd=0)
        self.passw.place(x=200, y=250, width=300, height = 30)

        self.cpass_lable = tk.Label(self.root, text="Confirm Password:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.cpass_lable.place(x=80, y=300, width=110, height = 30)

        self.cpassw = tk.Entry(self.root, width=35, bd=0)
        self.cpassw.place(x=200, y=300, width=300, height = 30)

        self.addi_lable = tk.Label(self.root, text="Address:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.addi_lable.place(x=80, y=350, width=110, height=30)

        self.addi = tk.Entry(self.root, width=35, bd=0)
        self.addi.place(x=200, y=350, width=300, height=30)

        self.number_lable = tk.Label(self.root, text="Number:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.number_lable.place(x=80, y=400, width=110, height=30)

        self.number = tk.Entry(self.root, width=35, bd=0)
        self.number.place(x=200, y=400, width=300, height=30)


        self.donebtn = tk.Button(self.root, text="Done", font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.signupdone)

        self.donebtn.place(x=285, y=480, width=90, height = 40)

    def unamexist(self):
        with open("webuser.txt") as user:
            self.userdict = user.readlines()
            for i in self.userdict:
                self.finduser = eval(i)
                if self.finduser['username'] == self.uname.get() and self.webuser.getUserName() != self.uname.get():
                    return True

    def signupdone(self):
        if self.fname.get() and self.uname.get() and self.addi.get() and self.number.get() and self.passw.get():
            if self.passw.get() != self.cpassw.get():
                messagebox.showerror("Missing Mandatories", "Password should be similar")

            else:
                if self.unamexist():
                    messagebox.showerror("Username Exist", "Username already exist, Please try another")
                else:
                    self.webuser.registerrecods(self.fname.get(), self.uname.get(), self.passw.get(), self.addi.get(),
                                            self.number.get(), "R")
                    messagebox.showerror("Welcome message", "Welcome To HCM \n Keep Your Home Mint Fresh")
                    self.wn_login.deiconify()
                    self.root.destroy()
        else:
            messagebox.showerror("Missing Mandatories", "All Field should be filled")

class Homepage:

    def __init__(self, parent, log = logintodb, user = User):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='silver')
        self.root.title("HCS Home Page")
        self.root.resizable(0, 0)
        self.wn_login = log
        self.wn_cart = Cart
        self.wn_user = user

        self.homelable = tk.Label(self.root, text=f"Welcome @{uname} ", font='time 22 bold', bg="#3B3C46", fg="white")
        self.homelable.place(x=70, y=50, width=449, height=65)

        self.infobtn = tk.Button(self.root, text="Profile", font='sans 16 bold',
                                 highlightbackground='black', highlightthickness=0, fg="white", command = self.gotoprofile)
        self.infobtn.place(x=70, y=115, width=89.8, height=40)

        self.topbtn = tk.Button(self.root, text="Top Up", font='sans 16 bold',
                                highlightbackground='black', highlightthickness=0, fg="white", command = self.gototopup)
        self.topbtn.place(x=159.8, y=115, width=89.8, height=40)

        self.cartbtn = tk.Button(self.root, text="Cart", font='sans 16 bold',
                                 highlightbackground='black', highlightthickness=0, fg="white", command = self.gototocart)
        self.cartbtn.place(x=249.6, y=115, width=89.8, height=40)

        self.logbtn = tk.Button(self.root, text="Log Out", font='sans 16 bold',
                                highlightbackground='black', highlightthickness=0, fg="white", command = self.logout)
        self.logbtn.place(x=339.4, y=115, width=89.8, height=40)

        self.privilagebtn = tk.Button(self.root, text="View", font='sans 16 bold', state = self.btnstate(),
                                highlightbackground='black', highlightthickness=0, fg="white", command=self.gotoview)
        self.privilagebtn.place(x=429.2, y=115, width=89.8, height=40)

        self.servicelable = tk.Label(self.root, text="Services", font='time 18 bold', bg="#6284A7", fg="white")
        self.servicelable.place(x=70, y=200, width=112.5, height=40)

        self.pricelable = tk.Label(self.root, text="Prices", font='time 18 bold', bg="#6284A7", fg="white")
        self.pricelable.place(x=405.5, y=200, width=112.5, height=40)

        # services
        self.var1 = tk.IntVar()
        self.service_1 = tk.Checkbutton(self.root, text="Regular Cleaning", variable = self.var1, font='time 16 bold',
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_1.place(x=70, y=260, height=40)

        self.var2 = tk.IntVar()
        self.service_2 = tk.Checkbutton(self.root, text="Deep Cleaning", font='time 16 bold', variable = self.var2,
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_2.place(x=70, y=290, height=40)

        self.var3 = tk.IntVar()
        self.service_3 = tk.Checkbutton(self.root, text="Weekly Cleaning", font='time 16 bold', variable = self.var3,
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_3.place(x=70, y=320, height=40)

        self.var4 = tk.IntVar()
        self.service_4 = tk.Checkbutton(self.root, text="Steam Cleaning", font='time 16 bold', variable = self.var4,
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_4.place(x=70, y=350, height=40)

        self.var5 = tk.IntVar()
        self.service_5 = tk.Checkbutton(self.root, text="Sanitization", font='time 16 bold', variable = self.var5,
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_5.place(x=70, y=380, height=40)

        self.var6 = tk.IntVar()
        self.service_6 = tk.Checkbutton(self.root, text="Vacuuming", font='time 16 bold', onvalue = 1, variable = self.var6,
                                offvalue = 0, bg="silver", fg="#055252")
        self.service_6.place(x=70, y=410, height=40)

        self.var7 = tk.IntVar()
        self.service_7 = tk.Checkbutton(self.root, text="Monthly Cleaning", font='time 16 bold', variable = self.var7,
                                        onvalue=1,
                                        offvalue=0, bg="silver", fg="#055252")
        self.service_7.place(x=70, y=440, height=40)

        # prices

        self.price_1 = tk.Label(self.root, text="200 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_1.place(x=405.5, y=260, height=40)

        self.price_2 = tk.Label(self.root, text="300 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_2.place(x=405.5, y=290, height=40)

        self.price_3 = tk.Label(self.root, text="450 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_3.place(x=405.5, y=320, height=40)

        self.price_4 = tk.Label(self.root, text="250 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_4.place(x=405.5, y=350, height=40)

        self.price_5 = tk.Label(self.root, text="150 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_5.place(x=405.5, y=380, height=40)

        self.price_6 = tk.Label(self.root, text="70 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_6.place(x=405.5, y=410, height=40)

        self.price_7 = tk.Label(self.root, text="100 AED", font='time 16 bold', bg="silver", fg="#055252")
        self.price_7.place(x=405.5, y=440, height=40)

        self.cartbtn = tk.Button(self.root, text="Add to Cart", font='sans 16 bold',
                                 highlightbackground='black', highlightthickness=0, fg="white", command = self.cart)
        self.cartbtn.place(x=220, y=490, width=150.5, height=40)

        self.exitlable = tk.Label(self.root, text="Keep Your House Mint Fresh", font='time 12 bold italic',
                                  bg="#3B3C46", fg="white")
        self.exitlable.place(x=70, y=560, width=449, height=40)

    def logout(self):
        self.wn_login.deiconify()
        self.root.destroy()
    def gotoprofile(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = Profile(self.root2, self.root, self.wn_user)
        self.root.withdraw()
    def gototopup(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = Topup(self.root2, self.root)
        self.root.withdraw()


    def gototocart(self):
        true = self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 \
        and self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 0
        if true:
            messagebox.showerror("Add To Cart", 'Your cart is empty')
        else:
            self.root2 = Toplevel(self.root)
            self.wn_cart = Cart(self.root2, self.root)
            self.root.withdraw()
    def gotoview(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = View(self.root2, self.root)
        self.root.withdraw()

    def btnstate(self):
        if self.wn_user.manger() or self.wn_user.employee():
            return 'normal'
        elif self.wn_user.regular():
            return 'disabled'


    def cart(self):
        true = self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 \
               and self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 0
        if true:
            messagebox.showerror("Add To Cart", 'You need to add services')
        else:
            cartdict = {}
            if self.var1.get(): cartdict["Regular"] = 200
            if self.var2.get(): cartdict["Deep"] = 300
            if self.var3.get(): cartdict["Weekly"] = 450
            if self.var4.get(): cartdict["Steam"] = 250
            if self.var5.get(): cartdict["Sanitation"] = 150
            if self.var6.get(): cartdict["Vacuuming"] = 70
            if self.var7.get(): cartdict["Monthly"] = 100
            messagebox.showerror("Go to payment", "To retrive your services\nYou need to go to your cart")
            global service_list
            service_list = cartdict

class Profile:

    def __init__(self, parent, wn_home = Homepage, user = User()):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Profile Page")
        self.root.resizable(0,0)
        self.wn_home = wn_home
        self.wn_user = user
        self.wn_user.updatingtobalance()
        self.wn_user.updatepoints1()





        self.lable = tk.Label(self.root, text=f"Hello {uname}", font='time 22 bold italic', bg=f"{self.color()}", fg="white")
        self.lable.place(x=70, y=50, width=450, height = 65)

        self.fname_lable = tk.Label(self.root, text="Full Name:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.fname_lable.place(x=80, y=150, width=110, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height = 30)
        self.fname.insert(0, self.wn_user.getFullname())

        self.uname_lable = tk.Label(self.root, text="Username:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.uname_lable.place(x=80, y=200, width=110, height = 30)

        self.uname = tk.Entry(self.root, width=35, bd=0)
        self.uname.place(x=200, y=200, width=300, height = 30)
        self.uname.insert(0, f"{self.wn_user.getUserName()}")

        self.pass_lable = tk.Label(self.root, text="Password:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.pass_lable.place(x=80, y=250, width=110, height = 30)

        self.passw = tk.Entry(self.root, width=35, bd=0)
        self.passw.place(x=200, y=250, width=300, height = 30)
        self.passw.insert(0, self.wn_user.getPassword())

        self.cpass_lable = tk.Label(self.root, text="Confirm Password:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.cpass_lable.place(x=80, y=300, width=110, height = 30)

        self.cpassw = tk.Entry(self.root, width=35, bd=0)
        self.cpassw.place(x=200, y=300, width=300, height = 30)

        self.addi_lable = tk.Label(self.root, text="Address:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.addi_lable.place(x=80, y=350, width=110, height=30)

        self.addi = tk.Entry(self.root, width=35, bd=0)
        self.addi.place(x=200, y=350, width=300, height=30)
        self.addi.insert(0, self.wn_user.getaddress())

        self.number_lable = tk.Label(self.root, text="Number:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.number_lable.place(x=80, y=400, width=110, height=30)

        self.number = tk.Entry(self.root, width=35, bd=0)
        self.number.place(x=200, y=400, width=300, height=30)
        self.number.insert(0, self.wn_user.getPhoneNum())

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.balance_lable.place(x=80, y=450, width=110, height=30)

        self.balance = tk.Label(self.root, text= self.wn_user.getbalance(), width=35, bd=0, bg = "silver")
        self.balance.place(x=200, y=450, width=300, height=30)

        self.points_lable = tk.Label(self.root, text="Points:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.points_lable.place(x=80, y=500, width=110, height=30)

        self.points = tk.Label(self.root, text= self.wn_user.getpoints(), width=35, bd=0, bg="silver")
        self.points.place(x=200, y=500, width=300, height=30)


        self.backbtn = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.goback)

        self.backbtn.place(x=70, y=550, width=90, height = 40)

        self.updatebtn = tk.Button(self.root, text="Update", font='sans 16 bold',
                                 highlightbackground='black', highlightthickness=0, fg="white", command = self.update)

        self.updatebtn.place(x=430, y=550, width=90, height=40)

    def unamexist(self):
        with open("webuser.txt") as user:
            self.userdict = user.readlines()
            for i in self.userdict:
                self.finduser = eval(i)
                if self.finduser['username'] == self.uname.get() and self.wn_user.getUserName() != self.uname.get():
                    return True

    def update(self):
        if self.fname.get() and self.uname.get() and self.addi.get() and self.number.get() and self.passw.get():
            if self.passw.get() != self.cpassw.get():
                messagebox.showerror("Confirm password", "Password should be similar")
            else:
                if self.unamexist():
                    messagebox.showerror("Username Exist", "Username already exist, Please try another")
                else:
                    self.wn_user.updateinfo(self.fname.get(), self.uname.get(), self.passw.get(), self.addi.get(),
                                            self.number.get())
                    messagebox.showerror("Update", "Successfully Updated")
                    self.goback()
        else:
            messagebox.showerror("Fill Field", "All fields must be full")

    def color(self):
        if self.wn_user.golden():
            return "#FFD700"
        elif self.wn_user.silver():
            return "#808080"
        else:
            return '#3B3C46'

    def goback(self):
        self.wn_home.deiconify()
        self.root.withdraw()




class Topup:

    def __init__(self, parent, home = Homepage,):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Top Up Page")
        self.root.resizable(0,0)
        self.wn_home = home
        self.user = User()
        self.user.updatingtobalance()

        self.lable = tk.Label(self.root, text="Top up from card", font='time 22 bold italic', bg="#3B3C46", fg="white")
        self.lable.place(x=70, y=50, width=450, height = 65)

        self.fname_lable = tk.Label(self.root, text="Name on card:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.fname_lable.place(x=80, y=150, width=110, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height = 30)

        self.cardnum_lable = tk.Label(self.root, text="Card Number:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.cardnum_lable.place(x=80, y=200, width=110, height = 30)

        self.cardnum = tk.Entry(self.root, width=35, bd=0)
        self.cardnum.place(x=200, y=200, width=300, height = 30)

        self.edate_lable = tk.Label(self.root, text="Exp Date:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.edate_lable.place(x=80, y=250, width=110, height = 30)

        self.edate = tk.Entry(self.root, width=35, bd=0)
        self.edate.place(x=200, y=250, width=300, height = 30)

        self.cvv_lable = tk.Label(self.root, text="CVV:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.cvv_lable.place(x=80, y=300, width=110, height = 30)

        self.cvv = tk.Entry(self.root, width=35, bd=0)
        self.cvv.place(x=200, y=300, width=300, height = 30)

        self.amount_lable = tk.Label(self.root, text="Amount:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.amount_lable.place(x=80, y=350, width=110, height=30)

        self.amount = tk.Entry(self.root, width=35, bd=0)
        self.amount.place(x=200, y=350, width=300, height=30)

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.balance_lable.place(x=80, y=400, width=110, height=30)

        self.balance = tk.Label(self.root, text= self.user.getbalance(), width=35, bd=0, bg="silver")
        self.balance.place(x=200, y=400, width=300, height=30)

        self.backbtn = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.donetopup)

        self.backbtn.place(x=80, y=480, width=90, height = 40)

        self.topupbtn = tk.Button(self.root, text="Done", font='sans 16 bold',
                                  highlightbackground='black', highlightthickness=0, fg="white", command=self.topup)

        self.topupbtn.place(x=420, y=480, width=90, height=40)


    def donetopup(self):

        self.wn_home.deiconify()
        self.root.destroy()

    def topup(self):

        if self.fname.get() and self.cardnum.get() and self.edate.get() and self.cvv.get() and self.amount.get():
            try:
                amount = float(self.amount.get())
                if amount >= 100:
                    self.user.topupmoney(amount)
                    messagebox.showerror("congratulations", f"You have Topup:  AED {amount}")
                    self.wn_home.deiconify()
                    self.root.withdraw()
                else:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Minimum Amount", "You should top up more or equal to a AED 100")
        else:
            messagebox.showerror("Missing Fields", "All fields must be field")

class Cart:

    def __init__(self, parent, home = Homepage, top = Topup):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Top Up Page")
        self.root.resizable(0,0)
        self.wn_home = home
        self.user = User()
        self.carttopup = top
        self.user.updatingtobalance()

        self.lable = tk.Label(self.root, text="Here is Your Cart", font='time 22 bold italic', bg="#3B3C46", fg="white")
        self.lable.place(x=70, y=50, width=450, height = 65)

        self.order_lable = tk.Label(self.root, text="Your Order:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.order_lable.place(x=80, y=150, width=110, height = 30)

        self.order = tk.Label(self.root, text = service_list, font='sans 10 bold', bg="white", fg="#3B3C46")
        self.order.place(x=200, y=150, width=300, height = 30)

        self.price_lable = tk.Label(self.root, text="Total Price:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.price_lable.place(x=80, y=200, width=110, height=30)


        self.price = tk.Label(self.root, text=f"AED {self.totalprice()}", font='sans 10 bold', bg="white", fg="#3B3C46")
        self.price.place(x=200, y=200, width=300, height=30)

        self.rate_lable = tk.Label(self.root, text="Discount Rate:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.rate_lable.place(x=80, y=250, width=110, height=30)

        self.rate = tk.Label(self.root, text=f"{self.user.rate()}%", font='sans 10 bold', bg="white", fg="#3B3C46")
        self.rate.place(x=200, y=250, width=300, height=30)

        self.Discounted_lable = tk.Label(self.root, text="Discount Price:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.Discounted_lable.place(x=80, y=300, width=110, height=30)

        self.Discounted = tk.Label(self.root, text=f"AED {self.user.discount(self.totalprice())}", font='sans 10 bold', bg="white", fg="#3B3C46")
        self.Discounted.place(x=200, y=300, width=300, height=30)

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 10 bold', bg="#3B3C46", fg="white")
        self.balance_lable.place(x=80, y=350, width=110, height=30)

        self.balance = tk.Label(self.root, text= self.user.getbalance(), width=35, bd=0, bg="silver")
        self.balance.place(x=200, y=350, width=300, height=30)

        self.back = tk.Button(self.root, text = "Back",font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.goback)
        self.back.place(x=70, y=450, width=90, height=40)


        self.paybtn = tk.Button(self.root, text="Pay", font='sans 16 bold',
                              highlightbackground='black', highlightthickness = 0, fg = "white", command = self.cartpay)

        self.paybtn.place(x=430, y=450, width=90, height = 40)

    def goback(self):
        self.wn_home.deiconify()
        self.root.withdraw()

    def totalprice(self):
        sum = 0
        for i in service_list.values():
            sum = sum + i
        return sum

    def cartpay(self):

        if self.user.balancecheck(self.totalprice()):
            messagebox.showerror("Paying System", "Your Payment Was Successful")
            self.user.servicedetail(service_list, self.totalprice())
            self.user.updatepoints(self.totalprice())
            self.wn_home.deiconify()
            self.root.destroy()
        else:
            messagebox.showerror("Paying System", "Your Payment Was not Successful\n "
                                                  "You Need To Top Up")


class View:

    def __init__(self, parent, home = Homepage):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= 'silver')
        self.root.title("HCS Top Up Page")
        self.root.resizable(0,0)
        self.wn_home = home
        self.user= User()

        self.lable = tk.Label(self.root, text="All The Users Info", font='time 22 bold italic', bg="#3B3C46", fg="white")
        self.lable.place(x=70, y=50, width=450, height=65)

        self.txtbox = tk.Text(self.root, font='time 12 bold italic')
        self.txtbox.place(x=70, y=150, width=450, height=320)
        self.txtbox.insert(tk.END, self.viewallaccounts())

        self.back = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='black', highlightthickness=0, fg="white", command = self.goback)
        self.back.place(x=60, y=490, width=190, height=40)
        self.delete = tk.Button(self.root, text="Delete all Accounts", font='sans 16 bold', state = 'normal',
                              highlightbackground='black', highlightthickness=0, fg="white", command = self.deleteall)
        self.delete.place(x=340, y=490, width=190, height=40)

        self.root.mainloop()

    def viewallaccounts(self):
        return self.user.list()

    def deleteall(self):
        self.deleteme()

    def deleteme(self):
        result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if result == 'yes':
            self.user.deleteaccounts()
            self.goback()
        else:
            return


    def goback(self):
        self.wn_home.deiconify()
        self.root.destroy()

    def state(self):
        if self.user.manger():
            return "normal"
        if self.user.employee():
            return 'disabled'


gui = logintodb()





