import unittest

import h5py
import numpy as np


class H5pyTest(unittest.TestCase):


    def test_write(self):
        
        f = h5py.File("/tmp/info.h5", 'w')
        f.create_dataset("data", shape=(10, 20))
        a = np.random.rand(10, 20)
        f["data"][:] = a
        f.close()
        self.assertEquals(1,1)

    def test_read(self):
        f = h5py.File("/tmp/info.h5", 'r')
        print(list(f.keys()))
        for x in f.keys():
            data = f[x]
            print(data.shape)
        self.assertEquals(1,1)