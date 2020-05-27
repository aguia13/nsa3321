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

def score(input_list):
	missing = find_missing(input_list)
	return(len(missing),input_list)

def best_scored(scored_list):
	lowest = 100
	best_list = []

	for x in scored_list:
		score = x[0]
		input_list = x[1]

		if score < lowest:
			lowest = score
			best_list = input_list
	return best_list

def one_to_nine(input_list):
	print(input_list)
	missing = find_missing(input_list)

	if len(missing) == 0:
		return input_list
	else:
		possible_improvement = [improve(input_list,missing) for i in range(len(missing))]
		scored_improvement = [score(i) for i in possible_improvement]
		best_list = best_scored(scored_improvement)
		return one_to_nine(best_list)


def main():
	print(one_to_nine([1,1,1,1,1,1,1,1,1]))
	return


if __name__ == '__main__':
	main()