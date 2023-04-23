
# variable declaration rules
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John
myvar2 = "John"

# avove mention all code has similar name but if you see then each one has,
#litttle bit of difference so all of the above code is containing totally different value 
# and the rule of creating variable name is listed below
	#1 variable contain alpha-numeric characters and underscores(A-z, 0-9, and _)
	#2 a variable must start with any letter or _ 
	#3 a variable name never start with any nubmer
	
	

# variable declaration
#camel case
myVariableName = "John"
#pascal case
MyVariableName = "John"
#snake case
my_variable_name = "John"


'''

# multiple variable declarations and value assign
'''
x,y,z = "Orange", "Banana" , "Cherry"
print(x)
print(y)
print(z)
'''

# one value in multiple variables
'''
x=y=z= "Orange"
print(x)
print(y)
print(z)
'''



# unpack a values in differen variables
'''
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)
'''




# assigned value in variable is printed out with print() function
'''
x = "Python is awesome"
print(x)

x="Python"
y = "is"
z= "awesome"
print(x,y,z)


print(x+y+z)
'''



# global variable declaration
'''
x = "awesome"

def myfunc():
	print("Python is " +x)

myfunc()
'''



'''
x = "awesome"

def myfunc():
	x = "fantastic"
	print("Python is " +x)
	
myfunc()

print("Python is " + x)

'''

'''
def myfunc():
	global x
	x= "fantastic"

myfunc()

print("Python is " +x)
'''

'''
x = "awesome"

def myfunc():
	global x 
	x= "fantastic"
	
myfunc()

print("Python is " + x)
'''






















































