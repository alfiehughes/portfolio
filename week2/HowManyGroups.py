students = int(input("How many students?"))
group = int(input("Required group size?"))
groups = students // group
remainder = students % group
if groups == 1 and remainder == 1:
    print("There will be 1 group with 1 student left over.")
elif groups == 1 and remainder != 1:
    print("There will be 1 group with", remainder, "students left over.")
elif groups != 1 and remainder == 1:
    print("There will be", groups, "groups with 1 student left over.")
else:
    print("There will be", groups, "groups with", remainder, "students left over.")
