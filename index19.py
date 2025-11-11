class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self.balance
    
    def withdraw(self, amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"Вы сняли {amount}сом, осталось: {self.balance}сом")
        else:
            print(f"Недостаточно денег, у вас осталось {self.balance}сом")

    def info(self):
        print(f"{self.name} Возраст: {self.age} Денег {self.balance} сом")

    
class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = [] # список объектов Person
        self.products = [] # (депозиты, кредиты, рассрочки)
        self.income = 0 # доход банка
        
    def add_client(self, client):
        self.clients.append(client)
        print(F"Клиент {client.name} добавлен")

    def add_product(self, product):
        self.products.append(product)
        print(f"Продукт добавлен")

    def add_income(self, amount):
        self.income += amount

    def calculate_total_profit(self):
        return self.income

    def show_clients(self):
        print("Наши клиенты:")
        for i in self.clients:
            print(f". {i.info()}")

    def show_products(self):
        print("Наши Продукты:")
        for i in self.products:
            print(f". {i.info()}")

class BankProduct:
    def __init__(self, client, amount, interest_rate, term_month):
        self.client = client
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_month = term_month

    def calculate_interest(self):
        return self.amount * (self.interest_rate / 100) * (self.term_month / 12)
    
    def info(self):
        print(f"{self.client.name} сумма: {self.amount}сом, ставка: {self.interest_rate}%, срок: {self.term_month} мес")
        

class Deposit(BankProduct):
    def close_deposit(self, bank):
        if self.client.withdraw(self.amount):
            profit = self.calculate_interest()
            payout = self.amount + profit
            self.client.deposit(payout)
            bank.add_income(profit * 0.01)
            print(f"Депозит закрыт: клиент {self.client.name} получил {payout}сом (включая {profit}сом в процентах)")
        else:
            print(f"Недостаточно денег чтобы открыть депозит")

class Credit(BankProduct):
    def monthly_payment(self):
        total = self.amount+self.calculate_interest()
        return round(total / self.term_montns, 2)
    
    def close_credit(self, bank):
        self.client.deposit(self.amount)
        total_payment = self.amount + self.calculate_interest()
        if self.client.withdraw(total_payment):
            bank.add_income(self.calculate_interest())
            print(f"Кредит закрыт {self.client.name} выплатил {total_payment}сои (включая проценты)")
        else:
            print(f"{self.client.name} не смог погасить кредит")
bank = Bank('PKS Bank')
zahid = Person('Zahid', 17, 100)
aibike = Person('Aibike')
