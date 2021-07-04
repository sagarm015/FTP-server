#19ucs182
#sagar mittal
#training 4 task3
months={'00':"invalid",'01':"jan",'02':"feb",'03':"mar",'04':"apr",'05':"may",'06':"jun",'07':"jul",'08':"aug",'09':"sep",'10':"oct",'11':"nov",'12':"dec"}
days_month={ '00':"invalid",'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
a=[]
for i in range(9):
    a.append(input("enter date "))
count=1    
for i in range(9):
    d= int(a[i][0:2])
    mm=a[i][3:5]
    m=int(a[i][3:5])
    yyyy=int(a[i][6:10])
    if yyyy<1900 or yyyy>2100:
       count=0
    elif m<1 or m>12 :
       count=0
    elif d<1 or d>days_month[mm]:
       count==0
    if count==1:
       print(d," ",months[mm]," ",yyyy)
    if count==0:
       print(a[i]," invalid date")
       

       
      
            
