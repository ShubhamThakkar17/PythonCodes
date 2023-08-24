amount = int(input("Enter the amount in multiples of hundred: "))

if(amount%100 == 0):
    print("Valid input\nAmount Processing.....")
else:
    print("Invalid Input\nRetry and Enter amount in multiples of hundred")    
    
n500 = amount//500
amount %= 500
n200 = amount//200
amount %= 200
n100 = amount//100
amount %= 100

print(f"500 x {n500} = {n500 * 500}")
print(f"200 x {n200} = {n200 * 200}")
print(f"100 x {n100} = {n100 * 100}")


