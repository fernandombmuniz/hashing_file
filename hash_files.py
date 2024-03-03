import hashlib

def calculate_hash(file_path):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # Open the file in binary mode and iterate over it in blocks of data
    with open(file_path, "rb") as f:
        while True:
            # Read a block of data from the file
            block = f.read(4096)
            # If there are no more blocks, exit the loop
            if not block:
                break
            # Update the hash object with the read block
            sha256.update(block)
    # Return the SHA-256 hash of the file as a hexadecimal string
    return sha256.hexdigest()

if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the file: ")
    try:
        # Calculate the hash of the file and display the result
        file_hash = calculate_hash(file_path)
        print(f"The SHA-256 hash of the file '{file_path}' is: {file_hash}")
    except FileNotFoundError:
        # Display an error message if the file is not found
        print("File not found.")