from math import sqrt,pow

x= input("enter any number")

y =sqrt(int(x))  #without using math
a =pow(int(x),2) #without using math

print("Square Root value", float(y))
print("Square value", float(a))

def si(p,r,t):
    return(p*r*t)
print(si(1000,2,10))


def SI(p,r=10,t=5):
 return(p*r*t/100)

print(SI(10000))

