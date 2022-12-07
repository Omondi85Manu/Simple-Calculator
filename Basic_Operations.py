# This program implements a simple calculator

# Define the main function
def main():
  # Prompt the user for the operation to perform
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  
  # Read the user's input
  choice = input("Enter choice (1/2/3/4): ")
  
  # Convert the input string to an integer
  choice = int(choice)
  
  # Prompt the user for the operands
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  
  # Perform the selected operation
  if choice == 1:
    result = num1 + num2
  elif choice == 2:
    result = num1 - num2
  elif choice == 3:
    result = num1 * num2
  elif choice == 4:
    result = num1 / num2
  else:
    # If the user entered an invalid choice, display an error message
    print("Invalid input")
    return
  
  # Display the result of the calculation
  print(num1, ",", num2, ":", result)
  
# Call the main function
main()

