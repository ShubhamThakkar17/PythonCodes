#print("Apple", "Mango", "Banana", sep="-",end=":")
#print("Thank You")

name = input("What's your name?")
print(f"Hello, {name}")

with open("users.txt", 'a') as file:
    file.write(f"{name}\n")

