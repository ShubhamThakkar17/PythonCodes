cities = ["Ahemdabad","Bengluru","Chennai","Delhi","Gwalior","Hyderabad","Imphal","Jameshdpur","Kolkata"]
x = input("Letter: ")

for city in cities:
    if city.startswith(x):
        print(city)