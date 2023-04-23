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


for n in range(2,10):
	for x in range(2,n):
		if n % x ==0:
			print(n, 'equals', x, '*' , n//x)
			break
	else:
		print(n, 'is a prime number')





