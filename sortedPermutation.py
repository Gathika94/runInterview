import sys, getopt

def split(word):
    return [char for char in word]

def readFile(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines();
    for line in lines:
        word = line
        print('input : '+word)
        sortCharacters(word)



def sortCharacters(word):
    invalid =False
    numeric =[]
    upperCase = []
    lowerCase = []
    characters = split(word)
    if(len(characters)==0):
        print ("[Empty Input]\n")
        return
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
    if(invalid):
        print('[Invalid Input]\n')
    else:
        numeric.sort()
        upperCase.sort()
        lowerCase.sort()
        sortedArray=numeric+upperCase+lowerCase
        permutationArray = permute(sortedArray)
        output = ",".join(permutationArray)
        print(output+'\n')

def permute(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return lst
    else:
        permutedArray=[]
        for i in range(len(lst)):
            consideredCharacter=lst[i]
            otherCharacters = lst[:i]+lst[i+1:]
            for permutation in permute(otherCharacters):
                permutedArray.append(consideredCharacter+permutation)
        return permutedArray

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

    print('Input file :'+ inputfile+'\n')
    readFile(inputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
