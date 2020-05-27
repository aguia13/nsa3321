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

def one_to_nine(input_list):
	print(input_list)
	missing = find_missing(input_list)

	if len(missing) == 0:
		return input_list
	else:
		new_list = improve(input_list, missing)
		return one_to_nine(new_list)


def main():
	print(one_to_nine([1,1,1,1,1,1,1,1,1]))
	return


if __name__ == '__main__':
	main()