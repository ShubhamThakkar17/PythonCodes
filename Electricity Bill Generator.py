import sys
units = int(input("Number of units: "))
#/ first 100 = 4/U
#  next 200 = 5/U
# beyond that = 10/U
# if bill > 1000 INR add 10% surcharge
# Add 18% GST on final bill/#
if units<0:
    sys.exit("Error - Invalid Input")
    
if (units<=100):
    amount = units * 4
    bill = amount
elif(units<=300):
    amount = (100*4) + (units - 100)*5
    bill = amount
else:
    amount = (100*4) + (200*5) + (units-300)*10
    bill = amount
    
if(amount>1000):
    bill = amount + (amount*10)/100

total = bill + (bill*18)/100

print("Your bill for",units, " Units is Rs", total)