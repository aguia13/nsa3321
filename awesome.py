
class Awesome(object):
	def __init__(self,awesome_thing):
		self.thing = awesome_thing
	def __str__(self):
		return "{0.thing} is awesome!!!".format(self)

def cool(group):
	return "Everything is cool when you're part of {0}".format(group)

if __name__ == '__main__':
	a = Awesome("Everything")
	print(a)
