import datetime
import time

time1 = time.localtime()
#[0:tm_year,1:tm_mon,2:tm_day,3:tm_hour,4:tm_min,5:tm_sec,6:tm_wday,7:tm_yday,8:tm_isdst]
hour=time1.tm_hour
minute = time1.tm_min
second = time1.tm_sec

if(hour<=5):
	print("You should be sleeping!")
elif(6<=hour&hour<=10):
	print("Good Morning!")
elif(11<=hour&hour<=14):
	print("How are those emails going?")
elif(15<=hour&hour<=17):
	print("Almost quitting time!")
