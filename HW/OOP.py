from csv import DictReader
import io

class Symbol(object):
	def __init__(self,name,input_file):
		self.name = name
		self.input_file = input_file
		self.daily_data = {}
		
		try:
			with open(input_file,'r') as data:
				for line in data:
					record = str.split(line,",")
					self.daily_data[record[0]] = [record[1],record[2],record[3],record[4],record[5]]
					#print(record)
		except:
			return self.daily_data

	def data_for_date(self,date_str):
		if date_str in self.daily_data:
			print(self.daily_data[date_str])

		else:
			return {}








def main():
	s1 = Symbol('AAPL','aapl.csv')
	print(s1.data_for_date('18-Feb-16'))
	#print(s1.data_for_date('18-Feb-20'))
	
	#s2 = Symbol('AAPL','aaple.csv')


if __name__ == '__main__':
	main()