import random

def improve(input_list,missing):
	random_index = random.choice(list(range(len(input_list))))
	random_value = random.choice(missing)
	new_list = input_list[:]
	new_list[random_index] = random_value
	return new_list

def find_missing(input_list):
	missing = [x for x in list(range(1,10)) if x not in input_list]
	return missing

def one_to_nine(input_list,prev_missing=None):
	print(input_list)
	missing = find_missing(input_list)

	if prev_missing is None:
		return one_to_nine(input_list,missing)
	elif len(missing) == 0:
		return True
	elif len(missing) > len(prev_missing):
		return False
	else:
		possible_improvements = (improve(input_list,missing) for i in range(len(missing)))
		return any((one_to_nine(p,missing) for p in possible_improvements))




def main():
	one_to_nine([1,1,1,1,1,1,1,1,1])


if __name__ == '__main__':
	main()