def g(w_0, w_1):
    x = [1, 0, 2, -1]
    y = [3, 2, 5, 0]

    g = 0
    for i in range(len(x)):
        g += ((w_0 + w_1 * x[i]) - y[i]) ** 2

    # g /= len(x)

    return g


W = [(2, 3), (3, 1), (2, 2), (0, 2)]

for w in W:
    loss = g(w[0], w[1])
    print(loss)