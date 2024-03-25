from ad import *

# Every layer is using relu activation function
def relu(u):
    return max(dual(0,0),u)

def convnet(x):
    w1 = dual(1.2, 1) # with respect to parameter w1
    w2 = dual(-0.2, 0)

    v1 = dual(-0.3, 0)
    v2 = dual(0.6, 0)
    v3 = dual(1.3, 0)
    v4 = dual(-1.5, 0)
    v = [v1, v2, v3, v4]

    z = []
    for i in range(len(x) - 1):
        # TODO
        u = x[i] * w1 + x[i+1] * w2
        # activation function
        z.append(relu(u))

    y = []
    for i in range(len(z)):
        # activation function
        y.append(relu(z[i]*v[i]))

    y_max = dual(0, 0)
    for i in range(4):
        y_max = max(y_max, y[i])

    # Gradients of the output with respect to the rest of the parameters
    FFw = relu(-y_max*(v1*z[0] + v2*z[1] + v3*z[2] + v4*z[3]))
    print(f'Gradient of the output with respect to the rest of the parameters: {FFw}')

    return y_max, z


x = [dual(0.3, 0), dual(-1.5, 0), dual(0.7, 0), dual(2.1, 0), dual(0.1, 0)]

y, z = convnet(x)
print(f'y = {y}')

n = 1
print('z =', z)
for i in z:
    print(f'\tz{n} = {i}')
    n += 1