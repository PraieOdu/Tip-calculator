print("Welcome to the tip calculator.")
T_bill = float(input("What was the total bill? "))
per_tip = float(input("What percentage tip would you like to give? 10,12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
per_tip_m = (per_tip / 100) + 1
T_bill_f = T_bill * per_tip_m
s_bill = round(T_bill_f / num_of_people,2)
print(f" Each person should pay: £{s_bill} ")
