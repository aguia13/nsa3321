'''
Exercise 1: Write a custom error and raise it if RangedQuery is created with dates not in the correct format.
'''
import re

class Query(object):
	def __init__(self,classification = None,justification=None,selector=None):
		self.classification = classification
		self.justification = justification
		self.selector = selector
	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}".format(self.classification,self.justification,self.selector)

class RangedQuery(Query):
	def __init__(self,classification,justification,selector,begin,end):
		super(RangedQuery,self).__init__(classification,justification)
		self.selector = selector	

		checkB = re.match("[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}",begin)				#Using Regular Expressions to check if date is in the YYYY/MM/DD
		checkE = re.match("[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}",end)		
		if(checkB==True):
			self.begin = begin
		else:
			self.begin = None
			print("Enter Beginning Date in the following format: YYYY/MM/DD")			
		if(checkE==True):
			self.end = end
		else:
			self.end = None
			print("Enter Beginning Date in the following format: YYYY/MM/DD")			
	

	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}\nBegin Date: {3}\nEnd Date: {4}".format(self.classification,self.justification,self.selector,self.begin,self.end)



def main():
	query2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat",["10.254.18.162","10.254.18.187"],"16-12-01","2016-12-15")


if __name__ == '__main__':
	main()