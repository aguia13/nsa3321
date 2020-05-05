class My_List(object):
	my_list = ['apples','milk','butter','orange juice']
	def __init__(self,snack='chocolate'):
		self.snack = snack
	def __str__(self):
		return 'My list: {}'.format(', '.join(self.my_list))
	def __repr__(self):
		return self.__str__()
	def in_my_list(self,item):
		if item in self.my_list:
			return 'Got it!'
		else:
			return 'Nope!'
	def snack_check(self):
		return self.snack in self.my_list


class caps_list(My_List):
	def in_my_list(self, item):
		#response = super(caps_list,self).in_my_list(item)
		response = My_List.in_my_list(self,item)
		return response.upper()

shouty = caps_list()
print(shouty.in_my_list('chocolate'))
print(dir(caps_list))



december = My_List()
december.my_list = december.my_list +['chocolate']

jan = My_List('apples')
print(jan.snack_check())

feb = My_List()
print(feb.snack_check())

