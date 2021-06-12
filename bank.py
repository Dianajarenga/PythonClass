from datetime import datetime



class Account:
    def __init__(self,name,phone,limit):
        self.phone=phone
        self.balance=0
        self.name=name
        self.limit=limit
        self.transaction=[]
        

    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount must be in figures"

        if amount<=0:
            return f"The amount must be greater than zero"
        else :  
            self.balance+=amount  
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transaction.append(transaction)
    
            return f"Dear {self.name} you have deposited {amount}, for account No 222 your balance is {self.balance} " 
        

        

    def show_balance(self):
        return self.balance
        
        #adding functionality
         
    def withdraw(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount must be in figures"



        if amount>0:
             
            return f"Dear {self.name} you have withdrawn {amount}, for account No 222 your balance is {self.balance-amount} " 
        elif amount<=0:
            return f"Amount must be greater than zero"

        elif amount>self.balance :

            return f"Amount must be less than balance"
        else :
            self.balance-=amount   
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transaction.append(transaction)
    
            return f"{self.balance}"


    def borrow(self,amount):
        try:
            10+amount
        except TypeError:
            return f"the amount must be in figures"


        if amount>self.limit:
           print(f"Above loan limit ,please select a lower amount")                
        elif self.loan>0:
          print(f"you have an outstanding debt")
        else:
          self.loan+=1
          self.balance+=amount
          transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
          self.transaction.append(transaction)
    
          return f"loan Successful you have received amount {amount} your new balance is"

    def get_statement(self):
        for transactions in self.transaction:
            narration=transactions["narration"]
            amount=transactions["amount"]
            balance=transactions["balance"]
            time=transactions["time"]
            print(f"{time.strftime('%D')},{narration},amount{amount},balance{balance}")

   # def loan_repayment(self,amount):

       # if amount>=self.loan:
        #    return f"you have paid {amount},your new balance{amount-self.loan}"
       # elif amount<self.loan:
            #return f"you have a pending loan of { self.loan- amount} to pay"
       # else:
         # difference=amount-self.loan
         # self.balance+=difference
         # self.loan=0
          #transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
          #self.transaction.append(transaction)
    
         #on3 return f"loan Successful you have received amount {difference} your new balance is"
            #jeannine
        

#Transaction,Amount,Balance,Time,Code/id,Narration,
#add empty list to have a place to store transactions
#self.transactions=[]
#use dictionery to capture sttributes and append to self. transtactions    >>> now.strftime("%d-%m-%Y")


#ability to send to another account
    def transfer(self,amount,account):
        try:
            10+amount
        except TypeError:
            return f"the amount must be in figures"

        if amount<0:
            return f"please select a higher amount"
        fee=amount*0.05
        if amount+fee>self.balance:
            return f" your balance is {self.balance},you need{amount+fee}"
        else:
             self.balance-=amount+fee
             account.deposit(amount)
             return f" you have transfered {amount}  and your fee was {fee}your balance is{self.balance}"

#class inheritance syntax
#Class Parent:
#  ****
#class Child:
class Mobilemoneyaccount(Account):
    def __init__(self,name,phone,service_provider,limit=30000):
        Account.__init__(self,name,phone,limit)
        self.service_provider=service_provider
       
    
    def buy_airtime(self,amount):
        if amount>self.balance:
            return f"This is impossible!"
        elif amount>self.limit:  
            return f"select a lower amount your limit is {self.limit}"  
        else:
            amount<=self.balance
            self.balance-=amount

            return f"You have sucessfully purchased {amount} airtime and your balance is {self.balance-amount}."
        
            

