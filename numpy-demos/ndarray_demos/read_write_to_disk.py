# encoding utf-8
import numpy as np
import unittest

x = np.array([23.23, 24.24])

bin_file = 'array.bin'
text_file = 'array.txt'

class ReadWriteBinaryFile(unittest.TestCase):

    def test_save(self):
        np.save(bin_file, x)

    def test_load(self):
        print(np.load(bin_file + '.npy'))

class ReadWriteTextFile(unittest.TestCase):


    def test_save(self):
        np.savetxt(text_file, X=x, delimiter=',')

    def test_load(self):
        print(np.loadtxt(text_file, delimiter=','))