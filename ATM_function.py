def calculate_denominations(amount):
    if amount <= 1000:
        num_notes_100 = 1
        amount -= 100
    else:
       num_notes_100 = 5
       amount -= 500

    num_notes_2000 = amount // 2000
    amount %= 2000

    num_notes_500 = amount // 500
    amount %= 500

    num_notes_200 = amount // 200
    amount %= 200
    
    num_notes_100 += amount // 100
    amount %= 100

    # Print the denominations
    print(f"Denominations for {amount}:")
    print(f"2000 x {num_notes_2000} = {num_notes_2000 * 2000}")
    print(f"500 x {num_notes_500} = {num_notes_500 * 500}")
    print(f"200 x {num_notes_200} = {num_notes_200 * 200}")
    print(f"100 x {num_notes_100} = {num_notes_100 * 100}")


# Get the amount from the user
amount = int(input("Enter the amount: "))
calculate_denominations(amount)
