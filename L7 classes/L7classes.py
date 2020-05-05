'''
function vs method:
	name = "Mark"
	len(name) - returns int, length of obj
	name.upper() - changes name

name is an instance of the str type.
name is an obj of that type(str)
obj is wrapper around data & functionality related to data ie methods
methods are defined in a class definition
methods live inside of class instead of outside of it
'''
class Person(object):
	species = "Homo sapiens"
	def __init__(self, name="Unknown",age=18):
		self.name = name
		self.age = age
	def talk(self):
		return "Hello, my name is {}.".format(self.name)
	def __str__(self):
		return "Name: {0},Age: {1}".format(self.name,self.age)
	def __repr__(self):
		return "Person('{0}',{1}".fomat(self.name,self.age)
	def __eq__(self,other):
		return self.age == other.age

class Student(Person):
	bedtime = 'Midnight'
	def do_homework(self):
		import time
		print("I need to work")
		time.sleep(5)
		print("Did I just fall asleep?")

class Employee(Person):
	def __init__(self,name,age,employer):
		super(Employee,self).__init__(name,age)
		self.employer = employer
	def talk(self):
		talk_str = super(Employee,self).talk()
		return talk_str + " I work for {}".format(self.employer)

class StudentEmployee(Student,Employee):
	pass

nobody = Person()
print(nobody.species)
print(nobody.talk())

tyler = Student("Tyler",19)
print(tyler.species)
print(tyler.talk())
tyler.do_homework()

fred = Employee("Fred Flinstone",55,"Slate Rock and Gravel Company")
print(fred.talk())

ann = StudentEmployee("ann",58,"Family Services")
print(ann.talk())
print(ann)
#bill = StudentEmployee("bill",20) #crashes because no employer is passed