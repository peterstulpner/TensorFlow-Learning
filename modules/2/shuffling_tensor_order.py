# Shuffle a tensor (good for data shuffling, to get rid of the input orders effect on learning)

import tensorflow as tf


not_shuffled = tf.constant([[10, 7], 
                            [3, 4], 
                            [2, 5]])

# Shuffled along the first dimenosion, (m, n) will shuffle along m, n will preserve order, 
# if you call tf.random.set_seed(seed) you can guarantee the randomness is the same each time
tf.random.set_seed(42)
shuffled = tf.random.shuffle(not_shuffled, seed=42)

# Need to set both the global and operational seeds (set_seed = global, seed in the operation = operational) then the shuffled tensor 
# will be recreatable