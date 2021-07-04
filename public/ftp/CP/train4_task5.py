#19ucs182
#sagar mittal
#training 4 task 5
days_month={ 00:"invalid",01:31,02:28,03:31,04:30,05:31,06:30,07:31,08:31,09:30,10:31,11:30,12:31}

date=input("enter a date")
dd=int(date[0:2])
mm=int(date[3:5])
yyyy=date[6:10]
minus=93-dd
minus=minus-days_month[mm-1]-days_month[mm-2]
dd=days_month[mm-3]-minus
print(dd,mm-3,yyyy)






