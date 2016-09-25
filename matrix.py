def printMatrix(matrix, size):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end = " ")
        print()
    print()


"""
Simple Sudoku Matrix
"""
class SSM():
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.sz = size - 1
        self.hsize = int(size ** 0.5)    # Half SIZE -- the square root of the size

    def printMatrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j], end = " ")
            print()
        print()

    def is_well_formed(self):
        setx = set(range(self.size+1))
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] not in setx:
                    return False
        return True



"""
Backtracking Sudoku Box
"""
class BSB(SSM):
    def __init__(self, matrix):
        self.matrix = matrix.matrix
        self.size = matrix.size
        self.sz = self.size - 1
        self.hsize = int(self.size ** 0.5)    # Half SIZE -- the square root of the size

        self.blueprint = [[False for j in range(self.size)] for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != 0:
                    self.blueprint[i][j] = True



    def solve(self):
        import copy
        c = copy.deepcopy(self.matrix)
        res = []
        direction = True #true = forward; false = backward
        i = j = 0
        while (True):
            if self.blueprint[i][j]:
                if direction:
                    if j == self.sz:
                        if i == self.sz:
                            res.append(copy.deepcopy(c))
                            c[i][j] = 0
                            direction = False
                            j -= 1
                            continue
                        i += 1
                        j = 0
                    else:
                        j += 1
                else:
                    if j == 0:
                        if i == 0: return res
                        j = self.sz
                        i -= 1
                    else:
                        j -= 1
            else:
                while (True):
                    c[i][j] += 1
                    if self.valid(i,j,c):
                        direction = True
                        if j == self.sz:
                            if i == self.sz:
                                res.append(copy.deepcopy(c))
                                c[i][j] = 0
                                direction = False
                                j -= 1
                                break
                            i += 1
                            j = 0
                        else:
                            j += 1
                        break
                    else:
                        if c[i][j] >= self.size:
                            direction = False
                            c[i][j] = 0
                            if j == 0:
                                if i == 0: return res
                                j = self.sz
                                i -= 1
                            else:
                                j -= 1
                            break







    """ Check if the last added number is valid """
    def valid(self, i, j, tmp_matrix):
        if tmp_matrix[i][j] > self.size:
            return False
        col_set = set() #COLumn SET
        col_cnt = 0  #COLumn added element CouNTer
        row_set = set() #ROW SET
        row_cnt = 0 #ROW CouNTer
        for l in range(self.size):
            col_elem = tmp_matrix[l][j]  #COLumn ELEMent
            if col_elem != 0:
                col_set.add(col_elem)
                col_cnt += 1
            row_elem = tmp_matrix[i][l]  #ROW ELEMent
            if row_elem != 0:
                row_set.add(row_elem)
                row_cnt += 1
        if len(col_set) != col_cnt or len(row_set) != row_cnt:
            return False

        blk_set = set() #BLocK SET
        blk_cnt = 0 #BLocK added element CouNTer
        ii = i // self.hsize * self.hsize
        jj = j // self.hsize * self.hsize
        for a in range(self.hsize):
            for b in range(self.hsize):
                blk_elem = tmp_matrix[ii+a][jj+b] #BLocK ELEMent
                if blk_elem != 0:
                    blk_set.add(blk_elem)
                    blk_cnt += 1
        if blk_cnt != len(blk_set):
            return False

        return True




"""
Special matrix
"""
class SMatrix():
    def __init__(self, matrix, size):
        self.size = size
        self.hsize = int(size ** 0.5)

        """ Initialize the blocks """
        self.blocks = [[0 for j in range(self.hsize)] for i in range(self.hsize)]
        """ Construct the blocks """
        for i in range(self.hsize):
            for j in range(self.hsize):
                block_matrix = [[0 for j in range(self.hsize)] for i in range(self.hsize)]
                for ii in range(self.hsize):
                    for jj in range(self.hsize):
                        block_matrix[ii][jj] = matrix.matrix[i*self.hsize+ii][j*self.hsize+jj]
                self.blocks[i][j] = SBlock(block_matrix, self.hsize)


    """ Display blocks to console """
    def display_blocks(self):
        for i in range(self.hsize):
            for j in range(self.hsize):
                self.blocks[i][j].display()





"""
Special Block
"""
class SBlock():
    def __init__(self, block_matrix, hsize):
        self.hsize = hsize
        self.bm = [[0 for j in range(self.hsize)] for i in range(self.hsize)]

        for i in range(self.hsize):
            for j in range(self.hsize):
                self.bm[i][j] = SCell(block_matrix[i][j], self.hsize)


    """ Display the block to console """
    def display(self):
        for i in range(self.hsize):
            for j in range(self.hsize):
                print(self.bm[i][j].value, end = " ")
            print()
        print()






"""
Special Cell
"""
class SCell():
    def __init__(self, value, hsize):
        self.hsize = hsize
        self.value = value
        candidates = range(hsize) if value == 0 else []
