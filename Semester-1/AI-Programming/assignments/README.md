"""
Use the l2 norm when:
The data is not sparse and you want to handle outliers gracefully.
The data has a more balanced range of values and you don't need to worry about feature importance.
You want to ensure that the overall distance between samples is well-preserved.
"""

"""
And I compared the dataset, for each pixel's value
before normalized: 0~255, it can be considered as already normalized
after normalized: 0~1
After using Normalizer, the accuracy of prediction drops about 0.1
therefore I decided not to use Normalizer.

the drop in accuracy after using Normalizer() is likely due to the reduced range of pixel values. Normalizer() scales each sample individually to unit norm, which means that the maximum value of each pixel becomes 1. This can make it difficult for the model to distinguish between different images, as the range of values is much smaller than the original range of 0 to 255.

StandardScaler, on the other hand, centers and scales each feature by removing the mean and dividing by the standard deviation. This preserves the original range of the pixel values, while still normalizing the data. As a result, StandardScaler is generally a better choice for image classification tasks.

StandardScaler preserves the original range of the data, while Normalizer does not. This is why StandardScaler is generally a better choice for image classification tasks.
"""
