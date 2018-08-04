import json
import numpy as np
#import torch

#Dataset1
def data1(n):
    x = 3 * (np.random.rand(n, 2) - 0.5)#x -> n * 2
    return x

def ans1(x, n):
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

    return y

#N = 100
#data = data1(N)
#ans = ans1(data, N)
#print(data)
#print(ans)


#n = 100
#x = 3 * (np.random.rand(n, 2) - 0.5)#x -> n * 2

#radius = np.zeros((n, 1))
#for t in range(n):
#    radius[t] = (x[t][0]**2 + x[t][1]**2)**-2
#radius = ((x[:, 0]**2 + x[:, 1]**2)**-2)
#radisu = [x(:, 1).^2 + x(:, 2).^2];

#rand1 = np.random.randn(n, 1)
#rand2 = np.random.randn(n, 1)

#y = (radius > 0.7 + 0.1 * randn(n, 1)) & (radius < 2.2 + 0.1 * randn(n, 1));
#y = (radius - 0.1 * rand1 > 0.7) & (radius - 0.1 * rand2 < 2.2)
#y = 2 * y -1

#print(y.shape)
#print(y.T)
