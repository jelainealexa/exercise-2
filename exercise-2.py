# Print the sum of the current number and the previous number

print("Printing current and previous number sum in a range(10)")

for i in range(10):
    current_number = i
    previous_number = i - 1
    sum = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum}")
