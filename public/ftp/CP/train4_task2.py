#19ucs182
#sagar mittal
#training4_task2

months={'00':"invalid",'01':"jan",'02':"feb",'03':"mar",'04':"apr",'05':"may",'06':"jun",'07':"jul",'08':"aug",'09':"sep",'10':"oct",'11':"nov",'12':"dec"}
a=[]
for i in range(5):
    a.append(input("enter date "))
    
for i in range(5):
    if(len(a[i])==10):
       d= int(a[i][0:2])
       mm=a[i][3:5]
       yyyy=a[i][6:10]
       print(d," ",months[mm]," ",yyyy)
       

