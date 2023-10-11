def integercheck():
    if num in range(1, 101):
        print("True")
    else:
        print("False")


num = int(input("Please enter a number"))
integercheck()
