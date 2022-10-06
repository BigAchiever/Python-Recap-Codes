# Mutable - List in mutable and can change
# Immutable - Tuple is immutable and cannot change

grocery = ["Harpic", "vin bar", "deo", "bhindi", 66]
print(grocery)  # will prin the list

num = [2, 3, 4, 1, 4, 55, 3, 5, 22]
num.sort()
# num.reverse()
print(num[:])  # it will print al the elements in the list
#  Slicing always returns a list --- Slicing means string k sath khelna
print(num[1:5:2])

# Using append function - Will add an element you want to add in the list at the END.
num.append(9)
print(num)

# Will insert a new value in the list at whatever index you want
num.insert(3, 10)
print(num)

num.pop()  # To pop the number at last of the list
print(num)

#  TUPLES
tp = (1,2,3,4,5,2)
tp.insert(2,4)  # WIll throw an error cuz tuples cannot change.
print(tp)

# to swap two to elements or more
a= 1
b = 3
a,b=b,a
print(a,b)



