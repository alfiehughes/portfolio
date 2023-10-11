input = int(input("Please enter the number of the times table you would like to see:"))
count = 0
if input < 0:
    count = 12
    while count > -1:
        input = abs(input)
        result = count * input
        print(count, "x", input, "=", result)
        count = count - 1
else:
    while count < 13:
        result = count * input
        print(count, "x", input, "=", result)
        count = count + 1
