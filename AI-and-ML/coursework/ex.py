import numpy as np

def relu(x):
  """ReLu activation function."""
  return np.maximum(0, x)

def two_layer_cnn(x, w, v):
  """Calculates the output of a 2-layer CNN with ReLU activation."""
  # Convert input to a numpy array
  x = np.array(x)

  # Calculate weighted sum in the hidden layer
  z = np.dot(w, x)
  # Apply ReLU activation in the hidden layer
  z = relu(z)

  # Calculate weighted sum in the output layer
  y = np.dot(v, z)
  # Apply ReLU activation in the output layer (not typical for CNNs)
  y = relu(y)

  return y

# Define input vector, weights, and output layer weights
x = [0.3, -1.5, 0.7, 2.1, 0.1]
w = np.array([1.2, -0.2])
v = np.array([-0.3, 0.6, 1.3, -1.5])

# Calculate the output
y = two_layer_cnn(x, w, v)

print("Output y:", y)
