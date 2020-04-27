#Lesson2Exercises
#save fav snack into var, print it 100 times
snack = "apple"
#print((snack +" ")*100)

#save a second fav snack, concat the two snacks and print 100 times
snack2 = "banana"
#print((snack+" "+snack2+" ")*100)

#create list, check to see if snack is in list
groceries = ["grape","strawberry","apple","watermelon","blueberries"]
#print(snack in groceries)

#check if snack2 is in list
#print(snack2 in groceries)

#fast swap snack and snack2, print to verify
snack,snack2 = snack2,snack
#/print("Original was apple, banana. Swapped is "+snack,snack2

#make list of grocery prices then find cheapest and most expensive item
prices = [9.42,5.67,3.25,13.40,7.50]
print("Cheapest item costs: ",min(prices))
print("Most expensive item costs: ",max(prices))

#import random, run help(random.randint), use randint to randomly print your fav snack 0-100

#randint(a,b) method of random.Random instance
	#return random integer in range[a,b], including both end points.

import random

print(random.randint(0,100)*snack2)	

#run dir(random), find func in random to return random item from list
print(random.choice(groceries))

#select random price from list, round to nearest int, print result
mystery = random.choice(prices)
print(mystery)
mystery = round(mystery)
print(mystery)

#challenge: rand item from price list is chosen, if more than 10; you get item & diff in price back. else you get item and change back as normal. 

change = 0;
promo = random.choice(prices)
if(promo>10):
	change = abs(promo-10)
	print("YOU WIN FREE CHANGE")
else:
	change = 10-promo
	print("You did not win free change")

print("Promo item price is: ",promo)
print("Change is: ",change)


#MAKING YOUR OWN FUNCTIONS
def first_funct(x):
	return(x*2)#use print to see value

first_funct(10)
first_funct("hello")

#simplest func ever
def simple():
	pass

def add(a,b):
	return a+b

#add(2,3) returns 5
#add(1) returns error because only 1 arg instead of 2
#add('a',3) returns error because concact str & int
#add('a','b') returns concat str 'ab'
#add returns where function is stored in mem

def add2(a,b):
	print(a+b)

#x = add(2,3) - add() returns a value so x is assigned the returned ans
#x = add2(2,3) - add2() prints value so while func is ran, no value is returned therefor x has no value.

#x = add - x is now storing mem location of add() 
#add = 7 - would reassign var add to a int instead of func
#add(2,3) - wouldn't work as you cant pass args to int
#x(2,10) - would return 12 because x is pointing to mem location of add() and therefore x is callable

#create all_the_snacks(snacks) to print snacks 100 times
#def all_the_snacks(snacks):
	#print(snacks*100)

#all_the_snacks(snack2)
#all_the_snacks(2) #when given an int, returns int

#rewrite all_the_snacks to take spacer as arg
def all_the_snacks(snacks,spacer):
	print((snacks+spacer)*100)

all_the_snacks(snack," ")
#all_the_snacks(snack,2) #error in concat str and int
all_the_snacks(2,10)#returns product of two nums

#rewrite allthesnacks to control num of times printed
def all_the_snacks(snacks,spacer,num):
	print((snacks+spacer)*num)

all_the_snacks(snack," ",2)

def in_grocery_list(grocery_item):
	if(grocery_item in groceries):
		#print("True")
		return(True)
	else:
		#print("False")
		return(False)

in_grocery_list(snack)

def price_matcher():
	print(random.choice(groceries),random.choice(prices))

#price_matcher()

#challenge modify pricematcher to return item and price instead of print
#write free_change() to call price_matcher() and uses result to print item and abs val of change assuming you paid $10
def price_matcher():
	r_item = random.choice(groceries)
	r_price = random.choice(prices)
	#print(r_item,r_price)
	return(r_item,r_price)

price_matcher()

def free_change():
	x_item, x_price = price_matcher()
	print(x_item,abs(10-x_price))

free_change()