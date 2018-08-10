# coding: utf-8
import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

fname_input = 'corpus81.txt'
fname_word2vec_out = 'vectors.txt'
fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'

word2vec.word2vec(train=fname_input, output=fname_word2vec_out, size=300, threads=4, binary=0)

with open(fname_word2vec_out, 'rt') as data_file:
    work = data_file.readline().split(' ')
    size_dict = int(work[0])
    size_x = int(work[1])

    dict_index_t = OrderedDict()
    matrix_x = np.zeros([size_dict, size_x], dtype=np.float64)

    for i, line in enumerate(data_file):
        work = line.strip().split(' ')
        dict_index_t[work[0]] = i
        matrix_x[i] = work[1:]

io.savemat(fname_matrix_x300, {'matrix_x300': matrix_x})
with open(fname_dict_index_t, 'wb') as data_file:
    pickle.dump(dict_index_t, data_file)
