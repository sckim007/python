# Lab 4 Multi-variable linear regression
import tensorflow as tf
import numpy as np

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0403-linear.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

# Launch the graph in a session.
graph = tf.get_default_graph()

# Read each trained variables
RX = graph.get_tensor_by_name("holder_x:0")
RWeight = graph.get_tensor_by_name("weight:0")
RBias = graph.get_tensor_by_name("bias:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")

# Print each trained variables
print("Restored Weight = ", sess.run(RWeight))
print("Restored Bias   = ", sess.run(RBias))

# Ask prediction for input values
print("Your score will be ", sess.run(RHypothesis, feed_dict={RX: [[100, 70, 101]]}))
print("Other scores will be ", sess.run(RHypothesis, feed_dict={RX: [[60, 70, 110], [90, 100, 80]]}))

# Close session
sess.close()