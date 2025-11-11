class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id
        self.__hourly_rate = hourly_rate
        self._is_busy = False
        self._current_client = None
        self._hours = 0

    @property
    def id(self):
        return self.__id
    
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate >=50 and new_rate <=1000:
            self.__hourly_rate = new_rate
            return self.__hourly_rate
        

    def start_session(self, client, hours):
        if self._is_busy:
            print("Комп {self.id} занят")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True # Комп знят
            self._current_client = client
            self._hours = hours
            print(f"{client.name} начал сессию")
            return True
        else:
            print(f"Не хватает денег {client}")

    def end_session(self): # завершает сессию, считает оплату
        self._is_busy = False
        income = self.__hourly_rate * self._hours
        client_name= self._current_client.name
        print("Сессия завершена {client_name}")
        self._current_client = None
        self._hours = 0
        return income
    
    def info(self):
        status = 'Занят' if self._is_busy else 'Сыободен'
        print(f"Комп {self.id}:{status}")

class Client:
    def __init__(self, name, balance):
        self.name, self.balance = name, balance

    def pay(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма.")

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount

    def info(self):
        print(f"{self.name}: {self.balance} у.е.")

class Client:
    def __init__(self, name, balance):
        self.name = name 
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def add_balance(self, amount):
        if amount > 0 and amount<=1000:
            self._balance += amount
            print(f"Баланс пополнен на {amount}сом, теперь у вас {self._balance}")
        else:
            print(f"Введите корректное значение на пополнение")
            return False

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def info(self):
        print(f"Имя: {self.name} на карте: {self.balance} сом")

c = Client("Захид", 1000)
c.pay(300)
c.add_balance(200)
c.info() 

class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []
        self._income = 0

    def add_computer(self, computer):
        pass
    def find_free_computer(self):
        pass
    def serve_client(self, client, hours):
        pass
    def end_all_session(self):
        pass
    def show_status(self):
        pass