# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'
fname_input = './wordsim353/combined.tab'
fname_output = 'combined_out.tab'


def cos_sim(vec_a, vec_b):
    norm_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if norm_ab != 0:
        return np.dot(vec_a, vec_b) / norm_ab
    else:
        return -1


with open(fname_dict_index_t, 'rb') as data_file:
        dict_index_t = pickle.load(data_file)

matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

with open(fname_input, 'rt') as data_file, open(fname_output, 'wt') as out_file:
    header = True
    for line in data_file:
        if header is True:
            header = False
            continue

        cols = line.split('\t')

        try:
            dist = cos_sim(matrix_x300[dict_index_t[cols[0]]], matrix_x300[dict_index_t[cols[1]]])

        except KeyError:
            dist = -1

        print('{}\t{}'.format(line.strip(), dist), file=out_file)
