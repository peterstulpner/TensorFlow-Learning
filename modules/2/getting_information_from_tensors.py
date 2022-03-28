import tensorflow as tf

# Getting information from tensors:
# Info could be:
# - Shape, Rank, axis/dimension, size
# - tensor.shape, tensor.ndim, tensor[0], tensor[:, 1] etc, tf.size(tensor)

# Creating a rank 4 tensor:
rank_4_tensor = tf.zeros((2, 3, 4, 5))

# Getting attributesL
print("Datatype of everyelement: ", rank_4_tensor.dtype)
print("Number of dimensions (rank): ", rank_4_tensor.ndim)
print("Tensor shape: ", rank_4_tensor.shape)
print("Elements along the 0 axis: ", rank_4_tensor.shape[0])
print("Elements along last axis: ", rank_4_tensor.shape[-1])
print("Total num elements in out tensor: ", tf.size(rank_4_tensor).numpy()) # Gives us a nice int instead of a tensor object

# Indexing on tensors: 

# Tensors can be indexed the same way as lists:

# First 2 elements of each dimension:
rank_4_tensor[:2, :2, :2, :2] 

# Get first element from each dimention except the last dimension:
rank_4_tensor[:1, :1, :1, :]

# Adding dimension to the end of a tensor:

# Rank 2 tensor:

rank_2_tensor = tf.constant([[10, 7], [3, 4]])

# Get the last item of each row of the rank 2 tensor:
rank_2_tensor[:, -1]

# Adding in a dimension to the tensor:
rank_3_tensor = rank_2_tensor[..., tf.newaxis] # adds a dimension on the end of 1, ... acts same way as spread operator in js

# OR:

tf.expand_dims(rank_2_tensor, axis=-1) # Axis = -1 => The last axis of the tensor