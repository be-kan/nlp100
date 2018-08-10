# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'
fname_input = 'family.txt'
fname_output = 'family_out.txt'


def cos_sim(vec_a, vec_b):
    norm_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if norm_ab != 0:
        return np.dot(vec_a, vec_b) / norm_ab
    else:
        return -1


with open(fname_dict_index_t, 'rb') as data_file:
    dict_index_t = pickle.load(data_file)

keys = list(dict_index_t.keys())
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

with open(fname_input, 'rt') as data_file, open(fname_output, 'wt') as out_file:
    for line in data_file:
        cols = line.split(' ')
        try:
            vec = matrix_x300[dict_index_t[cols[1]]] - matrix_x300[dict_index_t[cols[0]]] + matrix_x300[dict_index_t[cols[2]]]
            dist_max = -1
            index_max = 0
            result = ''
            for i in range(len(dict_index_t)):
                dist = cos_sim(vec, matrix_x300[i])
                if dist > dist_max:
                    index_max = i
                    dist_max = dist

            result = keys[index_max]

        except KeyError:
            result = ''
            dist_max = -1

        print('{} {} {}'.format(line.strip(), result, dist_max), file=out_file)
        print('{} {} {}'.format(line.strip(), result, dist_max))
