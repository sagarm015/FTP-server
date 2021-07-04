Python 3.7.3 (default, Apr  3 2019, 19:16:38) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5*4 +3
23
>>> 5+4*3
17
>>> 5/4+3
4.25
>>> 5+4/3
6.333333333333333

>>> 5*6/4
7.5
>>> 50/6*5
41.66666666666667
>>> 3+6/2
6.0
>>> 3/6+2
2.5
>>> 2**3**2
512
>>> #right to left
>>> 2+-3
-1
>>> #unary has highest precedence
>>> #checking float answers
>>> 5/2
2.5
>>> 5//2
2
>>> 5.0/2
2.5
>>> 5.0//2
2.0
>>> 2**3.0
8.0
>>> 2**-3
0.125
>>> #round function
>>> round(3*9.8,2)
29.4
>>> round(3*9.8,15)
29.400000000000002
>>> #using input
>>> time=input("please give start time ")
please give start time 3
>>> start_t= int(time) #conersion
>>> end_t=int(input("enter end time "))
enter end time 5
>>> g= float(input("provide vlaue for g/n"))
provide vlaue for g/n 9.8
>>> print ("g is",g)
g is 9.8
>>> #calculating value of pie using  a sequence
>>> #num_n=2*n -1
>>> #frac-n= n**2/(num_(n+1) + frac_(n+1))
>>> #assuming frac_10 to be zero
>>> frac_9=9**2/(17+0)
>>> frac_8= 2**2/(15+frac_9)
>>> frac_7 =7**2/(13+frac_8)
>>> 
>>>  frac_9=9**2/(19+0)
 
SyntaxError: unexpected indent
>>>  frac_9=9**2/(17+0)
 
SyntaxError: unexpected indent
>>> frac_9 =2
>>> frac_9 = (9**2)/(19+0)
>>>  frac_8= 2**2/(17+frac_9)
 
SyntaxError: unexpected indent
>>> frac_8= 2**2/(17+frac_9)
>>> frac_7 =7**2/(13+frac_8)
>>> frac_7 =7**2/(11+frac_8)
>>> frac_6= 6**2/(9 + frac_7)
>>> frac_8=8**2/(17+frac_9)
>>> frac_5 =5**2/(7+frac_6)
>>> frac_4=4**2/(5+frac_6)
>>> frac_4=4**2/(5+frac_5)
>>> frac_3=3**2/(3+frac_4)
>>> frac_2=2**2/(1+frac_3)
>>> frac_2
1.4487757014880265
>>> 
