# Типы данных 
# int - целые числа
# float - число с остатком
# bool - True False 
# str - строки 'hello' "hello2" """hello3"""
# list - списки [1,2,3, 'hello4', [12,3,4], 45] изменяемый тип данных
# tuple - кортеж (1,2,3, 'hello4', [12,3,4], 45) он абсолютно похож на списки, только с одним исключением, тем что он не ИЗМЕНЯЕМЫЙ тип данных 
# set - множества, тип данных который также как tuple пишется через фигурные скобки, только с исключением на то что они неупорядоченные т могут ы себе хранить только уникальные значения
listA = [1,2,3, 'hello4', [12,3,4], 45]
listA[2] = 'hello5'
print(listA)

tupleA = (1, 2,3, 'hello', [12,3,4], 'hello4', 'hello4', 45)
# tupleA[2] = 'hello6'
# print(tupleA.count('hello4'))
# print(tupleA.index('hello4'))
print(type(tupleA))
print(tupleA[0])

setA = {'jiraf', 'Aibek', 'begemot', 'Gena', 'begemot', 'Gena', 'Mars', '34'}
setA = set(setA)
print(type(setA))
setA.add('Nina')
setA.remove('Aibek')
setA.pop()
print(setA)

listA = [1, 2,3, 'hello4', [12,3,4], 45, 'hello4', 'hello4', 'hello4']
listB = [1, 2.3, 'hello4', [12,3,4], 45]
listA.insert(2, 'Привет')
listA.pop(4)
listA.reverse()
print(listA.index('hello4'))
print(listA.count('hello4'))
listA.extend(listB)
print(listA)

# Переменные -variable
# Переменные предназначены для хранения данных
age = 34
list2 = [34,45,234]
print(list2)

# dict - dictionary - словари {key:value}
# dict - изменяемый тип данных, хранит в себе ключ и значение
names_age = {
    'elnura':18,
    'marsel':17,
    'marlen':17,
    'zahid':19,
    'aibike':16,
}
print(names_age.get('zahid')) # вывод значения ключа
for itemkey,value in names_age.items():
    print(itemkey, value)
    