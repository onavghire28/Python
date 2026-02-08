#Atm machine code
class Atm:

    #constructor        --> function inside the class
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance 
        4. Press 4 to withdraw
        5. Anything else to exit
        """) 

        if user_input == '1':
            #create pin
            self.create_pin()

        elif user_input == '2':
            #change pin
            self.change_pin()

        elif user_input == '3':
            # check balance
            self.check_balance()

        elif user_input == '4':
            #withdraw
            self.withdraw()
        else:
            exit()    

    def create_pin(self):
        user_pin = input("Enter the pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter the balance: "))
        self.balance = user_balance 

        print("Pin created successfully")   
        self.menu()

    def change_pin(self):
        old_pin = input("Enter the old pin: ")

        if old_pin == self.pin:
            #change pin
            new_pin = input("Enter the new pin: ")

            self.pin = new_pin
            print("Pin change successfully")
            self.menu()

        else:
            print("Not able to change")
            self.menu()   

    def check_balance(self):
        user_pin = input("Enter the pin: ")

        if user_pin == self.pin:
            print("Your Balance: ", self.balance)

        else:
            print("Try Again") 

        self.menu()      

    def withdraw(self):
        user_pin = input("Enter the pin: ")

        if user_pin == self.pin:
            amount = int(input("Enter the Amount: "))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdraw successfully, balance is: ", self.balance)

            else:
                print("Balance is less")    

        else:
            print("Pin is not correct")  

        self.menu()                       

obj = Atm()           