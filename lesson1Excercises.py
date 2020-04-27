#Built in functions and methods
#-------------------------------
#help(x):shows interactive help
#dir(x):gives the directory of the objects, ie all the methods available
#type(x)tells you the type of x
#isinstance(a,b): tells if obj a is an instance of b
#print
#hasattr(a,b)
#getattr
#id
#input
#1-Make grocery list of 5 items
print("Items on grocery list-")
list = ["apple","banana","milk","eggs","bacon"];
for x in list:
	print(x)
#prices for respective items
list = [9.42,5.67,3.25,13.40,7.50];
print("")
print("Total price of all items is =",+sum(list))
#total = all items + 4 more of last item bought
total = sum(list) +(7.5*4);
print("Add an addittional 4 packages of bacon",+total)