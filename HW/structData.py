from csv import DictReader
from datetime import datetime

def average(numbers):
	if len(numbers) == 0:
		return 0.0
	return sum(numbers)/float(len(numbers))	

def get_year_week(record):
	dt = datetime.strptime(record['Date'],'%d-%b-%y')
	return (dt.year,dt.isocalendar()[1])


def get_averages(data):
	avgs = {}

	for year_week, closes in data.items():
		avgs[year_week] = average(closes)
	return avgs

def weekly_summary(reader):
	weekly_data = {}

	for record in reader:
		year_week = get_year_week(record)

		if year_week not in weekly_data:
			weekly_data[year_week] = []

			weekly_data[year_week].append(float(record['Close']))

	return get_averages(weekly_data)



def file_weekly_summary(infile_name):
	with open (infile_name,'r') as infile:
		return weekly_summary(DictReader(infile))

def print_weekly_summary(weekly_data):
	for year_week in reversed(sorted(weekly_data.keys())):
		year = year_week[0]
		week = year_week[1]
		avg = weekly_data[year_week]
		print('Year {year}, Week {week}, Average Close {avg:.2f}'.format(year=year,week=week,avg=avg))


def main():
	data = file_weekly_summary('aapl.csv')
	print_weekly_summary(data)

	return

if __name__ == '__main__':
	main()