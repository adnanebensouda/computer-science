def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    """Summarize the pizza we are about to make."""
    print("\Making a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)