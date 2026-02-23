# This is a tip calculator that asks for the bill, how many ways it's being split, and the tip %, then it does calculations with it, and prints output of the tip, bill, and split
bill = float(input("What's the damage? "))
peoplecount = float(input("How many ways are we splitting the bill? "))
percenttip = float(input("What is the tip percent? "))

tip = (bill/100)*percenttip
billtip = bill + tip
billsplit = billtip/peoplecount

print(f'You are tipping ${round(tip, 2)}, '
      f'The full bill plus tip is ${round(billtip, 2)}, '
      f'each person must pay: ${round(billsplit, 2)}')