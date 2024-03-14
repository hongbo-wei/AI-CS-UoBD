a = 10**(-1000)  # Underflow for most integer representations
print(a)

# Increase number of bits to represent floating-point numbers
from decimal import Decimal

a = Decimal('10') ** Decimal('-1000')
print(a)

# a mixture of really big and small numbers and whether you could re-order the computation
a = 1e20
b = 3.14
c = a + b - a
print(c)

# reorder the computation
a = 1e20
b = 3.14
c = a - a + b
print(c)