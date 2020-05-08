import re
import operator

'''
Add a method to your 'Ranged Query' class to allow instances of the 
class to be sorted by 'start date'
'''


class Query(object):
	def __init__(self,classification = None,justification=None,selector=None):
		self.classification = classification
		self.justification = justification
		self.selector = selector
	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}".format(self.classification,self.justification,self.selector)

class RangedQuery(Query):
	def __init__(self,classification,justification,selector,start_date,end_date):
		super(RangedQuery,self).__init__(classification,justification,selector)
		
		for i in start_date:
			print(i)

		checkB = str.split(start_date,'-')
		checkE = str.split(end_date,'-')
		s_B = str(checkB[0])
		s_E = str(checkE[0])

		if(int(checkB[0])>1900 and int(checkB[0]) <= 2020):
			self.start_date = start_date
		else:
			self.start_date = None
			raise Exception("Enter Start Date in the following format: YYYY-MM-DD")

		if(int(checkE[0])>1900 and int(checkB[0]) <= 2020):
			self.end_date = end_date
		else:
			self.end_date = None
			raise Exception("Enter End Date in the following format: YYYY-MM-DD")			
	

	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}\nBegin Date: {3}\nEnd Date: {4}".format(self.classification,self.justification,self.selector,self.start_date,self.end_date)



def main():
	query1 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat","10.254.18.162","2016-12-01","2016-12-15")
	query2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat",["10.254.18.162","10.254.18.187"],"2016-12-01","2016-12-15")
	query2.startDateSort()

if __name__ == '__main__':
	main()