import os
from matrix import *

IN_DIR = "input/"	#input directory
FILE_NAME = "16_1.txt"
AUTO_FILENAME = False
EXTENSION = ".txt"



""" Open the input file """
def get_filename():
    if (AUTO_FILENAME):
        print ("AUTO_FILENAME [OK]\n")
        f = open(IN_DIR + FILE_NAME, 'r')
    else:
        print ("Enter the file name (without '.txt' extension):", end = "")
        fileName = input()
        path = IN_DIR + fileName + EXTENSION
        
        if ( os.path.isfile(path) ):
            f = open(path, 'r')
        else:
            raise AssertionError("THE SPECIFIED FILE PATH DOES NOT EXIST!")
    return f



""" Read the matrix from file f """
def read_matrix(f):
    """ Put the content of the file into a matrix """
    f.seek(0,0)
    size = int(f.readline());
    matrix = [[0 for x in range(size)] for x in range(size)]    # define a matrix of zeros

    for i in range(size):
        l = f.readline()
        t = l.split(" ")
        for j in range(size):
            matrix[i][j] = int(t[j])

    x = SSM(matrix, size)
    if not x.is_well_formed():
        raise AssertionError("Bad matrix input!")
    return SSM(matrix, size)



if __name__ == "__main__":
    main()
