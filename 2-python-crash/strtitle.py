name = "Ada lovelace"

print(name.title())

print(name.upper())

print(name.lower())

first_name = "ada"

last_name = "lovelace"

full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")

print("python")

print("\tpython")

print("Languages:\nPython\nC\nJavascript")

print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_launguage = 'python '

print(favorite_launguage.rstrip())

massage = "Hello Eric, would you like to learn some Python today?"

print(massage)

age = 32

mess = "happy " + str(age) + "rd Birthday!"

print(mess)

motorcycles = ['honda', 'yamaha','suzuki']
motorcycles[0] = 'ducati'
motorcycles.append('gogo')
motorcycles.insert(0, 'alomi')
motorcycles.insert(3, 'balolo')
del motorcycles[0]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'suzuki'

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

motorcycles.append('kiya')

motorcycles.append('yamaha')

motorcycles.append('yakuza ninja')

print(motorcycles)

motorcycles.sort()
print(motorcycles)

motorcycles.sort(reverse=True)
print(motorcycles)

print("here is the original list:")
print(motorcycles)

print("\nhere is the sorted list:")
print(sorted(motorcycles))

print("\nhere is the original list again:")
print(motorcycles)

motorcycles.reverse()
print(motorcycles)

print(len(motorcycles))

for motorcycle in motorcycles:
    print(motorcycle)