var1 = "Hello World"
var2 = 22
var3 = 33.6
# Whe we add two strings then it is known as Concatenation.
print(var2 + var3)
print(type(var1))
print(100 * var1)
print(str(int(var2) + int(var3)))

# Inputting number from user scenario
print("Enter the number")
inp = input()  # The number you will enter will store as a string in variable inp.
# So you cannot change or perform arithmetic calculations afterward.
print("The number you entered is", inp)
# print("The number you entered is", inp + 1000)  # Will throw error! CUz it cannot Concatenate of add string with an
# integer.


# To solve this issue we have come up with a solution called typecasting
print("You entered the number and its some is", int(inp)+100)