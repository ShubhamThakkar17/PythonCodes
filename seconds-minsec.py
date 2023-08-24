import time

seconds = int(input("Enter seconds: "))

convert = time.strftime("%M:%S", time.gmtime(seconds))

print(convert)