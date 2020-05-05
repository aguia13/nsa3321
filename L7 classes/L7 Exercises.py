'''
Exercise 1-
Write a Query class that has the following attributes:
	classification
	justification
	selector
Provide default values for each attribute (consider using None).
Make it so that when you print it, iyou can display all of the 
attributes and their values nicely.
'''
class Query(object):
	def __init__(self,classification = None,justification=None,selector=None):
		self.classification = classification
		self.justification = justification
		self.selector = selector
	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}".format(self.classification,self.justification,self.selector)

'''
query1 = Query("TS//SI/REL TO USE, FVEY","Primary email address of Zendian Diplomat","ileona@stato.gov.zd")
print(query1)

Exercise 2

Make a RangedQuery class that inherits from Query and has additional attributes:
	begin date
	end date
For now, just make the dates of the form YYYY-MM-DD. Don't worry about date formatting or error checking for now.
Well talk about the datetime module and exception handling later.

Provide defaults for these attributes. Make sure you incorporate the Query Class's initializer into the RangedQuery initializer
Ensure the new class can also be printed nicely.

class RangedQuery(Query):
	def __init__(self,classification,justification,selector,begin,end):
		super(RangedQuery,self).__init__(classification,justification,selector)
		self.begin = begin
		self.end = end
	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}\nBegin Date: {3}\nEnd Date: {4}".format(self.classification,self.justification,self.selector,self.begin,self.end)

query2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat","10.254,18.162","2016-12-01","2016-12-15")
print(query2)


Exercise 3

Change the query class to accept a list of selectors rather than a single selector. Make sure you can still print everything OK.
'''
class RangedQuery(Query):
	def __init__(self,classification,justification,selector,begin,end):
		super(RangedQuery,self).__init__(classification,justification)
		self.selector = selector
		self.begin = begin
		self.end = end
	def __str__(self):
		return "Classification: {0}\nJustification: {1}\nSelector: {2}\nBegin Date: {3}\nEnd Date: {4}".format(self.classification,self.justification,self.selector,self.begin,self.end)

query2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat",["10.254.18.162","10.254.18.187"],"2016-12-01","2016-12-15")
print(query2)