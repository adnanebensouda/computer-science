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


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print("\n" + musician + "\n")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician + "\n")


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'handrix', age='27')
print(musician)


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# this is an infinite loop!

while True:
    print("\nPlease tell me you name :")
    print("enter 'q' at any time to quit")
    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

"""third ex"""


def city_country(city, country):
    c_country = city + ", " + country
    return c_country


n_country = city_country('Tanger', 'morocco')
n_count = city_country('antwerp', 'belgium')
n_countr = city_country('paris', 'french')
print(n_country)
print(n_count)
print(n_countr + "\n")


def make_album(first_name, last_album):
    artist = {'first': first_name, 'last': last_album}
    return artist


artists = make_album('Radio head', 'The Bends')
ar_twists = make_album('Kanye West', 'Graduation')
art_lists = make_album('Blur', 'Modern Life Is Rubbish')
print(artists)
print(ar_twists)
print(art_lists)


def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks is not None:
        album['tracks'] = num_tracks
    return album


# Example function calls
album1 = make_album('Radiohead', 'The Bends', 12)  # Includes number of tracks
album2 = make_album('Kanye West', 'Graduation')  # No number of tracks provided
album3 = make_album('Blur', 'Modern Life Is Rubbish', 14)  # Includes number of tracks

print(album1)
print(album2)
print(album3)


def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks is not None:
        album['tracks'] = num_tracks
    return album


while True:
    print("\nEnter album information (or 'q' to quit):")
    artist = input("Enter artist name: ")

    if artist.lower() == 'q':
        break  # Exit the loop if the user enters 'q'

    title = input("Enter album title: ")

    album = make_album(artist, title)
    print("Album information:")
    print(album)

"""from here"""

print("\n")


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print("\n")

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.

print("\nThe following models have been printed:")

for completed_model in completed_models:
    print(completed_model)

"""from here second function"""

print("\n")


def print_models(unprinted_designs, completed_models):
    """
     Simulate printing each design, until none are left.
     Move each design to completed_models after printing.
     """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)