import numpy as np
import matplotlib.pyplot as plt

# Generate Gaussian linear classification data and model, σ determines the overlap
def gen_data(N,D,σ):

    # True model parameters
    wtrue = np.random.normal(0,1.0,(D,1))
    # mean is 0, standard deviation is 1.0
    # generate an array with size D*1

    # Generate random X (feature) data
    X = np.random.normal(0.0,1.0,(D,N))
    # size of X is D*N

    # Generate Y (label) data
    e = np.random.normal(0.0,σ,(1,N))
    Y = np.sign((wtrue.T) @ X + e).reshape(N)
    return wtrue, X, Y

# Generate initial parameter guess
def gen_w0(D):
    return np.random.normal(0,1.0,(D,1))

# 0-1 loss linear classification objective function value
def F01(w,X,Y):
    D,N = X.shape
    return (np.sign(w.T @ X).reshape(N) == Y).sum(axis=0)

# Perceptron loss objective function
def Fp(w,X,Y):
    D,N = X.shape
    F = 0
    for i in range(N):
        F = F + max(0, (-Y[i]*(w.T @ X[:,i]))[0])
    return F
