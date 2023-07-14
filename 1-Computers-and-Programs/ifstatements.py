p = input("Enter any principle amount")

t = input("Enter any time")


if(int(t) > 10):
    si=int(p)*int(t)*10/100
else:
    si=int(p)*int(t)*15/100

print("Simple Interest=", si)