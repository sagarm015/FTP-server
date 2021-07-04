Python 3.7.3 (default, Apr  3 2019, 19:16:38) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> g=9.8
>>> ua1=0
>>> ub1=0
>>> ua2=10*(2**0.5)
>>> ua2
14.142135623730951
>>> #let total time be t
>>> #time taken for first ball to hit the ground 10*(2**0.5)
>>> ua2=100*(2**0.5)
>>> #adding distance travelled by second ball and distance travelled by first ball after hitting ground=1000
>>> #distance by first ball (after hitting ground= ua2*(t-10*(2**0.5)) - 0.5*g*(t-10*(2**0.5))**2
>>> #distance travelled by second ball after being released by 5 seocnd
>>> #using second eq of motion s=ut = 1/2at**2
>>> #distance will be = 0.5*g*(t-5)**2
>>> #adding the two distances we will get total height =1000
>>> # 1000= s1+s2
>>> # 1000=  {ua2*(t-10*(2**0.5)) - 0.5*g*(t-10*(2**0.5))**2} + {0.5*g*(t-5)**2}
>>> t=7750/((400**0.5)-100)
>>> t
-96.875
>>> t=7750/((400*(2**0.5))-100)
>>> t
16.64213562373095
>>> 
