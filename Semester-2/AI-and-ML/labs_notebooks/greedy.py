import math

# Find minimum of list of tuples
def mintuple(x):
    xmin = math.inf
    for i,xp in x:
        if xp < xmin:
            imin,xmin = i,xp
    return (imin,xmin)

# Ensure cluster assignment is feasible (has at least one data point in each cluster)
def cluster_fix(X,K):
    N = len(X)
    for k in range(K):
        if X.count(k) == 0:
            X[k] = k
    return X

# Cluster means
def cluster_means(x,X,K):
    N = len(X)
    mu = [0]*K
    for k in range(K):
        # generate a list to store corresponding cluster points for each cluster
        xk = [x[i] for i in range(N) if X[i]==k]
        mu[k] = sum(xk)/len(xk)
    return mu

# Compute cluster objective
def cluster_obj(x,X,mu,K):
    N = len(X)
    F = 0
    for k in range(K):
        # generate a list to store corresponding cluster points for each cluster
        xk = [x[i] for i in range(N) if X[i]==k]
        dk = sum([(xp-mu[k]/len(xk))**2.0 for xp in xk])
        F = F + dk
    return F

# Create 1-Hamming distance cluster assignment neighbourhood
def cluster_nbr(X,K):
    N = len(X)
    Xnbr = []
    for n in range(N):
        j = X[n] + 1
        if j == K:
            j = 0
        Xn = X.copy()
        Xn[n] = j
        Xnbr = Xnbr + [cluster_fix(Xn,K)]
    return Xnbr

# Evaluate objectives for cluster assignment neighbourhood
def cluster_nbrobj(x,Xnbr,K):
    N = len(x)
    Fnbr = []
    for nbr in range(N):
        mu = cluster_means(x,Xnbr[nbr],K)
        Fnbr = Fnbr + [(nbr,cluster_obj(x,Xnbr[nbr],mu,K))]
    return Fnbr
