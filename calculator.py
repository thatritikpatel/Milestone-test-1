def add(x, y):
  """
  This function adds two numbers.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The sum of x and y.
  """
  return x + y

def subtract(x, y):
  """
  This function subtracts two numbers.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The difference of x and y.
  """
  return x - y

def multiply(x, y):
  """
  This function multiplies two numbers.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The product of x and y.
  """
  return x * y

def divide(x, y):
  """
  This function divides two numbers, handling division by zero.

  Args:
      x: The first number (dividend).
      y: The second number (divisor).

  Returns:
      The quotient of x and y, or an error message for division by zero.
  """
  if y == 0:
    return "Error: Division by zero"
  return x / y

# Example usage (optional)
if __name__ == "__main__":
  result = add(5, 3)
  print(f"5 + 3 = {result}")

  result = subtract(10, 2)
  print(f"10 - 2 = {result}")

  result = multiply(4, 6)
  print(f"4 * 6 = {result}")

  result = divide(12, 3)
  print(f"12 / 3 = {result}")

  result = divide(10, 0)
  print(result)
