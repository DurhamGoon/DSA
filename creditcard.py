class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank 
        self._acnt = acnt 
        self._limit = limit 
        self._balance = balance

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_acnt(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        
        if type(price) not in (int, float):
            raise TypeError("Bro, get yo bitcoin using ahhh outta here. We accept real money.")

        if price + self._balance > self._limit:
            print("This charge will go over your limit, brokey!")
            return False
        else:
            self._balance += price 
            return True 
        
    def make_payment(self, amount):
        if type(amount) not in (int, float):
            raise TypeError("Bro, get yo bitcoin using ahhh outta here. We accept real money.")
        
        if amount < 0:
            raise ValueError("You think you slick boi. We have a flawless banking game. All we care about is money. L bozo.")
        self._balance -= amount

    