def calculator():
  """
  Performs basic arithmetic operations based on user input.
  """

  try:
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
      result = num1 + num2
    elif operation == '-':
      result = num1 - num2
    elif operation == '*':
      result = num1 * num2
    elif operation == '/':
      if num2 == 0:
        print("Error: Division by zero!")
        return  # Exit the function to avoid the error
      result = num1 / num2
    else:
      print("Invalid operation. Please enter +, -, *, or /.")
      return  # Exit if the operation is invalid

    print(f"{num1} {operation} {num2} = {result}")

  except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
  except Exception as e: # Catch other potential errors
      print(f"An unexpected error occurred: {e}")
# Run the calculator
calculator()

