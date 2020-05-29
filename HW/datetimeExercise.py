'''
How long before christmas?
how many seconds since you were born?
what is the average nmber of days between Easter and Christmas for the years 2000 - 2999?
What day of the week does Christmas fall on this year?

You get a intercepted email with a POSIX timestamp of 1435074325. the email is from the leader of a zendian extremist group and
says that there will be an attack o nthe Zendian capitol in 14 hours. When will the attack occur? (assume tz is same as kabul)
'''
import datetime
from datetime import date, timedelta

def easter(year):
	a = year %19
	b = year //100
	c = year %100
	d = (19*a + b - b // 4 -((b-(b+8) // 25+1) //3) +15) %30
	e = (32+2 * (b%4) +2 *(c//4) -d -(c%4)) %7
	f = d + e - 7*((a+11 * d+22*e) //451) + 114
	month = f // 31
	day = f % 31 + 1
	return(date(year,month,day))

def avgCalc(days):
	numYears = len(days)
	total = 0
	for i in range(numYears):
		total += days[i].days
	return(total/1000)



def main():
	xmas = datetime.datetime(2020,12,25)
	now = datetime.datetime.now()
	bday = datetime.datetime(1994,11,8)

	since_birth = now - bday


	print("There are ",xmas-now," hours left until Christmas")
	print("It has been",since_birth.total_seconds(),"seconds since I was born")
	
	avgDays = []


	for i in range(2000,3000):
		iEaster = easter(i)
		xmas = datetime.date(i,12,25)
		avgDays.append(xmas-iEaster)


	avgCalc(avgDays)



if __name__ == '__main__':
	main()