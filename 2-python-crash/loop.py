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
        print("\nHello " + lists + " thank you for logging in again\n")

users = ['google', 'youtube', 'twitter', 'yahoo', 'linkdin']

if users:
    for user in users:
        print(user)

else:
        print("we need to find some users!")

print("\n")

current_users = ['jhon']

new_users = ['adnane']

for current_user in current_users:
    if current_user in new_users:
        print("that the username is available")
    else:
        print("the person will need to enter a new username")


"""make this ex another time"""
ordinal_n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_n:
        print(str(ordinal_number) + "th")
print("\n")
alien_0 = {'color': 'green', 'points': '5'}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)

alien_0['x_position'] = 0

alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("the alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("the alien is " + alien_0['color'] + ".")

print("\n")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_positon: " + str(alien_0['x_position']))

print(alien_0['speed'])

alien_0['speed'] = 'fast'

print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']

print(alien_0)

favourite_languages = {
    'jen': 'python',
    'sraha': 'C',
    'edward': 'reby',
    'phil': 'python',
}

print("sarah's favorite language is " + favourite_languages['sraha'].title() + ".")

person = {
    'first_name': 'jhon',
    'last_name': 'berzok',
    'age': 27,
    'city': 'new york'
}
print("\n")
print("my name is " + person['first_name'] + " " + person['last_name'] + " i have " + str(person['age']) + " year's old i'm from " + person['city'])

print("\n")
favorite_number = {
    'zack': '0634797291',
    'jhon': '0637201932',
    'carter': '0638729171'
}

print("zack favorite number is " + favorite_number['zack'] + ".")
print("jhon favorite number is " + favorite_number['jhon'] + ".")
print("carter favorite number is " + favorite_number['carter'] + ".")

"""finish glossary"""
print("\n")
glossary = {
    'sort': 'listing items',
    'set': 'give you non duplicate values',
    'if': 'condition',
    'list': 'list of data',
    'for': 'looping'
}

print("sort is " + glossary['sort'] + "\n" + "set is " + glossary['set'] + "\nif " + glossary['if'] + "\nlist " + glossary['list'] + "\nfor " + glossary['for'])


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for k, v in user_0.items():
    print("\nKey: " + k + "\nValue: " + v)

print("\n")

for n, l in favourite_languages.items():
    print(n.title() + "'s favorite language is " + l.title() + ".")
print("\n")

for n in favourite_languages.keys():
    print(n.title())

friends = ['phil', 'sraha']

print("\n")

for name in favourite_languages.keys():
    print(name)
    if name in friends:
        print("Hi " + name.title() + " I see your favorite language is " + favourite_languages[name].title() + "!")

    if 'erin' not in favourite_languages.keys():
        print("\nErin, please take our poll!")

for name in sorted(favourite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")
print("\n")
for name in favourite_languages.keys():
    print(name.title() + " thank you for taking the poll.")

print("\n")

print("The following langauge have been mentioned:")
for l in favourite_languages.values():
    print(l)
print("\n")
for l in set(favourite_languages.values()):
    print(l)

print(glossary)

for k, v in glossary.items():
    print(" i learn " + k.title() + " and it's mean " + v.title())
print("\n")
river = {
    'nile': 'egypt',
    'dead sea': 'lebanon',
    'atlantis': 'spain',
}

for k, v in river.items():
    print(k.title() + " runs through " + v.title())
print("\n")
print(favourite_languages.keys())
friends = ['sasha', 'leran', 'micheal', 'phil', 'sraha']
print("\n")
for name in favourite_languages.keys():
    if name in friends:
        print("thank you for taking the poll " + name)
    else:
        print("\nyou have invition to take the poll " + name)
print("\n")
alien_0 = {
    'color': 'green',
    'points': 5
}
alien_1 = {
    'color': 'yellow',
    'points': '10'
}
alien_2 = {
    'color': 'red',
    'points': '15'
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n")
# make an empty list for sorting aliens.

aliens = []

# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show 3 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# replace the 3 yellow with red
for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens:

for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.

print("Total number of aliens: " + str(len(aliens)))

# store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra sheese'],
}

# summarize the order.

print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tlocation: "+ location.title())

"""make the ex here ok"""

"""input and while true"""

"""remove comment to work
message = input("Tell me something, and i will repeat it back to you: ")
print(message)"""


"""remove comment to work
name = input("please enter you name:")
print("Hello, " + name + "!")"""

prompt = "if you tell us who you are, we can personalize the messages you see."
"""prompt += "\nWhat is your first name? 
name = input(prompt)
print("\nHello, " + name + "!")"""


"""remove comment to work
age = input("How old are you? ")
print(age)"""

"""height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou tall enough to ride!")
else:
    print("\nYou'll be to ride when you're a little older.")"""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finish quit"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 2:
    current_number += 1
    if current_number % 2 == 1:
        continue
    print(current_number)

x = 1
while x <= 5:
    print(x)
    x += 1

# start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)

    #Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in  confirmed_users:
        print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # Store the response in the dictionary:
    responses[name] = response

    # find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete. show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

