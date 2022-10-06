faulty_calc_var = {"56*5": "540", "45+19": "61", "56-18": "31"}
num1 = (input("Enter the 1st number :"))
print("Which operation you want to perform :")
operation = (input())
num2 = (input("Enter the second number :"))
string = num1+operation+num2
if string in faulty_calc_var:
    print(faulty_calc_var[string])
elif operation == "+":
    print(int(num1) + int(num2))
elif operation == "*":
    print(int(num1) * int(num2))
elif operation == "-":
    print(int(num1) - int(num2))
elif operation == "/":
    print(int(num1) / int(num2))