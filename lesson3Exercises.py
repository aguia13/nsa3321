#Lesson 03: Flow Control
import random
import datetime
import time
#variables
a = "mystring"
blood = "blood-oxygenation level dependent functional magnetic resonance imaging"
favSnack = "Hot Cheetos"
favSnack2 = ""
prices = (9.42,5.67,3.25,13.40,7.50)
groceries = "grape","strawberry","apple","watermelon","blueberries"

'''
INTRO
def you_won(price_list):
	if(random.choice(price_list)>10):
		print("True")
	else:
		print("False")

you_won(prices)

def snack_check(snack):
	if(snack==favSnack):
		#print("True")
		return True
	else:
		#print("False")
		return False

snack_check(favSnack)
'''

#IF STATEMENT
'''
def even(n):
	if(n%2==0):
		print('I am even!')
	else:
		print('I am odd!')
even(2)
even(3)
even('hello')	#str arg hasn't been covered	


def even(n):
	if(type(n)!=int):
		print('I only talk about integers')
	elif(n%2 == 0):
		print('I am even!')
	else:
		print('I am odd!')
even(2)
even(3)
even('hello')
'''

#WHILE,BREAK,CONTINUE,ELSE
'''
i=1
while(i<2):
	print(i)
	if True:
		break
	i+=1	
else:
		print("This wont print because the loop was exited early")
print("Done!")	

while(i<=10):
	i=i+1
	print(favSnack)

i=1
while(i<=10):
	print(favSnack*i)
	i=i+1
i=1
while(i<100):
	i = i+1
	pass
print((favSnack+' ')*100)

'''
#FOR LOOP
'''
for i in [1,2,3,4,5,'a','b','c']:
	print(i)

for i in [1,2,3,4,5,'a','b','c']:
	print(i,type(i))

for c in 'orange':
	print(c)

for i in 'blood-oxygenation level dependent functional magnetic resonance imaging':
	print(i)

for i in groceries:
	print("Note to self, buy: "+i)

l = 1
for i in groceries:
	if(i==favSnack):
		print("Here is my favorite snack!")
		break
	print(l,i)
	l = l+1

l=1
for i in groceries:
	if(l<len(groceries)):
		print(l,i)
		l = l+1
	elif(i==favSnack2):
		print("Here is my favorite snack!")
		break
	else:
		print(l,i)
		print("My favorite snack isnt here!")
#range & xrange
for i in range(len(a)):
	print("The character at position "+str(i)+" is "+a[i])

for(i,j) in enumerate(a):
	print("The character at position "+str(i)+" is "+j)
#In python3, the range function produces an iterator as an obj that knows where to start, stop and how to get from start to stop.
#xrange for python2

for i in range(len(groceries)):
	print(i+1,groceries[i])
'''
for i in enumerate(groceries):
	print(i)

for i in range(10):
	print(favSnack)




#functions
def snack_check(snack):
	if(type(snack)!= str):
		print("Get the snack out of here")
	elif(snack==favSnack):
		print("That's my favorite snack")
	else:
		print("I hate that snack")
#snack_check("Hot Cheetos")

def in_grocery_list(grocery_item):
	if(type(grocery_item)!=str):
		print("Hey that's not a string!")
	elif(grocery_item in groceries):
		print("I bought that!")
	else:
		print("That's not mine!")
#in_grocery_list(favSnack)
#in_grocery_list(123)

def you_won(priceList):
	r_price = random.choice(priceList)
	if(r_price>10):
		print("You won:$",abs(10-r_price))
	else:
		print("You did not win! Here is your change",(10-r_price))
#you_won(prices)

def splitter(word):
	splitted = str.split(word," ")
	for i in splitted:
		print(i)
#splitter(blood)

#Challenge
def guessMyNum():
	answer = int((random.random()*10))
	guess = int(input("What number am I thinking of? You get 3 guesses."))
	g_remaining = 3

	#print(answer)
	#print(guess)
	while(g_remaining>0):
		if(answer==guess):
			print("You're correct! The number is ",answer)
			break
		elif(g_remaining==1):
			print("You're out of guesses. The answer was",answer)
			break
		else:
			g_remaining = g_remaining-1
			guess = int(input("You have "+str(g_remaining)+"guesses remaining."))
#guessMyNum()		