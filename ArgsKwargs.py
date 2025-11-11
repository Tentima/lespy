#*args, **kwargs
# arguments

def add(*args):
    print(args)

add(7,8,9,0,6,5)

a = [5,6,7,8,9]
b = [*a,1,2,3,4]
print(b)

def sum2(*args):
    total = 0
    for n in args:
        total+=n
        print(f"Сумма: {total}")

sum2(4,5,6,7,8,9,3,2,1)


def printScore(student, *args):
    print(f"Имя: {student}")
    for sc in args:
        print(sc, end=', ')

printScore("Мао", 2,3,4,5,6)


# **kwargs KEYWOD ARGUMENTS - DICT {KEY:VALUE
def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

show(name='Mao', age=17, birth='12.12.2000', city='Bishkek')


def pets(owner, **kwargs):
    print(f"Хозяин: {owner}")
    for k,v in kwargs.items():
        print(k,v)

pets('Zahid', dog='Bobik', cat='bruda', eats=['fish', 'meat','water'])

# Комбинация
# I)Оператор **kwargs нельзя писать до *args, если сделаете то будет ошибка
# II) Мы конечно же можем писать не только args и kwargs, но и совсем другими словами, но общепринятые правила говорят чтобы писали именно так *args и **kwargs
def demo(*args, **kwargs):
    print('args=',args)
    print('kwargs=',kwargs)

demo(43,3,4,5,6,7,56,7,8,9, age=45, hobbi='гимнастика', phone='redmi')
