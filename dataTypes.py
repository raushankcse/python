# Data types in python

'''
x = "Hello World"
print(type(x))
x =20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple" , "banana", "cherry"}
print(type(x))
x = frozenset({"apple" , "banana" , "cherry"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))
'''


# number data types in python
'''
x=1
y = 2.8
z = 2j

print(type(x))
print(type(y))
print(type(z))
'''

#integer types
'''
x=1
y= 356898374987934293
z= -323555

print(type(x))
print(type(y))
print(type(z))

'''

#float types
'''
x=1.10
y=1.0
z=-35.59

print(type(x))
print(type(y))
print(type(z))



x=35e3
y =12E4
z= -87.7e100

print(type(x))
print(type(y))
print(type(z))

'''



#complex numbers
'''
x=3+5j
y = 5j
z= -5j

print(type(x))
print(type(y))
print(type(z))
'''


# type conversion
'''
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))
'''



# generating random number
'''
import random

print(random.randrange(1,10))
'''



# #####################Strings data types
'''
a="Hello"
print(a)
'''

# multiline strings
'''
a = """ it is 
a 
multiline string.
"""

print(a)
'''

"""
a = '''It is 
a 
multiline
string
'''
print(a)

"""


# strings are work like arrays
'''
a= "Hello, World!"
print(a[1])
'''

# string looping
'''
for x in "banana":
	for i in x:
		print(i,end="")
	print()

'''


# length of the string
'''
a = "Hello, World!"
print(len(a))
'''


# Check String is in or not
'''
txt = "The best things in life are free!"
print("free" in txt)
'''

'''
txt = "The best things in life are free!"
if "free" in txt:
	print("Yes, 'free' is present.")
'''

'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''


'''
txt = "The best things in life are free!"
if "expensive" not in txt:
	print("No, 'expensive' is NOT present. ")
'''


# string method
'''
b = "Hello, World!"
print(b[2:5])
'''

'''
b = "Hello, World!"
print(b[:5])
'''

'''
b = "Hello, World!"
print(b[2:])
'''

'''
b = "Hello, World!"
print(b[-5:-2])
'''


'''
a = "Hello, World!"
print(a.upper())
'''

'''
a = "   Hello, World!"
print(a.strip())
'''



'''
a = "Hello, World!"
print(a.replace("H", "J"))
'''



'''
a = "Hello, World!"
print(a.split(","))
'''

'''
a = "Hello"
b = "World"
c = a+" " +b
print(c)
'''


'''
age = 36
txt = "My name is John, I am {}" 
print(txt.format(age))
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}. "
print(myorder.format(quantity, itemno, price))
'''


#escape strings
'''
txt = "We are the so-called \" Vikings\" from the north."
print(txt)
'''



























