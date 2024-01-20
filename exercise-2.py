# Print the sum of the current number and the previous number

# Display message
print("Printing current and previous number sum in a range(10)")

# Create a variable to start the loop from 0
previous_number = 0

# Iterate the first 10 numbers
for i in range(10):
    #Assign the current number to variable current_number
    current_number = i
    
    #Calculate the sum of current and previous numbers
    sum = current_number + previous_number

    #Display current number, previous number, and their sum
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum}")
    
    previous_number = current_number