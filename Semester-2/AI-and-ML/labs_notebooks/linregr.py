import numpy as np

# Generate Gaussian linear regression data and model
def gen_data(N,D,σ):

    # True model parameters
    wtrue = np.random.normal(0,1.0,(D,1))

    # Generate random X (feature) data
    X = np.random.normal(0.0,1.0,(D,N))

    # Generate Y (label) data
    e = np.random.normal(0.0,σ,(1,N))
    Y = (wtrue.T) @ X + e

    return wtrue, X, Y

# Generate initial parameter guess
def gen_w0(D):
    return np.random.normal(0,1.0,(D,1))

# Linear regression objective function values
# a squared loss function
def F(w,X,Y):
    F = ((w.T @ X - Y)**2.0).sum(axis=1) # @ represents matrix multiplication
    return F[0]

# Linear regression gradient of objective function with respect to w
def Fw(w,X,Y):
    D = len(w)
    dF = 2*(((w.T @ X - Y))*X).sum(axis=1)
    return np.reshape(dF,(D,1))
