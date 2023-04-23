#print('learning linux')


#word = 'word'

#sentence= " This is a sentence."

'''paragraph = """ This is a pragraph
. It made uo multiple lines and sentences."""

'''
#print(word,sentence)

#print(paragraph)


'''
the_world_is_flat= True
if the_world_is_flat:
	print("Be careful not to fall off!")

'''

'''
x = int(input("Please enter an integer: "))

if x<0:
	x=0
	print('Negative changed to zero')
elif x==0:
	print('Zero')
elif x==1:
	print('Single')
else:
	print('More')
	
'''


'''
words = ['cat', 'window', 'defenestrate']

for w in words:
	print(w,len(w))	

'''

'''
users = {'Hans' : 'active', 'Eleonore' : 'inactive' , 'raj':'active'}

for user, status in users.copy().items():
	if status == 'inactive';
		del users[user]
		
active_users = {}
for user,status in users.items():
	if status == 'active':
		active_users[user] = status


'''




'''
for i in range(5):
	print(i)
	
	'''


'''
a = ['Mary' , 'had' ,'a' , 'little' , 'lamb']
for i in range(len(a)):
	print(i, a[i] )

'''	


# print(sum(range(10)))


# for n in range(2,10):
# 	for x in range(2,n):
# 		if n % x ==0:
# 			print(n, 'equals', x, '*' , n//x)
# 			break
# 	else:
# 		print(n, 'is a prime number')


# for num in range(2,10):
# 	if num % 2 ==0: 
# 		print("Found an even number", num)
# 		continue
# 	print("Found an odd number",num)




# while True: 
	# pass



# class MyEmptyClass:
# 	pass






# def initlog(*args):
# 	pass



# def http_error(status):
# 	match status:
# 		case 400:
# 			return "Bad request"
# 		case 404:
# 			return "Not found"
# 		case 418:
# 			return "I'm a teapot"
# 		case _:
# 			return "Something's wrong the internet"






# match point:
# 	case(0,0):
# 		print("Origin")
# 	case(0,y):
# 		print(f"Y={y}")
# 	case(x,0):
# 		print(f"X={x}")
# 	case (x,y):
# 		print(f"X={x}, Y={y}")
# 	case _:





# from enum import Enum
# class Color(Enum):
# 	RED = 'red'
# 	GREEN = 'green'
# 	BLUE = 'blue'

# color = Color(input("Enter your choice of 'red' , 'blue' or 'green' : "))
# match color: 
# 	case Color.RED:
# 		print("I see red!")
# 	case Color.GREEN:
# 		print("Grass is green")
# 	case Color.BLUE:
#		print("I'm feeling the blues :(")









"""Print a Fibonaccin series up to n"""
'''def fib(n):
	a,b=0,1
	while a<n:
		print(a, end=' ')
		a,b= b,a+b
	print()
	
	
fib(2000)

'''



'''
#return Fibonacci series up to n
def fib2(n):
	result = []
	a,b=0,1
	while a<n: 
		result.append(a)
		a,b = b,a+b
	return result

f100 = fib2(100)
print(f100)
'''

'''
def ask_ok(prompt, retries=4, reminder = 'Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no' , 'nop', 'nope'):
			return False
		retries = retries-1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)
		
'''



i=5
def f(arg = i):
	print(arg)
	
i = 6
f()
























