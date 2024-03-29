#!/usr/bin/python3.6
# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

random_arr = np.random.randn(100)

plt.plot(random_arr)
plt.savefig('rs')
