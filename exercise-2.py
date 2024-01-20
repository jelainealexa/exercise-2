# Print the sum of the current number and the previous number

# Display message
print("Printing current and previous number sum in a range(10)")

# Iterate the first 10 numbers
for i in range(10):
    #Assign the current number to variable current_number
    current_number = i
    
    #Calculate the previous number by subtracting 1 from the current number
    previous_number = i - 1
    
    #Calculate the sum of current and previous numbers
    sum = current_number + previous_number

    #Display current number, previous number, and their sum
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum}")
