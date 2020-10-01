import tensorflow as tf
def synthetic_data(w, b, num_examples): 
    """Generates synthetic data for linear regression example as  y = Xw + b + noise.
       Accepts inputs as :
       w = weights vector
       b = beta
       num_examples = number of observations"""
    X = tf.zeros((num_examples, w.shape[0]))
    X += tf.random.normal(shape=X.shape)
    y = tf.matmul(X, tf.reshape(w, (-1, 1))) + b
    y += tf.random.normal(shape=y.shape, stddev=0.01)
    y = tf.reshape(y, (-1, 1))
    return X, y