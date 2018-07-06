# Lab 5 Logistic Regression Classifier
import tensorflow as tf
import numpy as np

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0502-logistic.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

# Launch the graph in a session.
graph = tf.get_default_graph()
RX = graph.get_tensor_by_name("holder_x:0")
RWeight = graph.get_tensor_by_name("weight:0")
RBias = graph.get_tensor_by_name("bias:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")

# Create session with enabled gpu option
print("Restored Weight = ", sess.run(RWeight))
print("Restored Bias   = ", sess.run(RBias))

# Ask prediction for input values
test_data = [[-0.294118, 0.487437, 0.180328, -0.292929, 0., 0.00149028, -0.53117, -0.0333333]]
print('1st prediction = ', sess.run(RHypothesis, feed_dict={RX: test_data}))
test_data = [[-0.882353, -0.145729, 0.0819672, -0.414141, 0, -0.207153, -0.766866, -0.666667]]
print('2st prediction = ', sess.run(RHypothesis, feed_dict={RX: test_data}))