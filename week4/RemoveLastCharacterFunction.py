def removelastcharacter():
    if len(word) > 1:
        removed = word[:-1]
        print(removed)
    else:
        print(word)


word = input("Please enter a string")
removelastcharacter()
