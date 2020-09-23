# Simple vending machine change maker

class vending_machine:
    def __init__(self):
        # initializing denominations
        self.hundreds = 0

        self.fifties = 10

        self.twenties = 10

        self.tens = 10

        self.fives = 10

        self.ones = 25

        self.quarters = 25

        self.dimes = 25

        self.nickels = 25

        self.pennies = 25

        print("Welcome to vending machine change maker")

        print("Change maker initialized.")

        # loop until user quit

        while(True):

            # print stock info

            print("Stock contains:")

            print(str(self.hundreds)+"--- hundreds")

            print(str(self.fifties)+"--- fifties")

            print(str(self.twenties)+"--- twenties")

            print(str(self.tens)+"--- tens")

            print(str(self.fives)+"--- fives")

            print(str(self.ones)+"--- ones")

            print(str(self.quarters)+"--- quarters")

            print(str(self.dimes)+"--- dimes")

            print(str(self.nickels)+"--- nickels")

            print(str(self.pennies)+"--- pennies")

            # get valid purchase price

            cents = self.getPurchasePrice()

            if cents == -1:  # if the user select 'q'

                break

            # displaying menu

            print("Menu for deposits:")

            print("'h' - deposit a hundred dollar bill")

            print("'fi' - deposit a fifty dollar bill")

            print("'tw' - deposit a twenty dollar bill")

            print("'t' - deposit a ten dollar bill")

            print("'f' - deposit a five dollar bill")

            print("'o' - deposit a one dollar bill")

            print("'q' - deposit a quarter")

            print("'d' - deposit a dime")

            print("'n' - deposit a nickel")

            print("'p' - deposit a penny")

            print("'c' - cancel the purchase")

            initial_cents = cents

            # recieving payment while any payment is due

            while self.print_payment_due(cents):

                # getting valid deposit choice and taking corresponding action

                deposit_choice = self.deposit_choice()

                if(deposit_choice == -1):

                    continue

                if deposit_choice == 'p':

                    self.pennies += 1

                    cents -= 1

                if deposit_choice == 'n':

                    self.nickels += 1

                    cents -= 5

                if deposit_choice == 'd':

                    self.dimes += 1

                    cents -= 10

                if deposit_choice == 'q':

                    self.quarters += 1

                    cents -= 25

                if deposit_choice == 'o':

                    self.ones += 1

                    cents -= 100

                if deposit_choice == 'f':

                    self.fives += 1

                    cents -= 500

                if deposit_choice == 't':

                    self.tens += 1

                    cents -= 1000

                if deposit_choice == 'tw':

                    self.twenties += 1

                    cents -= 2000

                if deposit_choice == 'fi':

                    self.fifties += 1

                    cents -= 5000

                if deposit_choice == 'h':

                    self.hundreds += 1

                    cents -= 10000

                if deposit_choice == 'c':

                    cents -= initial_cents

        # calculating and displaying total cents in machine

        cents = (10000 * self.hundreds)+(5000 * self.fifties)+(2000 * self.twenties)+(1000 * self.tens)+(500 * self.fives)+(100*self.ones)+(25*self.quarters)+(10*self.dimes)+(5*self.nickels) + (1*self.pennies)

        print("Total: ", end="")

        if(cents >= 100):

            print(str(cents//100)+" dollars", end=" and ")

        print(str(cents % 100) + " cents")

    # prompt the user to chose a valid deposit choice and return it.

    def deposit_choice(self):

        user_input = input("Select your deposit: ")

        if (user_input == 'p' or user_input == 'n' or user_input == 'd' or user_input == 'q' or user_input == 'o' or user_input == 'f' or user_input == 't' or user_input == 'tw' or user_input == 'fi' or user_input == 'h' or user_input == 'c'):

            return user_input

        print("Wrong selection: "+user_input)

        return -1

# checks if payment is due and offer change

    def print_payment_due(self, cents):

        # if payment completed and change is needed

        if(cents <= 0):

            change =- cents

            # calculate the number of coins using greedy algorithm

            hundreds = min(self.hundreds, (change//10000))
            change = change - 10000 * hundreds

            fifties = min(self.fifties, (change//5000))
            change = change - 5000 * fifties

            twenties = min(self.ones, (change//2000))
            change = change - 2000 * twenties

            tens = min(self.ones, (change//1000))
            change = change - 1000 * tens

            fives = min(self.fives, (change//500))
            change = change - 500 * fives

            ones = min(self.ones, (change//100))
            change = change - 100 * ones

            quarters = min(self.quarters, (change//25))

            change = change - 25 * quarters

            dimes = min(self.dimes, (change//10))

            change = change - 10 * dimes

            nickels = min(self.nickels, (change//5))

            change = change - 5 * nickels

            pennies = min(self.pennies, (change//1))

            change = change - 1 * pennies

            print("Please take the change below.")

            if(fifties > 0):

                self.fifties -= fifties

            print(str(fifties)+" fifties")

            if(twenties > 0):

                self.twenties -= twenties

            print(str(twenties) + " twenties")

            if(tens > 0):

                self.tens -= tens

            print(str(tens) + " tens")

            if(fives > 0):

                self.fives -= fives

            print(str(fives) + " fives")


            if(ones > 0):

                self.ones -= ones

            print(str(ones) + " ones")

            if(quarters > 0):

                self.quarters -= quarters

            print(str(quarters) + " quarters")

            if(dimes > 0):

                self.dimes -= dimes

            print(str(dimes) + " dimes")

            if(nickels > 0):

                self.nickels -= nickels

            print(str(nickels) + " nickels")

            if(pennies > 0):

                self.pennies -= pennies

            print(str(pennies) + " pennies")

            if(change > 0):

                print("The Machine is out of change.")

                print("See the store manager for the remaining fund")

                print("Amount due is: ", end="")

            if (change >= 100):

                print(str(change // 100) + " dollars", end=" and ")

            print(str(change % 100) + " cents")

            if(cents == 0):

                print("No change due.")

            return False

        # displaying due info
        print("Payment due: ", end="")

        if(cents >= 100):

            print(str(cents//100)+" dollars", end=" and ")

        print(str(cents % 100) + " cents")

        return True

    # Function to accept and return valid purchace price
    def getPurchasePrice(self):

        print("Enter the purchase price (xx.xx) or 'q' to quit: ", end="")

        user_input = input()

        if user_input == 'q':

            return -1

        if float(user_input) <= 0:

            print("The price must be a non-negative.")

            return self.getPurchasePrice()

        else:
            return int(round(float(user_input)*100))


user = vending_machine()
