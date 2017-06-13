# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
直方图
'''

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000) # 生成10000个正态分布点
plt.hist(v, bins=100, normed=1)
plt.title('Matplot hist')
plt.show()

# Numpy的histogram函数
# |bin1-n1|bin2-n2|bin3-n3|
(n, bins) = np.histogram(v, bins=100, normed=True)
plt.plot(0.5 * (bins[1:] + bins[:-1]), n)
plt.title('Numpy histogram')
plt.show()
