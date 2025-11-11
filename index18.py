class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")
        
class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position

    def calculate_salary(self):
        return self.salary
    
    def info(self):
        person = super().info()
        print(f"{person} Должность: {self.position}, Зарплата: {self.salary}")


