from ad import *

# activation function for every layer: relu 
def relu(u):
    return max(dual(0,0),u)

def convnet(x):
    '''
    x: input vector
    w1, w2: weights
    v: weights
    z: intermediate layer
    y: output
    '''
    x_dual = [dual(val, 0) for val in x]
    w1 = dual(1.2, 1) # with respect to parameter w1
    w2 = dual(-0.2, 0)
    v = [-0.3, 0.6, 1.3, -1.5]
    v_dual = [dual(val, 0) for val in v]

    # z = max(0, w^T * x)
    z = []
    for i in range(len(x) - 1):
        u = x_dual[i] * w1 + x_dual[i+1] * w2
        z.append(relu(u)) # activation function

    # y = max(0, v^t * z)
    y = relu(z[0]*v_dual[0] + z[1]*v_dual[1] + z[2]*v_dual[2] + z[3]*v_dual[3])

    return y, z


x = [0.3, -1.5, 0.7, 2.1,0.1]

y, z = convnet(x)
print('y = ', y)

n = 1
print('z =', z)
for i in z:
    print(f'\tz{n} = {i}')
    n += 1