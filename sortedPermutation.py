import sys, getopt


def readFile(filename):
    file = open(filename, 'r')
    for line in file:
        print("nl")
        print(line)


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
