#function to take user input
def writeToFile(filename):
    with open(filename, 'w') as file:
        while True:
            user_input = input("Enter text (type 'stop' to finish): ")
            if user_input.lower() == 'stop':
                break
            file.write(user_input + '\n')

#function to read from file
def readFromFile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nContent read from file:")
        print(content)
    except FileNotFoundError:
        print("File not found.")

# main
filename = 'May-7/user_input.txt'
writeToFile(filename)
readFromFile(filename)
