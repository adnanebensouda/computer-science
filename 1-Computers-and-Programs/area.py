from math import sqrt

print("1-Area of square")
print("2-Area of rectangle")
print("3-Area of triangle")

c = input ("Enter any Choice: ")

if(int(c)==1):
    s = input("enter any side of the square: ")
    a= int(s)*int(s)
    print("Area=", end=" ")
    print(int(a))

elif(int(c)==2):
    l=input("enter length: ")
    b=input("enter breadth: ")
    a=int(l)*int(b)
    print("Area=", end=" ")
    print(int(a))

elif(int(c)==3):
    x=input("enter first side triangle: ")
    y=input("enter second side of triangle: ")
    z=input("enter third side of triangle: ")
    s= 4.5
    b=s*(s-int(x))*(s-int(y))*(s-int(z))
    A=sqrt(b)
    two_numbers = "{:.2f}".format(A)
    print("Area=", end=" ")
    print(two_numbers)
else:
    print("Wrong input")