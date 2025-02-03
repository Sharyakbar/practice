import os

def create_file(filename, content="Hello, World!"):
    """ Create a file and write content to it. """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")

def read_file(filename):
    """ Read content from a file. """
    try:
        with open(filename, 'r') as file:
            print(f"Reading from '{filename}':")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

def append_to_file(filename, content):
    """ Append content to an existing file. """
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Content added to '{filename}' successfully.")

def delete_file(filename):
    """ Delete a file. """
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"Error: '{filename}' does not exist.")

if __name__ == "__main__":
    filename = 'example.txt'
    content = "Hello, World!"
    additional_content = "\nThis is an appended line."

    # File operations
    create_file(filename, content)
    read_file(filename)
    append_to_file(filename, additional_content)
    read_file(filename)
    delete_file(filename)
