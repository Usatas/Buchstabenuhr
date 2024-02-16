import os

def remove_dir(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Remove each file
    for file in files:
        print(f"Remove file: {file}")
        os.remove(directory + '/' + file)
    
    # Remove the directory itself
    os.rmdir(directory)


if __name__ == "__main__":
    files = os.listdir()
    for file in files:
        print(file)
    print('end')