class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return self.is_available

    def return_book(self):
        self.is_available = True
        return self.is_available

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Доступность: {self.is_available}"

book1 = Book('Война и мир', "Лев Толстой", 1867)
book1.borrow()
# print(book1.info())
# book1.return_book()
# print(book1.info())

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.balance += amount
        print(f"{self.owner} пополнил счет на {amount}сом, теперь у вас {self.balance}сом")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
            return
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.balance -= amount
        print(f"{self.owner} сняли со счета {amount}сом, теперь у вас {self.balance}сом")

    def info(self):
        print(F"Владелец: {self.owner}, Счет: {self.balance}")
        
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_accounts(self, owner):
        accounts = BankAccount(owner)
        self.accounts.append(accounts)
        print(f"Открыт счет на имя {owner} в банке {self.name}")
        return accounts
    
    def find_accounts(self, owner):
        for acc in self.accounts:
            if acc.owner == owner:
                print(f"{owner} зарегистрирован в банке")
                return acc
        print(f"Не найден {owner}")
        return None
    
    def transfer(self, from_owner, to_owner, amount):
        from_acc = self.find_accounts(from_owner)
        to_acc = self.find_accounts(to_owner)
        if not from_acc or not to_acc:
            print("Перевод невозможен")
            return
        if from_acc.balance < amount:
            print("Недостаточно средств")
            return
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Перевод {amount}сом от {from_acc} к {to_acc} выполнен")
    
bank = Bank('PKS-Bank')
acc1 = bank.open_accounts("Aijan")
acc2 = bank.open_accounts("Denis")
bank.find_accounts('Denis')
acc1.deposit(3000)
acc2.deposit(9000)
acc2.deposit(1200)
acc1.info()
acc2.info()
bank.transfer('Denis', 'Aijan', 3200)
acc1.info()
acc2.info()
