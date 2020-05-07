def f(x):
	try:
		print("I am going to convert the input to an integer")
		print(int(x))
	except ValueError:
		print("Sorry, I was not able to convert that.")

def be_careful(a,b):
		try:	
			print(float(a)/flat(b))
		except (ValueError,TypeError,ZeroDivisionError) as detail:
			print("Handled Exception: ",detail)
		except:
			print("Unexpected Error!")
		finally:
			print("THIS WILL ALWAYS RUN!")