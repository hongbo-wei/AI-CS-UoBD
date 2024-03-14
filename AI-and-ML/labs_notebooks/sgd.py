import math

# Sequential gradient descent, Algorithm 9.1
def sgd(Fobj,Fwobj,α,ε,w0):

    # Initialization
    F = Fobj(w0)
    Fn = []
    ΔF = math.inf
    w = w0

    # Convergence test and iteration
    while (ΔF >= ε):

        # Save current objective function value for output
        Fn = Fn + [F]

        # Gradient descent step
        wnew = w - α*Fwobj(w)

        # Compute convergence measure
        Fnew = Fobj(wnew)
        ΔF = abs(Fnew-F)

        # Iteration -- update parameters and objective function value
        w = wnew
        F = Fnew

    return w, Fn
