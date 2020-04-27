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
