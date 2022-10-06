List = [1, 2, 5, 6, 2, 7, 9, 3]
# print(max(List))
# num = List[0]
# for i in List:
#     if i > num:
#         num = i
# print(num)

# 2D Lists----------------------------------
matrix = [
    [1, 2, 3],  # two-dimensional list representation
    [4, 5, 6],
    [7, 8, 9]
]

# matrix[0][1] = 20  #  changing the value at that index
print( matrix[0][1])  # printing the value at that index

for items in matrix:
    for values in items:
        print(values)

# Program to remove duplicates
numbers = [ 1, 1, 2, 4, 5, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#  removing duplicates using dict
numbers = [1, 2, 1, 2, 3, 4]
numbers = list(dict.fromkeys(numbers))
print(numbers)