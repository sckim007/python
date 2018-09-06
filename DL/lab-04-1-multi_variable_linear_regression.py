# Disable GPU Operation
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Lab 4 Multi-variable linear regression
import tensorflow as tf

# 시작시간 마킹
import time
start = time.time()

tf.set_random_seed(777)  # for reproducibility

x1_data = [73., 93., 89., 96., 73.]
x2_data = [80., 88., 91., 98., 66.]
x3_data = [75., 93., 90., 100., 70.]

y_data = [152., 185., 180., 196., 142.]

# placeholders for a tensor that will be always fed.
x1 = tf.placeholder(tf.float32, name='holder_x1')
x2 = tf.placeholder(tf.float32, name='holder_x2')
x3 = tf.placeholder(tf.float32, name='holder_x3')

Y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]), name='weight1')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
tf.identity(hypothesis, name='hypothesis')
print(hypothesis)

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize. Need a very small learning rate for this data set
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(4001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
        print("w1: {}".format(sess.run(w1)), "w2: {}".format(sess.run(w2)),
              "w3: {}".format(sess.run(w3)), "b: {}".format(sess.run(b)))

# Ask prediction for input value.
i = 0
for _ in y_data:
    print(i, "st prediction = ", sess.run(hypothesis, feed_dict={x1:x1_data[i], x2:x2_data[i], x3:x3_data[i]}))
    i += 1

# 학습 데이터(그래프 각 변수) 저장
saver = tf.train.Saver()
saver.save(sess, './model_save_dir/0401-linear')
sess.close()

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))