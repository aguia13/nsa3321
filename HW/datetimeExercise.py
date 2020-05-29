'''
How long before christmas?
how many seconds since you were born?
what is the average nmber of days between Easter and Christmas for the years 2000 - 2999?
What day of the week does Christmas fall on this year?

You get a intercepted email with a POSIX timestamp of 1435074325. the email is from the leader of a zendian extremist group and
says that there will be an attack o nthe Zendian capitol in 14 hours. When will the attack occur? (assume tz is same as kabul)
'''
import datetime
from datetime import timedelta

def butchers(year):
	a = year %19
	b = year /100
	c = year %100
	d = b/4
	e = b%4
	f = (b+8)/25
	g = (b-f+1)/3
	h = (19*a+b-d-g+15)%30
	i = c/4
	k = c%4
	l = (32_2*e+2*i-h-k)%7
	m = (a+11*h+22*l)/451
	easter = (h+l-7*m+114)/31
	p = (h+1-7*m+114)%31
	date = (p+1)
	return date

def main():
	xmas = datetime.datetime(2020,12,25)
	now = datetime.datetime.now()
	bday = datetime.datetime(1994,11,8)

	since_birth = now - bday


	print("There are ",xmas-now," hours left until Christmas")
	print("It has been",since_birth.total_seconds(),"seconds since I was born")


	print(butchers(2020))
	




if __name__ == '__main__':
	main()