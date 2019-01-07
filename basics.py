print('hello\'s world')
name = input("what is your name?\n")
#raw_input alternative

age = int(input("what is your " + \
        "age?\n"))
print('hello\'s ' + name+ ", age: "+str(age))
# or print('hello\'s ' + name+ ", age: %d" %age) d for decimal, f for float
#like C :D

#basic string functions
print(name.upper())
print(name.lower())
print(name.swapcase())

area = 100
num = 5
area += num
print('the area is %.2f' %area)

