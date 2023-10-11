sweets = int(input("How many sweets?"))
pupils = int(input("How many pupils?"))
perpupil = sweets // pupils
remainder = sweets % pupils
if perpupil == 1 and remainder == 1:
    print("Each pupil will get 1 sweet and there will be 1 sweet left over.")
elif perpupil == 1 and remainder != 1:
    print("Each pupil will get 1 sweet and there will be", remainder, "sweets left over.")
elif perpupil != 1 and remainder == 1:
    print("Each pupil will get", perpupil, "and there will be 1 sweet left over.")
else:
    print("Each pupil will get", perpupil, "sweets and there will be", remainder, "sweets left over.")
