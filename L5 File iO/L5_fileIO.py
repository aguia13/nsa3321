'''
Copy sonnet from -redacted: I will be using Shakespear's 18th- and paste into sonnet.txt

EXERCISE 1- WRITE A FUNCITON CALLED file_capitalize() that takes an input file name and an output file name,
then writes each word from the input file with only the first letter capitalized to the output file. 
Remove all the punctuation except apostrophe

capitalize('sonnet.txt','sonnet_caps.txt') => capitalized words written to sonnet_caps.txt
'''
import io



def capitalize(i_sonnet,o_sonnet):
	punctuation = ['.',',','?','!',':',';']	#create word bank to check if char is punctuation
	new_sonnet = open(o_sonnet,'r+')
	first = 1
	with open(i_sonnet) as my_sonnet:
		for line in my_sonnet:			#for every line in txt file
			line = str.lower(line)		#default line to lowercase char
			for i in line:				#for every char in line if it's punctuation, skip but set 'first' = 0 as it's no longer first char
										#could add conditional statement to account for in case punctuation if first char
				if(i in punctuation):
					first = 0
					continue
				elif(first==1):			#if its first char then uppercase it, write to file, set 'first' to 0
					new_sonnet.write(str.upper(i))
					first = 0
				else:					#it is not punctuation or first char, so write to file
					new_sonnet.write(i)

#capitalize('sonnetXVIII.txt','test.txt')
'''
EXERCISE 2 - Write a function called file_word_count() that takes a file name and returns a dictionary
containing the counts for each word. Remove all the punctuation except apostrophe. Lowercase all the words.
'''
def file_word_count(i_sonnet):
	#init a dictionary
	words ={}
	punctuation = ['.',',','?','!',':',';']
	with open (i_sonnet) as my_sonnet:
		for line in my_sonnet:			#loop through each line and set default to lowercase
			line = str.lower(line)
			spaced = str.split(line," ")#split each line with ' ' delimeter to get individual words

			for i in spaced:			#loop through every word in sentence/line.
				if(i in punctuation):
					continue 
				elif(i in words):		#if word is already in dict then increment count + 1
					words[i] += 1
				else:
					words.update({i:1})#else word isn't in dict so add it to dict and set count to 1
	print(words)
#file_word_count('sonnetXVIII.txt')
'''
EXTRA CREDIT - Write the counts dictionary to a file, one key:value per line
'''
def export_word_count(i_sonnet):
	punctuation = ['.',',','?','!',':',';']	#create punctuation list to compare against
	words={}								#words dict init
	new_sonnet = open('dictCount.txt','w')	#file that word count is being written to
	with open(i_sonnet) as my_sonnet:
		for line in my_sonnet:				#iterate through each line in txt file
			line = str.lower(line)			#default to lowercase
			spaced = str.split(line," ")	#split words with ' ' delimeter

			for i in spaced:				#iterate through each word per sentence
				if(i in words):				#add to dict and update count if word is already present
					words[i] +=1
				else:
					word = ""
					for j in i:				#iterate through each char in word and check to see if its punctuation
						if(j in punctuation):
							break			
						else:				#if not then continue building word 
							word = word+j
					words.update({word:1})	#once every char is iterated, add built word to dict

	for keys in words:
		new_sonnet.write(keys+':'+str(words[keys])+'\n')

export_word_count('sonnetXVIII.txt')
