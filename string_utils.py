def reverse_string(text):
  """
  This function reverses a string.

  Args:
      text: The string to be reversed.

  Returns:
      The reversed string.
  """
  return text[::-1]

def capitalize_first(text):
  """
  This function capitalizes the first letter of a string.

  Args:
      text: The string to be capitalized.

  Returns:
      The string with the first letter capitalized.
  """
  return text.capitalize()

def all_caps(text):
  """
  This function converts a string to uppercase.

  Args:
      text: The string to be converted.

  Returns:
      The string in uppercase.
  """
  return text.upper()

def all_lowercase(text):
  """
  This function converts a string to lowercase.

  Args:
      text: The string to be converted.

  Returns:
      The string in lowercase.
  """
  return text.lower()

def remove_whitespace(text):
  """
  This function removes all whitespace characters from a string.

  Args:
      text: The string from which to remove whitespace.

  Returns:
      The string with whitespace removed.
  """
  return text.replace(" ", "")

# You can add more string manipulation functions here

# Example usage (optional)
if __name__ == "__main__":
  original_text = "Hello, world!"
  reversed_text = reverse_string(original_text)
  capitalized_text = capitalize_first(original_text)
  uppercase_text = all_caps(original_text)
  lowercase_text = all_lowercase(original_text)
  no_whitespace = remove_whitespace(original_text)

  print(f"Original: {original_text}")
  print(f"Reversed: {reversed_text}")
  print(f"Capitalized first: {capitalized_text}")
  print(f"All caps: {uppercase_text}")
  print(f"All lowercase: {lowercase_text}")
  print(f"No whitespace: {no_whitespace}")  
