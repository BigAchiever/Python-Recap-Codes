try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)

# Exited with exit code 0 is good

except ZeroDivisionError: # Another kind of error
    print("Age cannot be zero")
except ValueError:
    print("invalid Value")