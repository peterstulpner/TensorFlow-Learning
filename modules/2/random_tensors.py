import tensorflow as tf

# Tensor of arbitrary size with random numbers as elements, 
# very usefull for initialising neural networks as the inputs are a random tensor
random_tensor = tf.random.Generator.from_seed(42) # seed is for reproducibility
random_tensor = random_tensor.normal(shape=(3, 2)) # Normal tells us its a normal distribution, can also use uniform or other distributions

# If we keep the same seed then everytime the same "random" tensor will be genereated everytime, not setting the seed will result
# in different tensors every time

print(random_tensor)