import sys, getopt

def split(word):
    return [char for char in word]

def readFile(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines();
    for line in lines:
        print("nl")
        print(line)
        word = line
        sortCharacters(word)



def sortCharacters(word):
    invalid =False
    numeric =[]
    upperCase = []
    lowerCase = []
    characters = split(word)
    print(characters)
    for char in characters:
        if char.isdigit():
            numeric.append(char)
        elif char.isupper():
            upperCase.append(char)
        elif char.islower():
            lowerCase.append(char)
        else:
            invalid=True
            break
    print(numeric)
    print(upperCase)
    print(lowerCase)
    numeric.sort()
    upperCase.sort()
    lowerCase.sort()
    sortedArray=numeric+upperCase+lowerCase
    print(sortedArray)


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('sortedPermutation.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sortedPermutation.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    print('Input file is "', inputfile)
    readFile(inputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
