magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That great magic show!")

message = "Hello python world!"
print(message)

stores = ['pizza hot', 'pizza mix', 'pizza go', 'kfc']

for store in stores:
    print("I like " + store)
print("i really love pizza")

animals = ['lion', 'tiger', 'eagle', 'bear', 'cat', 'dog']

for animal in animals:
    print(animal + " would make a great pet")
print("any of these animals would make a great pet!")

for value in range(1, 10):
    print(value)

numbers = list(range(1, 10))
print(numbers)
print("\n")
even_numbers = list(range(2, 11, 4))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

for numb in range(1, 21):
    print(numb)

for number in range(1, 101):
    print(number)

number_list = list(range(1, 101))
print(number_list)

print(min(number_list))
print(max(number_list))
print(sum(number_list))

"""finish the odd"""

for three in range(3, 31, 3):
    print(three)

cube_three = []
for value in range(1, 11):
    square = value**3
    cube_three.append(square)
print(cube_three)

squ = [value**3 for value in range(1, 16)]
print(squ)

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("here are the first players on my team:")
for names in players[:3]:
    print(names.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append('cano')
friends_food.append('ice cream')

print("my favorite food are:")
print(my_foods)

print("\nmy friend's favorite food are:")
print(friends_food)

print(friends_food[:3])
print(my_foods[1:-1])

pizza = stores
pizza_friend = pizza[:]

pizza.append('pizza fish')
pizza_friend.append('pizza white')

for piz in pizza:
    print("my favorite pizza are:" + piz)
print("\n")

for piz in pizza_friend:
    print("my friend pizza are:" + piz)
"""tuple Ex"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


print("\nthis the original dimension are:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,  100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


foods = ('pizza', 'burger', 'tacos', 'sushi', 'soup')

print("our food menu are:")
for food in foods:
    print(food)

print("\n")
cars = ['audi', 'bmw',  'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

"""it's end here"""

print("\n")
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("hold the anchovies!")
print("\n")
answer = 17
if answer != 42:
    print("that is not the correct answer. please try again!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

game_active = True

can_edit = False

print(game_active)

print(can_edit)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 19
if age >= 18:
    print("you are old enough to vote!")
"""Defines an integer addition function."""
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")

age = 12
if age < 4:
    print("Your admission cost is 0$.")
elif age < 18:
    print("Your admission cost is 5$.")
else:
    print("Your admission cost is 10$.")
print("\n")

age = 12

if age < 4:
    price = 0
elif age < 65:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + "\n")

requested_toppings = ['mushrooms', 'extra sheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra sheese' in requested_toppings:
    print("Adding extra sheese.")

print("\nfinished making your pizza!\n")

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra sheese' in requested_toppings:
    print("Adding extra sheese.")

print("Finished making your pizza!")

alien = ['green', 'yellow', 'red']

if 'green' in alien:
    print("you earn 5 point")
elif 'yellow' in alien:
    print("you pass")
elif 'red' in alien:
    print("you fail")

print("\n")

age = 64

if age <= 2:
    print("the person is baby")
elif age <= 4:
    print("the person is toddler")
elif age <= 13:
    print("the  person kid")
elif age <= 20:
    print("the person is teenager")
elif age <= 64:
    print("the person is an adult")
else:
    print("person is an elder")

print("\n")

favourite_fruits = ['banana', 'apple', 'orange', 'berry',]

if 'banana' in favourite_fruits:
    print("i really like banana!")
if 'orange' in favourite_fruits:
    print("i really like orange!")
if 'berry' in favourite_fruits:
    print("i really like berry!")
if 'apple' in favourite_fruits:
    print("i really like apple!")

print("\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra sheese']

for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_toppings + ".")

print("\nFinished making your pizza!\n")

"""using multiple lists"""

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra sheese']

requested_toppings = ['mushrooms', 'french fries', 'extra sheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

"""make list for five users"""

list = ['Eric', 'carter', 'admin', ' jack']

for lists in list:
    if 'admin' in lists:
        print("\nHello " + lists + " would you like to see a status report!")
    else:
        print("\nHello " + lists + " thank you for logging in again")