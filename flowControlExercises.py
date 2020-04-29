#Change the loop below so that it prints numbers 1 to 10
#for i in range(9):
	#print(i)
'''
for i in range(1,11):
	print(i)
'''
#Using a for loop and enumerate, write a function getindex(string, character) to recreate the string method .index
#"skyscraper".index('c')
#4
#getindex("skyscraper",'c')
'''
def getindex(block,cell):
	index = 0
	char = ''
	for i in enumerate(block):
		index = i[0]
		char = i[1]
		if(cell==char):
			print(index)
			break
		#print(index,char)
getindex("Flow",'o')
'''
#Using the shout function from the first set of basic exercises, write a shout_word(sentence) function that takes a string argument
#and "shouts each word on its own line"
#shouts_words("Everybody likes bananas")
#EVERYBODY!
#LIKES!
#BANANAS!
'''
def shout_words(sentence):
	yell = str.split(sentence," ")		
	for i in enumerate(yell):
		print(str.upper(i[1])+"!")
shout_words("you are the worst")
'''
#Write an extract_longer(length, sentence) function that takes a sentence and word length, then returns a list of the sentence's words that 
#exceed the given length. If no words match the length, return false
def extract_longer(length,sentence):
	count = 0
	sentence = str.split(sentence)
	r_list = ""

	for x in enumerate(sentence):
		if(len(x[1])>length):
			r_list =r_list+x[1]+','
	if(len(r_list)==0):
				print('false')
			
	print(r_list)		
extract_longer(3,"The cow jumped over the moon")