# Disable GPU Operation
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Lab 4 Multi-variable linear regression
import tensorflow as tf

# 시작시간 마킹
import time
start = time.time()

tf.set_random_seed(777)  # for reproducibility

x_data = [[73., 80., 75.],
          [93., 88., 93.],
          [89., 91., 90.],
          [96., 98., 100.],
          [73., 66., 70.]]
y_data = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]]

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

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session.
#sess = tf.Session()
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# 반복 학습
for step in range(4001):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

# 각 변수 값 출력 : w1, w2, w3, b
print("Result : ", sess.run(W), sess.run(b))

# 아래와 같이 각 변수를 찾아 출력
trained_weights = sess.run(W)
trained_bias = sess.run(b)
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
print(sess.run(hypothesis, feed_dict={X:test_data}))

# 학습 데이터(그래프 각 변수) 저장
saver = tf.train.Saver()
saver.save(sess, './model_save_dir/0402-linear')
sess.close()

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))