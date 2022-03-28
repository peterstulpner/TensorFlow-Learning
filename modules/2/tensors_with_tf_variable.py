import tensorflow as tf

# Create the same tensors from before using tensor variable:
changeable_tensor = tf.Variable([10, 7])
unchangeable_tensor = tf.constant([10, 7])

# Changing elements in changeable tensor:
changeable_tensor[0].assign(7)

print(changeable_tensor)