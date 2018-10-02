import random
import sys
row = int(sys.argv[1])
columns = int(sys.argv[2])
#adapted from https://stackoverflow.com/questions/40566675/how-to-make-a-board-in-python most code adjusted because of required sys.argv
def main():
    print("Board:\n")

    for i in range(row): 
        print('0'*columns) 

if __name__ == '__main__':
    main()
