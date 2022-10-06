# for x in range(4):  # after the inner loop is completed this loop will run
#     for y in range(3):  # This is the inner loop which will run till 2 iterations
#         print(x, y)

# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print('x'*item)


# Alternate method for printing patters x
numbers = [1, 1, 1, 1, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += ' x'
    print(output)