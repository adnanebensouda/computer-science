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
    