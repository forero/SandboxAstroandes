#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np


#Lectura de imagen
img = plt.imread('descarga2.jpg') #Abro imagen

img_red = img[:,:,0]

n_row = len(img_red[:,0])

n_col = len(img_red[0,:])

combinations = []
for i in range(n_row//2):
    for j in range(n_col//2):
        a = img_red[i*2:i*2+2,j*2:j*2+2].flatten()
        pos = list(np.argsort(a))
        combinations.append(pos)

count = {}
for c in combinations:
    s = ''.join([str(i) for i in c])
    try:
        count[s] += 1
    except:
        count[s] = 0

n_tot = 0
for k in count.values():
    n_tot += k

p = []
for k in count.values():
    p.append(k/n_tot)

p = np.array(p)
S = np.sum(-p*np.log2(p))/np.log2(len(p))
print(S)
