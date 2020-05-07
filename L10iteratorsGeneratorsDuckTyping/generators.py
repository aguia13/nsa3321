import random

def xsquared():
	for i in range(30):
		yield i*i

def xsquared_inf():
	x = 0
	while True:
		yield x*x
		x += 1

def day_of_week():
	i = 0
	days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	while True:
		yield days[i%7]
		i += 1

def snowday(prob=.01):
	r = random.random()
	if r < prob:
		return "snowday"
	else:
		return "regular day"


n = 0 
for x in day_of_week():
	today = snowday()
	print(x + "is a "+today)
	n+=1
	if today == "snowday":
		break