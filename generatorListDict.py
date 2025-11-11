data = []
for i in range(100):
    if i % 2 == 0:
        data.append(i)
print(data)
###### Генератор списков 
data2=[i for i in range(100) if i%2==0]
print(data2)
###### dict comprehension
marks = {
    'gena':40,
    'alla':50,
    'bini':30,
}
newMarks = [v for k,v in marks.items()]
print(newMarks)


# my_str = "frg5gtth57ubdfh67"
# nums = []
# temp = ''
# for i in my_str:
#     if i.isdigit():
#         temp+=i
#     elif temp:
#         nums.append(int(temp))
#         temp = ''
# if temp:
#     nums.append(int(temp))
# print(nums)


import re
my_str = "frg5gtth57ubdfh67"
nums = re.findall('[0-9]+', my_str)
numbers = []
for i in nums:
    numbers.append(int(i))
print(numbers)
#################