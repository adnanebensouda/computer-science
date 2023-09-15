import pizza
from target import greet_users

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)