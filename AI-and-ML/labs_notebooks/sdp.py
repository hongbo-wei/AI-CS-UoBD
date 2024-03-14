import math

# Find maximum of list of tuples
def maxtuple(x):
    xmax = -math.inf
    for i,xp in x:
        if xp > xmax:
            imax,xmax = i,xp
    return (imax,xmax)

# Find minimum of list of tuples
def mintuple(x):
    xmin = math.inf
    for i,xp in x:
        if xp < xmin:
            imin,xmin = i,xp
    return (imin,xmin)

# Return only values in list with true right tuple value
def truetuple(x):
    return [x for (x,b) in x if b]

# Add up all sublists, pair with sublist
def sublistsumpair(S):
    return [(X,sum(X)) for X in S]

# Returns True if given list is in ascending sorted order
def issorted(x):
    return all(x[i] <= x[i+1] for i in range(len(x)-1))

# Add up all sublists, pair with sublist
def listpartsortpair(S):
    return [(X,all(map(issorted,X))) for X in S]


# SDP exhaustive sublists
def sublists(x):

    # Initialization
    S = [[]]

    # Iteration
    for xn in x:

        # Extension
        S = S + [X + [xn] for X in S]

    return S


# SDP exhaustive list partitions
def listparts(x):

    # Initialization
    S = [[[x[0]]]]

    # Iteration
    for xn in x[1:]:

        # Extension
        S = [X[:-1] + [X[-1] + [xn]] for X in S] + [X + [[xn]] for X in S]

    return S


# SDP exhaustive permutations
def perms(x):

    # Initialization
    S = [[]]

    # Iteration
    for xn in x:

        # Extension
        S = [X[:i] + [xn] + X[i:] for X in S for i in range(len(X)+1)]

    return S


# Generic SDP (Algorithm 4.1)
def sdp_generic(x,init,extend,reduce,select):

    # Initialization
    S = init(x)

    # Iteration
    for xn in x:

        # Extension
        S = extend(S,xn)

        # Reduction
        S = reduce(S)


    # Selection
    return select(S)
