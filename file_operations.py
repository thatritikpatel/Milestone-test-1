def read_file(filename):
  """
  This function reads the contents of a file.

  Args:
      filename: The path to the file to read.

  Returns:
      The contents of the file as a string, or None if an error occurs.
  """
  try:
    with open(filename, 'r') as file:
      return file.read()
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

def write_file(filename, content):
  """
  This function writes content to a file, overwriting any existing content.

  Args:
      filename: The path to the file to write to.
      content: The data to write to the file (string).
  """
  try:
    with open(filename, 'w') as file:
      file.write(content)
    print(f"Data written to file: {filename}")
  except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")

def append_to_file(filename, content):
  """
  This function appends content to a file.

  Args:
      filename: The path to the file to append to.
      content: The data to append to the file (string).
  """
  try:
    with open(filename, 'a') as file:
      file.write(content)
    print(f"Data appended to file: {filename}")
  except (IOError, OSError) as e:
    print(f"Error appending to file: {e}")
