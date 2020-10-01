import random
import tensorflow as tf
#Picking minbatches from data
def minibatch_iter(batch_size,X,y):
    """This function provides an iterator for picking up minibatches of desired batch_size. Also needs X (features) and y (label) inputs"""
    no_obs = len(X)
    indices = list(range(no_obs))
    #randomly reading observations
    random.shuffle(indices)
    for i in range(0,no_obs,batch_size):
        j = tf.constant(indices[i:min(i + batch_size, no_obs)])
        yield tf.gather(X,j), tf.gather(y,j)