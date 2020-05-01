'''
EXERCISE #1
IF WE LIST ALL THE NATURAL NUMBERS BELOW 10 THAT ARE MULITPLES
OF 3 OR 5, WE GET 3,5,6 AND 9. THE SUM OF THESE MULTIPLES IS 23.

FIND THE SUM OF ALL THE MULTIPLES OF 3 OR 5 BELOW 1000
'''
def multiplesOf3or5():
	#create a list 'a' that iterates from 1-1000 and for every i checks if i modulo 3 == 0 or i modulo 5 == 0
	a = [i for i in range(1,1000) if i%3==0 or i%5==0]
	#save sum of values in list in seperate var to return
	total = sum(a)
	print('Multiples of 3 or 5:',a,'\n')
	print('Sum of all the multiples of 3 or 5 below 1000 =',total)

#multiplesOf3or5()

'''
EXERCISE #2
WRITE A FUNCTION THAT TAKES A LIST AS A PARAMETER AND RETURNS A SECOND LIST COMPOSED OF ANY OBJECTS THAT APPEAR MORE
THAN ONCE IN THE ORIGINAL LIST 
-duplicates([1,2,3,6,7,3,4,5,6]) should return [3,6]
-what should duplicates(['cow','pig','goat','horse','pig']) return? 
	It should return ['pig']
'''
def duplicates(d_list):
	#check - Create a duplicate list to compare original list to
	#foundOne -Create a list to store duplicates
	check = []
	foundOne = []
	#iterate through original list. if item has already been added to list then add duplicate item into foundOne[]
	for i in d_list:
		if i in check:
			foundOne.append(i)
		else:
			check.append(i)
	print(foundOne)
#duplicates([1,2,3,6,7,3,4,5,6])
#duplicates(['cow','pig','goat','horse','pig'])

'''
WRITE A FUNCTION THAT TAKES A PORTION MARK AS INPUT AND RETURNS THE FULL CLASSIFICATION
	-convert_classification('U//FOUO') should return 'UNCLASSIFIED//FOR OFFICIAL USE ONLY'
	-convert_classification('S//REL TO USA, FVEY') should return 'SECRET//REL TO USA, FVEY'

	#HAD TO LOOK UP GOV CLASSIFICATION LEVELS#
		To indicate the appropriate classification level, the symbols "(TS)" for Top
		Secret, "(S)" for Secret, and "(C)" for Confidential will be used. Portions that do
		not meet the standards for classification shall be marked with "(U)" for
		Unclassified or "(U//FOUO)" for Unclassified
'''


#Split Portion Mark using split function taking '//' as delimeter
#find appropriate level rating and concat and print appropriate message assuming category is the same
#if there are category abbrevations that need to be expanded, would just run a check in each statement for shorthand version

def convert_classification(abbrev):
	abbrev = str.split(abbrev,'//')
	level = abbrev[0]
	civilian_message = ''
	category = abbrev[1]
	if(level == 'TS'):
		civilian_message = 'TOP SECRET'
		print(civilian_message+' '+category)
	elif(level == 'S'):
		civilian_message = 'SECRET'
		print(civilian_message+' '+category)
	elif(level == 'C'):
		civilian_message = 'CONFIDENTIAL'
		print(civilian_message+' '+category)

	else:
		civilian_message = 'UNCLASSIFIED'
		if(category=="FOUO"):
			print('UNCLASSIFIED//FOR OFFICIAL USE ONLY')
		else:
			print('UNCLASSIFIED')
	

#convert_classification('U//FOUO')
#convert_classification('S//REL TO USA, FVEY')