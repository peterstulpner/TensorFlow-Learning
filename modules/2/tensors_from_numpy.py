import tensorflow as tf
import numpy as np

# TensorFlow ones/zeros, is the same as MATLAB and Numpy
ones = tf.ones([10, 7])
zeros = tf.zeros([10, 7])

# Turning numpy arrays into tf tensors
# Main difference between numpy arrays and tensorflow tensors: Tensors can be run faster on a GPU for numerical computing

numpy_A = np.arange(1, 25, dtype=np.int32)

tensor_from_A = tf.constant(numpy_A)

tensor_from_A = tf.constant(numpy_A, shape=(2, 3, 4))

print(tensor_from_A)