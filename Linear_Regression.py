# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:30:38 2024

@author: bitan
"""
import matplotlib.pyplot as plt
import numpy as np
my_data = np.genfromtxt(r"C:\Users\bitan\Downloads\project files\data.csv", delimiter=',') # read the data
X = my_data[:, 0].reshape(-1,1) # -1 tells numpy to figure out the dimension by itself
ones = np.ones([X.shape[0], 1]) # create a array containing only ones 
X = np.concatenate([ones, X],1) # cocatenate the ones to matrix X
y = my_data[:, 1].reshape(-1,1) # create the matrix y
plt.scatter(my_data[:, 0].reshape(-1,1), y)

alpha = 0.0001
iters = 1000

# theta is a row vector
theta = np.array([[1.0, 1.0]])


def computeCost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2) # @ means matrix multiplication of arrays. If we want to use * for multiplication we will have to convert all arrays to matrices
    return np.sum(inner) / (2 * len(X))

computeCost(X, y, theta) # outputs 319.40631589398157


def gradientDescent(X, y, theta, alpha, iters):
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum((X @ theta.T - y) * X, axis=0)
        cost = computeCost(X, y, theta)
        # if i % 10 == 0: # just look at cost every ten loops for debugging
        #     print(cost)
    return (theta, cost)

g, cost = gradientDescent(X, y, theta, alpha, iters)  
print(g, cost)


plt.scatter(my_data[:, 0].reshape(-1,1), y)
axes = plt.gca()
x_vals = np.array(axes.get_xlim()) 
y_vals = g[0][0] + g[0][1]* x_vals #the line equation
plt.plot(x_vals, y_vals, '--')
