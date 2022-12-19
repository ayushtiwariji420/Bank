from csv import DictReader


class User:
    all_user = {}
    all = all_user.keys()
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        User.all_user.update({self.name:self})

    def show_details(self):
        print(f"The users details are \n name : {self.name} \n age : {self.age} \n gender : {self.gender}")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Bank(User):
    def __init__(self, name, age, gender,pin,balance=0):
        super().__init__(name, age, gender)
        self.balance = balance
        self.pin = pin

    def deposit(self,amount=0):
        self.balance = self.balance + amount
        print(f"Amount depostited and your current account balance is {self.balance}")

    def withdraw(self,amount=0):
        if amount>self.balance:
            print(f"sorry but your account balance is {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Amount withdrawn and your current account balance is {self.balance}")


class ATM(Bank):

    def __init__(self, name, age, gender, pin, balance=0):
        super().__init__(name, age, gender, pin, balance)

    @classmethod
    def users_from_list(cls):
        with open('user.csv','r') as f:
            read = DictReader(f)
            users = list(read)

        for user in users:
           user.name = ATM(
               name=user.get('name'),
               age=int(user.get('age')),
               gender=user.get('gender'),
               pin=int(user.get('pin')),
               balance=int(user.get('balance'))
           )
    
    def use_atm(self):
        print("*****************Welcome to The ATM Service Of The Bank***********************")
        p = int(input("enter Your pin : "))
        if p==self.pin:
            opt = 0
            while opt != 5:
                print("please choose the option \n 1. show details \n 2.deposit money \n 3. withdraw money \n 4. show balance \n 5. Exit")
                opt = int(input("Enter the option : "))

                if opt==1:
                    self.show_details()
                elif opt==2:
                    amount = int(input("enter the Amount to deposit: "))
                    self.deposit(amount)
                elif opt==3:
                    amount = int(input("enter the Amount to deposit: "))
                    self.withdraw(amount)
                elif opt==4:
                    print("Your current Balance is : ",self.balance)
                elif opt==5:
                    break
                else:
                    print("please enter a correct option")

ATM.users_from_list()

User.all_user["Ayush"].use_atm()














# User.users_from_list()
# print(User.all_user)
# print(User.all_user["Purushottam"].age)
# User.all_user["Ayush"].age = 23
# print(User.all_user["Ayush"].age)
