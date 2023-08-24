def count_multiples(n, x):
    count = 0
    for num in range(1, x + 1):
        if num % n == 0:
            count += 1
    return count

# Example usage
n = int(input("Enter the number whose multiples you want to display: "))
x = int(input("Enter upperbound range: "))
result = count_multiples(n, x)
print(f"The number of multiples of {n} between 1 and {x} is: {result}")
