templist = []
check = True

while check:
    temp = input("Please enter a temperature followed by C. To finish inputting just press enter:")
    if temp == "":
        check = False
    else:
        temp = temp[:-1]
        templist.append(temp)

templist = [float(n) for n in templist]
meantemp = sum(templist) / len(templist)
print("The maximum temperature is", max(templist), 'C')
print("The minimum temperature is", min(templist), 'C')
print("The mean temperature is", round(meantemp, 2), 'C')
