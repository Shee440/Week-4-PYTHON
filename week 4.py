# Combined File Read, Write & Error Handling Program 🖋️🧪

filename = input("Enter the filename to read: ")

try:
    # Try to open and read the input file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify content (convert to uppercase)
    modified_content = content.upper()

    # Create a new file with "_modified" suffix
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\nSuccess! Modified content has been written to '{new_filename}'")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
