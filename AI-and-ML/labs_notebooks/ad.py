import builtins

# Implementation of dual numbers type
class dual:
    def __init__(self, val, grad):
        self.val = val
        self.grad = grad
    
    def __add__(self, other):
        val = self.val + other.val
        grad = self.grad + other.grad
        return dual(val, grad)
    
    def __sub__(self, other):
        val = self.val - other.val
        grad = self.grad - other.grad
        return dual(val, grad)
    
    def __neg__(self):
        val = -self.val
        grad = -self.grad
        return dual(val, grad)

    def __mul__(self, other):
        val = self.val * other.val
        grad = self.grad * other.val + other.grad * self.val
        return dual(val, grad)
    
    def __str__(self):
        return f'({self.val},{self.grad})'
    
    def __repr__(self):
        return str(self)

# Override built-in maximum function
def max(u,v):
    if type(u) is not dual:
        return builtins.max(u,v)
    else:
        val = builtins.max(u.val,v.val)
        # if u.val > v.val:
        #     grad = u.grad
        # else:
        #     grad = v.grad
        grad = u.grad*int(u.val > v.val) + v.grad*int(u.val <= v.val)
        return dual(val, grad)
