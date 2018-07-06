# Lab 5 Logistic Regression Classifier
import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

xy = np.loadtxt('data-03-diabetes.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape, y_data.shape)

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 8], name='holder_x')
Y = tf.placeholder(tf.float32, shape=[None, 1], name='holder_y')

W = tf.Variable(tf.random_normal([8, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(tf.matmul(X, W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
tf.identity(hypothesis, name='hypothesis')

# cost/loss function
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) *
                       tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Accuracy computation
# # True if hypothesis>0.5 else False
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# Launch graph
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
#sess = tf.Session(config=config)
with tf.Session(config=config) as sess:
    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())

    for step in range(20001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy],
                       feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)

    # Print weight and bias
    print("Weight : ", sess.run(W))
    print("Bias : ", sess.run(b))

    # Prediction for input data
    test_data = [[-0.294118, 0.487437, 0.180328, -0.292929, 0., 0.00149028, -0.53117, -0.0333333]]
    print('1st prediction = ', sess.run(hypothesis, feed_dict={X: test_data}))

    test_data = [[-0.882353, -0.145729, 0.0819672, -0.414141, 0, -0.207153, -0.766866, -0.666667]]
    print('2st prediction = ', sess.run(hypothesis, feed_dict={X: test_data}))

    ##########################################################################
    # 학습 데이터(그래프 각 변수) 저장
    ##########################################################################
    saver = tf.train.Saver()
    saver.save(sess, './model_save_dir/0502-logistic')

    # Tensorflow session을 종료하고 자원을 반환한다.
    sess.close()

