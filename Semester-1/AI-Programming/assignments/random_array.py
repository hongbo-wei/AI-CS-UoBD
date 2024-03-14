import numpy as np

# set seed so that each time it will generate the same result.
np.random.seed(0)

num_images_to_show = 5
array = np.random.randint(0, 100, num_images_to_show)
print(array)

# for i in array:
#     axes[i].imshow(X_train[i].reshape(28, 28), cmap='gray') # Reshapes the image data from a flat array to a 28x28 matrix
#     axes[i].axis('off') # Hide axis scale