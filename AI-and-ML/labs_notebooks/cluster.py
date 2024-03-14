import numpy as np

# Update configuration (cluster assignment indicator matrix)
def config(x,μ):
    K = len(μ)
    N = len(x)
    X = np.zeros((N,K))
    for i in range(N):
        dopt = np.inf # dopt (Optimal Distance)
        kopt = K + 1 # kopt (Index of Nearest Cluster Centroid)
        for k in range(K):
            d = (x[i]-μ[k])**2.0
            # print(d)
            if d < dopt:
                dopt = d
                kopt = k
        X[i,kopt] = 1
    return X

# Update centroids (cluster means)
def means(x,X):
    Nk = X.sum(axis=0)
    Σk = (X.T*x).sum(axis=1)
    μ = Σk/Nk
    return μ

# Update objective (sum-of-squared errors)
def Fobj(x,μ,X):
    F = 0
    N = len(x)
    K = len(μ)
    for i in range(N):
        for k in range(K):
            F = F + X[i,k]*(x[i]-μ[k])**2.0
    return F
