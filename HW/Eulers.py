def duplicates(x):
	dup={}
	result = []
	for i in x:
		dup[i] = dup.get(i,0)+1

	for i in dup.keys():
		if dup[i] > 1:
			result.append(i)

	return result

def duplicates2(x):
	dup = []
	for i in x:
		if x.count(i) and i not in dup:
			dup.append(i)
	return dup

def convert_classification(x):
	full_classfications = {'U//FOUO':'UNCLASSIFIED//FOR OFFICIAL USE ONLY','C//REL TO USA, FVEY':'CONFIDENTIAL//REL TO USA, FVEY','S//REL TO USA, FVEY':'SECRET//REL TO USA, FVEY','S//SI//REL TO USA, FVEY': 'SECRET//SI//REL TO USA, FVEY','TS//REL TO USA, FVEY':'TOP SECRET//REL TO USA, FVEY','TS//SI//REL TO USA, FVEY':'TOP SECRET//SI//REL TO USA, FVEY'}
	return full_classfications.get(x,'Unknown')




def main():
	multiples_3 = [i for i in range(3,1000,3)]
	multiples_5 = [i for i in range(5,1000,5)]

	multiples = set((multiples_3+multiples_5))
	sum(multiples)
	x = [1,2,3,6,4,,1,5,6,7,8,9,2,10]
	duplicates(x)











if __name__ == '__main__':
	main()