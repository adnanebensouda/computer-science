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
    s=(int(x)+int(y)+int(z))/2
    A=((int(s)-int(x))*(int(s)-int(y))*(int(s)-int(z))**0.5)
    print("Area=", end=" ")
    print(int(A))
else:
    print("Wrong input")