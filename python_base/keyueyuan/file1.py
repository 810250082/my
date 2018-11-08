import pandas as pd
from pandas import Series, DataFrame
import numpy as np


df = DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
                'key2':['one', 'two', 'one', 'two', 'one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)
                })

grouped = df['data1'].groupby([df['key1'], df['key2']])
means = grouped.mean()
#grouped=df['data1'].groupby(df['key1'])
#means = grouped.mean()

#
# data = DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
# data.icol(0)
a = 1
