"""
class designed to represent an image as a Quad Tree.

Juan Flores
5/20/23
"""
from binary_matrix import *
from math import inf as infinity

class QuadTree:

    def __init__(self, depth: int=0, mean: int=0, size: tuple=(0,0), nw=None, ne=None, sw=None, se=None) -> None:
        self.depth = depth
        self.mean = mean
        self.size = size
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se


    def insert(self, bin_mat, depth = 0):
        self.depth = depth
        self.mat = bin_mat
        self.mean = matrix_mean(bin_mat)
        self.size = (len(bin_mat), len(bin_mat[0]))
        if not same_bits(bin_mat):
            self.nw, self.ne, self.sw, self.se = QuadTree(), QuadTree(), QuadTree(), QuadTree()
            for object, i in zip([self.nw, self.ne, self.sw, self.se], split_4(bin_mat)):
                object.insert(i, depth+1)
        

    def reconstruct_image(self, depth):
        if not self.nw or self.depth == depth:
            return self.mat
        else:
            return stitch_matrices(self.nw.reconstruct_image(depth), self.ne.reconstruct_image(depth), self.sw.reconstruct_image(depth), self.se.reconstruct_image(depth))

    def __str__(self):
        if self.nw:
            return f"{'+' * self.depth + ' ' * int(bool(self.depth))}(({self.depth}, {self.mean}, {self.size}))\n{str(self.nw)}{str(self.ne)}{str(self.sw)}{str(self.se)}"
        else:
            return f"{'+' * self.depth + ' ' * int(bool(self.depth))}(({self.depth}, {self.mean}, {self.size}))\n" 
        

if __name__ == "__main__":
    binary_file = 'test.txt'  # in coding rooms change it to "images/fisherman.txt"
    matrix = read_bin_matrix(binary_file)
    q_t = QuadTree()
    q_t.insert(matrix)
    print(q_t)

    # depth = infinity # why infinity?
    # rec_mat = q_t.reconstruct_image(depth) 
    # plot_bin_matrix(rec_mat)

    