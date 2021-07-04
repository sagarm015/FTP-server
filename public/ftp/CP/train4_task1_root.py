upper =3
lower=2
for i in range(10000):
    mid = (lower +upper)/2
    f_upper= 2*upper**3-3*upper**2+5*mid-17
    f_mid= 2*mid**3-3*mid**2+5*mid-17
    if f_upper*f_mid>=0 :
       upper=mid
    else:
       lower=mid



print("(",upper,lower,")")
    
