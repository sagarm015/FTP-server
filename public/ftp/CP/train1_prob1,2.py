#questions from training 1
#programmer :sagar mittal ( 6th august 2019)
#problem 1
#final velocity will be zero
vel_final=0
vel_int = 100
g=float(input("enter value of g" ))
#third eq of motion 2as = v**2 - u**2
max_hieght = (vel_final**2 - vel_int**2)/(2*g)
print ("maximam height attained is ",max_hieght)

#problem 2
#time taken to reach max height
# using first eq of motion v=u + at
time1 = (vel_final - vel_int)/(-g)
#time2 (taken to reach ground from max height) = time 1
time2=time1
total_time = time1 + time2

print( " total time taken to reach ground aftr being thrown", total_time)


