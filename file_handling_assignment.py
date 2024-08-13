def create_and_write_file():
    try:
        
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("And this is the third line with some more text.\n")
        print("File created and initial content written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while creating or writing to the file: {e}")
    finally:
        print("Create and write operation completed.")

def read_file():
    try:
        
        with open('my_file.txt', 'r') as file:
            contents = file.read()
        print("File content:")
        print(contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Read operation completed.")

def append_to_file():
    try:
        
        with open('my_file.txt', 'a') as file:
            file.write("Appending a fourth line of text.\n")
            file.write("Here's a fifth line with more details.\n")
            file.write("And the sixth line for good measure.\n")
        print("Additional lines appended.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Append operation completed.")

if __name__ == '__main__':
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()  
