#19ucs182
#sagar mittal
#training 4 task 4
a=[]
b=[0,0,0,0,0,0,0,0,0,0]
days_month={ '00':"invalid",'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}

 
for i in range(10):
    a.append(input("enter date "))

for j in range(10):
    d= int(a[i][0:2])
    mm=a[i][3:5]
    m=int(a[i][3:5])
    yyyy=int(a[i][6:10])
    if yyyy<1900 or yyyy>2100:
        b[j]=1
    elif m<1 or m>12 :
        b[j]=1
    elif d<1 or d>days_month[mm]:
        b[j]=1





    
small=a[0]
if b[1]==0:
    if(int(a[1][6:10])<int(small[6:10])):
         small=a[1]
    elif(int(a[1][6:10])==int(small[6:10])):
         if(int(a[1][3:5])<int(small[3:5])):
              small=a[1]
         elif(int(a[1][3:5])==int(small[3:5])):
              if(int(a[1][0:2])<int(small[0:2])):
                    small=a[1]
if b[2]==0:
   if(int(a[2][6:10])<int(small[6:10])):
        small=a[2]
   elif(int(a[2][6:10])==int(small[6:10])):
        if(int(a[2][3:5])<int(small[3:5])):
              small=a[2]
        elif(int(a[2][3:5])==int(small[3:5])):
              if(int(a[2][0:2])<int(small[0:2])):
                    small=a[2]
if b[3]==0:
   if(int(a[3][6:10])<int(small[6:10])):
        small=a[3]
   elif(int(a[3][6:10])==int(small[6:10])):
        if(int(a[3][3:5])<int(small[3:5])):
              small=a[3]
        elif(int(a[3][3:5])==int(small[3:5])):
              if(int(a[3][0:2])<int(small[0:2])):
                   small=a[3]

if(int(a[4][6:10])<int(small[6:10])):
     small=a[4]
elif(int(a[4][6:10])==int(small[6:10])):
     if(int(a[4][3:5])<int(small[3:5])):
           small=a[4]
     elif(int(a[4][3:5])==int(small[3:5])):
             if(int(a[4][0:2])<int(small[0:2])):
                 small=a[4]

if(int(a[5][6:10])<int(small[6:10])):
     small=a[5]
elif(int(a[5][6:10])==int(small[6:10])):
     if(int(a[5][3:5])<int(small[3:5])):
           small=a[5]
     elif(int(a[5][3:5])==int(small[3:5])):
             if(int(a[5][0:2])<int(small[0:2])):
                 small=a[5]

                 
if(int(a[6][6:10])<int(small[6:10])):
     small=a[6]
elif(int(a[6][6:10])==int(small[6:10])):
     if(int(a[6][3:5])<int(small[3:5])):
           small=a[6]
     elif(int(a[6][3:5])==int(small[3:5])):
             if(int(a[6][0:2])<int(small[0:2])):
                 small=a[6]

                 
if(int(a[7][6:10])<int(small[6:10])):
     small=a[7]
elif(int(a[7][6:10])==int(small[6:10])):
     if(int(a[7][3:5])<int(small[3:5])):
           small=a[7]
     elif(int(a[7][3:5])==int(small[3:5])):
             if(int(a[7][0:2])<int(small[0:2])):
                 small=a[7]

if(int(a[8][6:10])<int(small[6:10])):
     small=a[8]
elif(int(a[8][6:10])==int(small[6:10])):
     if(int(a[8][3:5])<int(small[3:5])):
           small=a[8]
     elif(int(a[8][3:5])==int(small[3:5])):
             if(int(a[8][0:2])<int(small[0:2])):
                 small=a[8]

if(int(a[9][6:10])<int(small[6:10])):
     small=a[9]
elif(int(a[9][6:10])==int(small[6:10])):
     if(int(a[9][3:5])<int(small[3:5])):
           small=a[9]
     elif(int(a[9][3:5])==int(small[3:5])):
             if(int(a[9][0:2])<int(small[0:2])):
                 small=a[9]

print("the smallest date is ",small)
















                 
                 

                 
                 
                 
                 
                 

                    
