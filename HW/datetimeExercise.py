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
from pytz import timezone

def easter(year):
	#BUTCHERS ALG	
	a = year %19
	b = year //100
	c = year %100
	d = (19*a + b - b // 4 -((b-(b+8) // 25+1) //3) +15) %30
	e = (32+2 * (b%4) +2 *(c//4) -d -(c%4)) %7
	f = d + e - 7*((a+11 * d+22*e) //451) + 114
	month = f // 31
	day = f % 31 + 1
	return(date(year,month,day))

def avgCalc(b_year,e_year):
	if(type(b_year) != int or type(e_year) != int):
		print("Please enter a valid year")
	else:
		avgDays = 0

		for i in range(b_year,e_year,1):
			iEaster = easter(i)
			xmas = datetime.date(i,12,25)
			dayDiff = xmas-iEaster
			avgDays += dayDiff.days
		return int(avgDays/1000)	

def whenXmas(day):
	if(day ==0):
		print('Monday')
	elif(day == 1):
		print('Tuesday')
	elif(day == 2):
		print('Wednesday')
	elif(day == 3):
		print('Thursday')
	elif(day == 4):
		print('Friday')
	elif(day == 5):
		print('Saturday')
	elif(day == 6):
		print('Sunday')
	else:
		print('Enter a valid day of the week')			




def main():
	xmas = datetime.datetime(2020,12,25)
	now = datetime.datetime.now()
	bday = datetime.datetime(1994,11,8)

	since_birth = now - bday


	print("There are ",xmas-now," hours left until Christmas")
	print("It has been",since_birth.total_seconds(),"seconds since I was born")

	print(avgCalc(2000,2999))
	whenXmas(xmas.weekday())

	attackTime = 1435074325

	utcTime = datetime.datetime.utcfromtimestamp(attackTime)



if __name__ == '__main__':
	main()