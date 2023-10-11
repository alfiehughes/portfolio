def upperlower():
    lower = 0
    upper = 0
    for x in word:
        if x.islower():
            lower = lower + 1
        else:
            upper = upper + 1
    print("The number of lowercase characters is:", lower)
    print("The number of uppercase characters is:", upper)


word = input("Please enter a string")
upperlower()
