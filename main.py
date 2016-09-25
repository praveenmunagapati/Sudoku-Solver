#!/usr/bin/python3

from functions import *
from matrix import *



def main():
    m = read_matrix(get_filename())
    m.printMatrix()

    bsb = BSB(m)


    solution = bsb.solve()

    print("Number of solutions found:", len(solution))

    for i in range(len(solution)):
        printMatrix(solution[i],m.size)


    #sm = SMatrix(m, m.size)
    #sm.display_blocks()



if __name__ == "__main__":
    main()
