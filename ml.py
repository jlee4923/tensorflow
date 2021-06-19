import tensorflow as tf
import numpy as np
print(tf.__version__)
a= tf.constant(10,tf.int32)
b= tf.constant(20)
c= a+b
d= (a+b).numpy()

print(type(a), type(b))
print(type(c))
print(c)
print(type(d), d)
d_numpy_to_tensor= tf.convert_to_tensor(d) #converts a numpy object to a tensor object
print(type(d_numpy_to_tensor))
print(d_numpy_to_tensor)
