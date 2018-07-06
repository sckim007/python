import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)


xy = np.array([[828.659973, 833.450012, 908100, 828.349976, 831.659973],
               [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
               [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
               [816, 820.958984, 1008100, 815.48999, 819.23999],
               [819.359985, 823, 1188100, 818.469971, 818.97998],
               [819, 823, 1198100, 816, 820.450012],
               [811.700012, 815.25, 1098100, 809.780029, 813.669983],
               [809.51001, 816.659973, 1398100, 804.539978, 809.559998]])

# very important. It does not work without it.
xy = MinMaxScaler(xy)
print(xy)

x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0703-linear.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

# Launch the graph in a session.
graph = tf.get_default_graph()

# Read each trained variables
RX = graph.get_tensor_by_name("variable_x:0")
RWeight = graph.get_tensor_by_name("weight:0")
RBias = graph.get_tensor_by_name("bias:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")

# Print each trained variables
print("Restored Weight = ", sess.run(RWeight))
print("Restored Bias   = ", sess.run(RBias))

# Ask prediction for input values
for test_list_data in x_data:
    test_array_data = np.array(test_list_data)
    test_array_data2 = test_array_data.reshape(1, 4)
    print("test_array_data2's shape = ", test_array_data2.shape)
    print("{0}'s prediction = {1}".format(test_array_data2, sess.run(RHypothesis, feed_dict={RX:test_array_data2})))

##########################################################################
# 학습된 값을 가지고 어덯게 적용하는 것인가 ??????????????????????????????
##########################################################################