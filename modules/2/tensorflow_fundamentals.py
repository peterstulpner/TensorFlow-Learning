# Covers: 
# - Intorduction to tensors
# - Getting info from tensors
# - manipulating tensors
# - tensors and numbpy

# Introduction to Tensors:
import tensorflow as tf

scalar = tf.constant(7)

# Check the dimensions of a tensor:
scalar_dim = scalar.ndim

#Creating a vector:
vector = tf.constant([10, 10])
vector_dim = vector.ndim

# Creating a matrix
matrix = tf.constant([[10, 7], [7, 10]])
matrix_dim = matrix.ndim

matrix_2 = tf.constant([[10., 7.], 
                        [3., 2.], 
                        [8., 9.]], dtype=tf.float16)

