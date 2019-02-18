# encode utf-8

import unittest
import matplotlib.pyplot as plt
from movie_data_analysis.data_clean import *

# %matplotlib inline
# get_ipython().run_line_magic('matplotlib', 'inline')
# print(ratings.hist(column='rating', figsize=(15, 10)))
# ratings.hist(column='rating', figsize=(15, 10))
ratings.boxplot(column='rating', figsize=(15, 20))
# plt.figure()
# plt.plot(ratings.hist(column='rating', figsize=(15, 10)).data)
# plt.legend()
#
plt.show()
