#display all numbers where previous value is greater
number = [4, 7, 6, 8, 2, 1, 3]

for i in range(1, len(number)):
  if number[i] < number[i - 1]:
    print(number[i])
