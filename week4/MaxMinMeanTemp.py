import statistics

templist = []
check = True

while check:
    temp = input("Please enter a temperature followed by C. To finish inputting just press enter:")
    if temp == "":
        check = False
    else:
        temp = temp[:-1]
        templist.append(temp)

maxtemp = max(templist) + 'C'
mintemp = min(templist) + 'C'
templist = [float(n) for n in templist]
meantemp = sum(templist) / len(templist)
print("The maximum temperature is", maxtemp)
print("The minimum temperature is", mintemp)
print("The mean temperature is", round(meantemp, 2), "C")
