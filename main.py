# int£ & float
print("# int£ & float")

print(type(2 // 4))
print(4 % 15)

class MajbaUddin:
  pass
obj1 = MajbaUddin()
print(type(obj1))

m = 'Mejba'
u = ' Uddin'
print(m + u)

# string
print('# string')

single_string = 'Hey, Mejbah Uddin'
long_string = '''
wow
0 0
---
'''
print(single_string,long_string)

# string concatenation
print('# string concatenation')
print('Mejbah' + ' Uddin')

# math functions
print('# math functions')

Mejba = 8 / 6
print(round (Mejba))

print(abs(-20))

print(bin(5))
print(int('0b101', 2))

# variables
print("# variables")
mejba1 = 100
print(mejba1)

mejba_2 = 200
print(mejba_2)

mejba = 600
mejba_devide = mejba / 2
mejba_3 = mejba_devide
print(mejba_3)

mejba_4 = 700
mejba_4 = 400
print(mejba_4)

a,b,c,d = 100,200,300,400
print(a)
print(b)
print(c)
print(d)

# augmented assignment operator
print("# augmented assignment operator")
mejba_5 = 400
mejba_5 = mejba_5 + 100
print(mejba_5)
    # |
    # |
  # same
    # |
    # |
mejba_5 = 400
mejba_5 += 100
print(mejba_5)

# Type conversion
print("# Type conversion")
print(type(int(str(100))))
    # |
    # |
  # same
    # |
    # |
a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape Sequence
print('# Escape Sequence')

Escape_Sequence_str1 = "Hey, It\'s the best game of \"call of duty\""
Escape_Sequence_str2 = "\t Hey, It\'s the best game of \"call of duty\""
Escape_Sequence_str3 = "\n Hey, It\'s the best game of \"call of duty\""
print(Escape_Sequence_str1)
print(Escape_Sequence_str2)
print(Escape_Sequence_str3)

# Formatted string
print('#formatted string')

name = 'Hassan'
age = 20
# system 1
print('Hi ' + name + '. you are ' + str(age) + ' years old')
# system 2
print(f'Hi {name}. you are {age} years old')
# system 3
print('Hi {}. you are {} years old'.format(name,age))
# system 4
print('Hi {}. you are {} years old'.format('samim',20))
# system 5
print('Are you {1}? No, I am {0}.'.format('hassan','samim'))
# system 6
print('Hi {New_name}. you are {new_age} years old'.format(New_name='hassan',new_age=25))

# [Start: Stop: stepover]
print('# [start:stop:stepover]')

Mejba_uddin = '0123456789'
print(Mejba_uddin[::])
print(Mejba_uddin[::2])
print(Mejba_uddin[3:6:])
print(Mejba_uddin[4:6:])
print(Mejba_uddin[::-1])
print(Mejba_uddin[::-2])
print(Mejba_uddin[5:2:-1])
print(Mejba_uddin[5:3:-1])

# upper, title case, capitalize, find, replace .................
print('# upper, title case, capitalize, find, replace .................')

string_case = 'we use a don and then type in upper'
print(string_case.upper())
print(string_case.title())
print(string_case.capitalize())
print(string_case.find('then'))
print(string_case.replace('and', 'or'))

# what year were you born?
print('what year were you born?\n')

print('what year were you born?')
barth_day = input()
type_age = 2019 - int(barth_day)
print(f'your age is : {type_age}')

# password checker
print('# Password checker')

print('User name')
user_name = input()
print('Password')
user_pass = input()
hidd_pass = '*' * len(user_pass)

print(f'Your User name : {user_name}.')
print(f'Your password {hidd_pass}')

# list ..................................
print('# list ..................................')

list_string = [1, 'abcde', True, 12.1231]
list_string[2] = False
print(list_string)
print(list_string[1])
print(list_string[1][2])

# list slicing ...............
print('# list slicing ...............')

list_slicing = [
    'Computer',
    'Laptop',
    'Mobile phone',
    'Notebooks',
    'PC',
    'ETC'
]
print(list_slicing)
list_slicing[2] = 'Tablate'
print(list_slicing)
new_list = list_slicing[0:5]
new_list[0] = 'PC'
print(new_list)
print(list_slicing)

# Matrix
print('# Matrix')

Matrix = [
    [
        [1,2,3],
        [2,3,4],
        [3,4,5]
    ],[
        [1,2,3],
        [2,3,4],
        [3,4,5]
    ],[
        [1,2,3],
        [2,3,4],
        [3,4,5]
    ]
]

print(len(Matrix))
print(Matrix[0][2][1])
mat_asdf = Matrix.extend([123])
print(Matrix)

indexoflist = ['a', 'b', 'c', 'd', 'e']
print(indexoflist.index('c',1,3))
print(indexoflist)

in_string = 'This is a book'
print('f' in 'This is a book')
print('i' in in_string)

sorting_list = ['a','b','c','a','b','c']
print(sorted(sorting_list))
print(sorting_list)
sorting_list.sort()
print(sorting_list)

revers_list = ['x', 'y', 'z', 'x', 'y', 'z']
print(revers_list)
print(revers_list[::-1])
revers_list.reverse()
print(revers_list)

print(list(range(21)))

# adding
basked = [1, 2, 3, 4, 5]
basked.append(100)
basked.insert(3, 500)
basked.extend([101, 200])
print(basked)

# removing
basked2 = basked[:]
basked2.pop()
basked2.pop(7)
basked2.remove(100)
print(basked2)
# -------------------
basked3 = basked2[:]
basked3.clear()
print(basked3)

new_count = ['s', 's', 's', 'd', 'e']

print(new_count.count('s'))

# Start Question & Answer .......................

# Question No:

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket


# Answer :

basket.remove('Banana')
print(basket)
basket.pop()
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(0, 'Apples')
print(basket)
print(basket.count('Apples'))
basket.clear()
print(basket)

# End Question & Answer .......................
input('Thanks For Downloading...........')