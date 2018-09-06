# Disable GPU Operation
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

import tensorflow as tf
import numpy as np

# 시작시간 마킹
import time
start = time.time()

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
org_x = xy[:, 0:-1]
org_y = xy[:, [-1]]

# very important. It does not work without it.
xy = MinMaxScaler(xy)
print(xy)

x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print("<<<<<< x_data >>>>>>>")
print(x_data)
print("<<<<<< y_data >>>>>>>")
print(y_data)

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 4], name="variable_x")
Y = tf.placeholder(tf.float32, shape=[None, 1], name="variable_y")

W = tf.Variable(tf.random_normal([4, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis
hypothesis = tf.matmul(X, W) + b
tf.identity(hypothesis, name="hypothesis")

# Simplified cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session.
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(101):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

'''
Read Weight and Bias predictor 
'''
weight_variables = sess.run(W)
bias_variable = sess.run(b)
print("Weight : ", weight_variables)
print("Bias   : ", bias_variable)

print("<<<<<<<<<<<<<<<<<< prediction case I >>>>>>>>>>>>>>>>>>>>")
for test_list_data in org_x:
    test_array_data = np.array(test_list_data)
    pred_value = np.dot(test_array_data, weight_variables) + bias_variable
    print("{0}'s prediction = {1}".format(test_list_data, pred_value))

print("<<<<<<<<<<<<<<<<<< prediction case 2 >>>>>>>>>>>>>>>>>>>>")
for test_list_data in x_data:
    test_array_data = np.array(test_list_data)
    test_array_data2 = test_array_data.reshape(1, 4)
    print("{0}'s prediction = {1}".format(test_array_data2, sess.run(hypothesis, feed_dict={X: test_array_data2})))

##########################################################################
# Save trained data model
##########################################################################
saver=tf.train.Saver()
saver.save(sess, './model_save_dir/0703-linear')

# Tensorflow session을 종료하고 자원을 반환한다.
sess.close()

##########################################################################
# Restore trained data model
##########################################################################
# Launch the graph in a session.
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

saver = tf.train.import_meta_graph('./model_save_dir/0703-linear.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

graph = tf.get_default_graph()
RWeight = graph.get_tensor_by_name("weight:0")
RBias = graph.get_tensor_by_name("bias:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")
print("Restored Weight = ", sess.run(RWeight))
print("Restored Bias   = ", sess.run(RBias))
for test_list_data in x_data:
    test_array_data = np.array(test_list_data)
    test_array_data2 = test_array_data.reshape(1, 4)
    print("{0}'s prediction = {1}".format(test_array_data2, sess.run(RHypothesis, feed_dict={X: test_array_data2})))

##########################################################################
# 학습된 값을 가지고 어덯게 적용하는 것인가 ??????????????????????????????
##########################################################################

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))