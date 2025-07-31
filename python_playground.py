name = 'Jenifer'
# Буквы наоборот 
print(name[::-1])
# последние 3 символа
print(name[-3:])
# Каждые две буквы
print(name[::2])
# Все кроме последних двух
print(name[:-2])

#! Уровень B2 по строкам

# Перевернуться слова в строке
sentence = "hello my friend"
words = sentence.split() # ['hello', 'my', 'friend']
reversed_words = words [::-1] # ['friend', 'my', 'hello']
print(' '.join(reversed_words)) # 'friend my hello'

# Пока что по строка закончено тут

### FORMATED STRINGS - f{}

fruit = 'banana'
count = 5
print(f"I have {count} {fruit}s.")

### STRING METHODS 

# Methods are sensitive to Uppercase and lowercase register 
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.title())
print('Python' in course) # Вывод boolean format - True
print('python' in course) # Вывод - False

# FUNCTIONS NO = METHODS, here is why 

print(len(course))


### OPERATORS 

# Арифметические (+, -, *, /, **, %, //)

# 5 + 3

# Сравнения (==, !=, >, <, >=, <=)
# Сравнивают значения, возвращают True или False
# Пример: x == y, score > 100

# Членства (in, not in)

print('...' in course)

# Арифметические метода 
print(10 / 3)
print(10 // 3)
print (10 % 3) # remainder in the division = остаток от деления 10 : 3 = (3X3= 9, 10-9 = 1)
print (10 ** 3)

x = 10
x = x + 3 # инкрементировали
x += 3 # тоже самое 
y = 10
y -= 3

print(x)
print(y)
x = 10 + 3 * 2 ** 2
print(x)

### MATH FUNCTION

x = 2.9
print(round(x)) # rounds the number
print(abs(-2.9)) # absolute function to return positive number

import math

print(math.ceil(2.9))

# IF STATEMENTS

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")    
else:
    print("It's a lovely day")
print('Enjoy your day')

good_credit = True
house = 1000000
if good_credit:
    down_payment = int(house * 0.1)
else:
    down_payment = int(house * 0.2)

print(f"You need to put down {down_payment} dollars")

