check = float(input('enter amount here:'))
numpeople = float(input('How many people are paying?:'))
tip = float(input("tip percentage:"))
total = check *((tip/100)+1)
cpp = total/numpeople
print(f"price per person ins {cpp:.2f}")