x = [1, 2, 3]
y = [1, 5, 11]

alpha = [1, 2, 0.5]

for a in alpha:
    print(f"\nalpha={a}")
    C = 0
    w0 = 0
    w1 = 0
    for i in range(len(x)):
        f = w0 + w1 * x[i]
        C = C + (f - y[i]) ** 2
        w0 = w0 - a * (f - y[i])
        w1 = w1 - a * (f - y[i]) * x[i]

        # print f, C, w0, w1
        print(f"\tf={f} C={C} w0={w0} w1={w1}")