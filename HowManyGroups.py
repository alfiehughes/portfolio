group = 24
total = int(input("How many students will there be?"))
fullgroups = total // group
remainder = total % group
print("There will be", fullgroups, "full groups, and a smaller left over group of", remainder, "students.")
