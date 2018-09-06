# Disable GPU Operation
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Lab 3 Minimizing Cost
import tensorflow as tf
import matplotlib.pyplot as plt

# 시작시간 마킹
import time
start = time.time()

tf.set_random_seed(777)  # for reproducibility

X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.placeholder(tf.float32)

# Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Launch the graph in a session.
sess = tf.Session()

# Variables for plotting cost function
W_history = []
cost_history = []

for i in range(-30, 50):
    curr_W = i * 0.1
    curr_cost = sess.run(cost, feed_dict={W: curr_W})
    W_history.append(curr_W)
    cost_history.append(curr_cost)

# Show the cost function
plt.plot(W_history, cost_history)
plt.show()

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))