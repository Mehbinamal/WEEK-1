# Function To Count Unique Words and Their Frequencies
def countUniqueWords(f):
    uniqueWords = {}
    for data in f:
        words = data.strip().removesuffix('.').split()
        for word in words:
            if word in uniqueWords:
                uniqueWords[word] += 1
            else:
                uniqueWords[word] = 1
    return uniqueWords

#Printing Frequencies Function
def printDictionary(d):
    for key, value in d.items():
        print(f"{key}: {value}")


# Opening File
try:
    file = open('May-7/file', 'r')
    words = countUniqueWords(file) 
    printDictionary(words)
    file.close()
except FileNotFoundError:
    print("File Not Found")
