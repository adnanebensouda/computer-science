def greet_user(username):
    """Display a simple greeting."""
    print("Hello " + username.title() + "!")


greet_user('jesse')

"""first ex"""


def display_message():
    print("\ni learn how to create function")


display_message()


def favorite_book(title):
    print("my favorite book is " + title.title() + ".")


favorite_book('python Crack course')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

"""second ex"""

print("\n")


def make_shirt(text, size):
    print("A " + size + " shirt will be printed with the message: " + text)


make_shirt('hello world', 'medium')
print("\n")
make_shirt(size='large', text='i love python')

print("\n")


def describe_city(city, country='morocco'):
    print(city + " is in " + country)


describe_city('Reykjavik', 'Iceland')
describe_city('antwerp', 'belgium')
describe_city('tanger')
