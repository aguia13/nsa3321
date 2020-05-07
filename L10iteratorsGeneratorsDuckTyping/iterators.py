
class NonFactorIterable(object):
	def __init__(self,*args):
		self.avoid_multiples = args
		self.x = 0
	def __next__(self):
		self.x += 1
		while True:
			if self.x > 200:
				raise StopIteration
			for y in self.avoid_multiples:
				if self.x % y == 0:
					self.x += 1
					break
				else:
					return self.x
	def __iter__(self):
		return self

silent_fizz_buzz = NonFactorIterable(3,5)
print(silent_fizz_buzz)


class Squares(object):
	def __init__(self,limit=200):
			self.limit = limit
			self.x = 0
	def __next__(self):
		self.x += 1
		if self.x > self.limit:
			raise StopIteration
		return(self.x-1)**2
	def __getitem__(self,idx):
		#initialize counter to 0
		self.x = 0
		if not isinstance(idx,int):
			raise Exception("Only integer index arguments are accepted")
		while self.x < idx:
			self.__next__()
		return self.x**2
	def __iter__(self):
		return self	