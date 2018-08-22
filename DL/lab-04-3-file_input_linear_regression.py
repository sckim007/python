# Lab 4 Multi-variable linear regression
import tensorflow as tf
import numpy as np

tf.set_random_seed(777)  # for reproducibility

xy = np.loadtxt('data\data-01-test-score.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# Make sure the shape and data are OK
print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 3], name='holder_x')
Y = tf.placeholder(tf.float32, shape=[None, 1], name='holder_y')

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis
hypothesis = tf.matmul(X, W) + b
tf.identity(hypothesis, name='hypothesis')

# Simplified cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))
tf.identity(cost, name='cost')

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session.
# sess = tf.Session()
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

###############################################################################
# 학습된 Weight 와 Bias 확인
###############################################################################
print("Weight : ", sess.run(W))
print("Bias : ", sess.run(b))

###############################################################################
# 입력 값에 따른 예측치 확인
###############################################################################
print("Your score will be ", sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
print("Other scores will be ", sess.run(hypothesis, feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))

###############################################################################
# 학습 데이터(그래프 각 변수) 저장
###############################################################################
saver = tf.train.Saver()
saver.save(sess, './model_save_dir/0403-linear')
sess.close()


