#Simple vending machine change maker

class vending_machine:
    def __init__(self):
        #initializing denominations
        self.fives=0

        self.ones=0

        self.quarters=25

        self.dimes=25

        self.nickels=25

        print("Welcome to vending machine change maker")

        print("Change maker initialized.")

        #loop until user quits

        while(True):

            #print stock info

            print("Stock contains:")

            print(str(self.fives)+"--- fives")

            print(str(self.ones)+"--- ones")

            print(str(self.quarters)+"--- quarters")

            print(str(self.dimes)+"--- dimes")

            print(str(self.nickels)+"--- nickels")

            #get valid purchase price

            cents=self.getPurchasePrice()

            if cents==-1:# if the user select 'q'

                break


            #displaying menu

            print("Menu for deposits:")

            print("'f' - deposit a five dollar bill")

            print("'o' - deposit a one dollar bill")

            print("'q' - deposit a quarter")

            print("'d' - deposit a dime")

            print("'n' - deposit a nickel")

            print("'c' - cancel the purchase")

            initial_cents=cents

            #recieving payment while any payment is due

            while self.print_payment_due(cents):

            # getting valid deposit choice and taking corresponding action

                deposit_choice=self.deposit_choice()

                if(deposit_choice==-1):

                    continue

                if deposit_choice=='n':

                    self.nickels+=1

                    cents-=5

                if deposit_choice=='d':

                    self.dimes+=1

                    cents-=10

                if deposit_choice=='q':

                    self.quarters+=1

                    cents-=25

                if deposit_choice=='o':

                    self.ones+=1

                    cents-=100

                if deposit_choice=='f':

                    self.fives+=1

                    cents-=500

                if deposit_choice=='c':

                    cents-=initial_cents

        #calculating and displaying total cents in machine

        cents= (500 * self.fives)+(100*self.ones)+(25*self.quarters)+(10*self.dimes)+(5*self.nickels)

        print("Total: ",end="")

        if(cents>=100):

            print(str(cents//100)+" dollars",end=" and ")

        print(str(cents % 100) + " cents")

    #prompt the user to chose a valid deposit choice and return it.

    def deposit_choice(self):

        user_input =input("Select your deposit: ")

        if user_input=='n' or user_input=='d' or user_input=='q' or user_input=='o' or user_input=='f' or user_input=='c':

            return user_input

        print("Wrong selection: "+user_input)

        return -1

#checks if payment is due and offer change

    def print_payment_due(self,cents):

        #if payment completed and change is needed

        if(cents<=0):

            change=-cents

            #calculate the number of coins using greedy algorithm

            quarters=min(self.quarters,(change//25))

            change=change-25*quarters

            dimes=min(self.dimes,(change//10))

            change=change-10*dimes

            nickels=min(self.nickels,(change//5))

            change=change-5*nickels

            print("Please take the change below.")

            if(quarters>0):

                self.quarters-=quarters

            print(str(quarters)+" quarters")

            if(dimes>0):

                self.dimes-=dimes

            print(str(dimes)+" dimes")

            if(nickels>0):

                self.nickels-=nickels

            print(str(nickels)+" nickels")

            if(change>0):

                print("The Machine is out of change.")

                print("See the store manager for the remaining fund")

                print("Amount due is: ",end="")

            if (change >= 100):

                print(str(change // 100) + " dollars", end=" and ")

            print(str(change % 100) + " cents")

            if(cents==0):

                print("No change due.")

            return False

        #displaying due info
        print("Payment due: ",end="")

        if(cents>=100):

            print(str(cents//100)+" dollars",end=" and ")

        print(str(cents % 100) + " cents")

        return True


    # Function to accept and return valid purchace price
    def getPurchasePrice(self):

        print("Enter the purchase price (xx.xx) or 'q' to quit: ",end="")

        user_input=input()

        if user_input == 'q':

            return -1

        if float(user_input)<0 or (int(round(float(user_input)*100)))%5!=0:

            print("The price must be a non-negative and multiple of 5 cents.")

            return self.getPurchasePrice()

        else:
            return int(round(float(user_input)*100))

user = vending_machine()
