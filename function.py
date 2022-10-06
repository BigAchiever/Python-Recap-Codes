# We can take a few lines of code that have a specific purpose and then put them in a function.

def greet_user(first_name, last_name):  # Defining parameter inside a function
    # name = "Danish"   # We can define here or below when we call the function
    print("Hi there!", first_name, last_name)


#  Parameters are the words that we define inside a function.
#  Arguments are the actual form of information which is stored in parameters.
# These are positional arguments where positions matters of arguments


print("Start")
# greet_user("Danish")
greet_user("Danish", "Ali")  # Works as same as the name = "Danish"
# We cannot pu positional arguments after keyword arguments
greet_user("Hasan", last_name="Hashir")
# greet_user(first_name="Hasan", "Hashir") # Wrong

greet_user("Hasan", "Hashir")  # If there was no function we would have to repeat the print name line twice
# greet_user("Hashir", "Hasan") # with change in position output changes
# Keyword arguments-------
calc_cost(total=50, shipping=5, discount=0.5)
print("Finish")


#  Return functions of python
def square(number):
    return number * number
    # print(number * number) # By default python will return None at last because of no return


# result = square(3)
print(square(3))
