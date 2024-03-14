def bellman_product(x):

    # Initialization
    P = (1, 1)  # Change S to P for product
    X = ([[]], [[]])

    # Iteration
    for xn in x:
        if 1 > (xn * P[1]):  # Change 0 to 1 and '+' to '*' for product
            Ptails = 1
            Xtails = [[]]
        else:
            Ptails = xn * P[1]  # Change '+' to '*' for product
            Xtails = [Xp + [xn] for Xp in X[1]]

        if Ptails > P[0]:
            X = (Xtails, Xtails)
            P = (Ptails, Ptails)
        else:
            X = (X[0], Xtails)
            P = (P[0], Ptails)
    return (X, P)

x = [0.1, -0.3, 2.6, 9.1, -0.8]
Xopt, Popt = bellman_product(x)
print(f'Bellman recursion optimal product P={Popt}, configuration X={Xopt}')
