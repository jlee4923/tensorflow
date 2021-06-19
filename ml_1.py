import tensorflow as tf
import numpy as np
"""
instead of using placeholders, we use function(not lambda, def) to pass tensors(values) to it. This is possible now from TF 2.0 because of the feature, eager execution.
"""
a = tf.constant(3.0)
b = tf.constant(4.0)
@tf.function
def f(a,b):
    return a+b
res = f(a,b)
print(type(res)) #type of res= tensor
print(res.numpy()) #eager execution- can access res without running session in TF 1.x
