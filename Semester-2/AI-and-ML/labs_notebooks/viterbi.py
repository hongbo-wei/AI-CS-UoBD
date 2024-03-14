import numpy as np

# Implementation of Viterbi decoding for HMMs
def decode(x,Pyy,Pxy,Py0,states,symbols):

    # Step 1. Initialization
    T = len(x)-1
    K = len(states)
    pstar = np.empty((K,T+1))
    Ystar = np.empty((K,T+1),dtype=int)
    xt = symbols[x[0]]
    pxty = Pxy[:,xt]
    for y in range(K):
        pstar[y,0] = pxty[y]*Py0[y]

    # Step 2. Forward recursion:
    for t in range(1,T+1):
        xt = symbols[x[t]]
        pxty = Pxy[:,xt]
        ptxyy = np.empty((K,K))
        for y in range(K):
            for yp in range(K):
                ptxyy[y,yp] = pxty[y]*Pyy[yp,y]*pstar[yp,t-1]

        Ystar[:,t] = np.argmax(ptxyy,axis=1)
        pstar[:,t] = np.max(ptxyy,axis=1)

    # Step 3. Backtrack
    ystar = np.empty((T+1),dtype=int)
    ystar[T] = np.argmax(pstar[:,T])
    for t in range(T,0,-1):
        ystar[t-1] = Ystar[ystar[t],t]

    ypred = "".join([states[y] for y in ystar]) 
    return ypred, pstar, Ystar
