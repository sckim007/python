# Lab 4 Multi-variable linear regression
import tensorflow as tf

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0402-linear.meta')
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

# 각 변수 값 출력 : w1, w2, w3, b
print("Result : ", sess.run(RWeight), sess.run(RBias))

# 아래와 같이 각 변수를 찾아 출력
trained_weights = sess.run(RWeight)
trained_bias = sess.run(RBias)
print("w1 : {}".format(trained_weights[0][0]),
      "w2 : {}".format(trained_weights[1][0]),
      "w3 : {}".format(trained_weights[2][0]),
      "b : {}".format(trained_bias))
# 아래와 같이 각 변수를 찾아 출력
print("w1 : {}".format(trained_weights[0]),
      "w2 : {}".format(trained_weights[1]),
      "w3 : {}".format(trained_weights[2]),
      "b : {}".format(trained_bias))

# 주어진 값의 예측치
test_data = [[73., 80., 75.]]
print(sess.run(RHypothesis, feed_dict={RX:test_data}))

# Close session
sess.close()