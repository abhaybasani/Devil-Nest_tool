class x:
    def Atm(self):

        user = {
            'pin': 1234,
            'balance': 10000
        }
        print(user)

        def widthdraw_cash():
            while True:
                try:

                    amount = int(input("Enter the amount of money you want to widthdraw: "))
                    if amount > user['balance']:
                        print("You don't have sufficient balance to make this widthdrawal")
                    else:
                        user['balance'] = user['balance'] - amount
                        print(
                            f"{amount} .rs successfully widthdrawn your remaining balance is {user['balance']} .rs")
                        print('')
                        return False
                except:
                    print("got some error....")
        def balance_enquiry():
            print(f"Total balance {user['balance']} Dollars")
            print('')

        is_quit = False

        print('')
        print("Welcome to the ye wala ATM")

        pin = int(input('Please enter your four digit pin: '))

        if pin == user['pin']:
            while is_quit == False:
                print("what do you want to do")
                print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")

                query = int(input("Enter the number corresponding to the activity you want to do: "))

                if query == 1:
                    widthdraw_cash()
                elif query == 2:
                    balance_enquiry()
                elif query == 3:
                    is_quit = True

                else:
                    print("Please enter a correct value shown")
        else:
            print("Entered wrong pin")
obj=x()