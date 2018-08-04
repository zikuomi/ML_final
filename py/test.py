print('This is ML_final!')

import json
import numpy as np
#import torch

#Dataset1
n = 100
x = 3 * (np.random.rand(n, 2) - 0.5)#x -> n * 2

radius = np.zeros((n, 1))
for t in range(n):
    radius[t] = (x[t][0]**2 + x[t][1]**2)**-2
#radius = ((x[:, 0]**2 + x[:, 1]**2)**-2)
#radisu = [x(:, 1).^2 + x(:, 2).^2];

rand1 = np.random.randn(n, 1)
rand2 = np.random.randn(n, 1)

#y = (radius > 0.7 + 0.1 * randn(n, 1)) & (radius < 2.2 + 0.1 * randn(n, 1));
y = (radius - 0.1 * rand1 > 0.7) & (radius - 0.1 * rand2 < 2.2)
y = 2 * y -1

print(y.shape)
print(y.T)

#Dataset2
n = 40
omega = np.random.randn(1, 1)
noise = 0.8 * np.random.randn(n, 1)

x = np.random.randn(n, 2)
for t in range(n):
    y = 2 * (omega * x[t][0] + x[t][1] + noise > 0) - 1

print(y.shape)
print(y.T)

#Dataset3
m = 20
n = 40

r = 2

A = np.dot(np.random.rand(m, r), np.random.rand(r, n))

ninc = 100

Q = np.zeros((1, ninc))
for t in range(ninc):
    Q[t] = np.random.randrange(1, m*n, 1) % m*n
#Q = np.random.permutation((m * n, ninc))


print(A.shape)
print(Q.shape)

print(Q)

#A(Q) = NaN
