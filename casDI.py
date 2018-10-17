from casadi import *
import numpy

g = numpy.load("sparse.npy")
a = DM(g)
print(a)
nb, rowperm, colperm, rowblock, colblock, coarse_rowblock, coarse_colblock = a.sparsity().btf()

print("number of blocks: ", nb)
print("rowperm: ", rowperm)
print("colperm: ", colperm)
print("restored:")
print(a[rowperm,colperm])
print("rowblock: ", rowblock)
print("colblock: ", colblock)
print("coarse_rowblock: ", coarse_rowblock)
print("coarse_colblock: ", coarse_colblock)