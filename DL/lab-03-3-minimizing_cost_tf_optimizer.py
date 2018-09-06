# Disable GPU Operation
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Lab 3 Minimizing Cost
import tensorflow as tf

# 시작시간 마킹
import time
start = time.time()

tf.set_random_seed(777)  # for reproducibility

# tf Graph Input
X = [1, 2, 3]
Y = [1, 2, 3]

# Set wrong model weights
W = tf.Variable(5.0)

# Linear model
hypothesis = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize: Gradient Descent Magic
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run(W))
    sess.run(train)

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))