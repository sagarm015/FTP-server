population=0
baby =1
month=0
adults=0
while month<10:
    month= month+1
    adults=baby
    baby=population
    population=baby+adults
    
basket = [ "orange","banana","apple"]
price={"orange":30,"banana":20,"apple":50,"hghggh":88}
cost=0
for i in basket:
    cost = cost +price[i]
    
# print ("total cost is ",cost)

a=0
b=1
c=0
for i in range(10):
    a=b
    b=c
    c=a+b
    print(c)


    
    
    
    
