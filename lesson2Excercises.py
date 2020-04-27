#Lesson2Exercises
#save fav snack into var, print it 100 times
snack = "apple"
print((snack +" ")*100)
#save a second fav snack, concat the two snacks and print 100 times
snack2 = "banana"
print((snack+" "+snack2+" ")*100)
#create list, check to see if snack is in list
groceries = ["grape","strawberry","apple","watermelon","blueberries"]
print(snack in groceries)
#check if snack2 is in list
print(snack2 in groceries)
#fast swap snack and snack2, print to verify
snack,snack2 = snack2,snack
print("Original was apple, banana. Swapped is "+snack,snack2)