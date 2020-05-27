
def nth_fib(n):
	if n<1:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return(nth_fib(n-2)+nth_fib(n-1))


def fib(n, seq=[]):
	if len(seq) == n:
		return seq
	elif len(seq) == 0:
		return fib(n,[1])
	elif len(seq) == 1:
		return fib(n,[1,1])
	else:
		next_value = seq[-2] + seq[-1]
		return fib(n,seq+[next_value])


def main():
	#print(nth_fib(10))
	#print(fib(5))



if __name__ == '__main__':
	main()