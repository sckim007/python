# Lab 7 Learning rate and Evaluation
import tensorflow as tf
import random
import matplotlib.pyplot as plt
tf.set_random_seed(777)  # for reproducibility

from tensorflow.examples.tutorials.mnist import input_data
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

nb_classes = 10

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0704-mnist.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

# Launch the graph in a session.
graph = tf.get_default_graph()

# Read each trained variables
RX = graph.get_tensor_by_name("X:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")

'''
# Get one and predict
from datetime import datetime

for _ in range(5):
    print('>>> Prediction Start : ', datetime.now())
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction: ", sess.run(
        tf.argmax(RHypothesis, 1), feed_dict={RX: mnist.test.images[r:r + 1]}))
    print('>>> Prediction End : ', datetime.now())

    plt.imshow(
        mnist.test.images[r:r + 1].reshape(28, 28),
        cmap='Greys',
        interpolation='nearest')
    plt.show()
'''

'''
import PIL.Image as pilimg
import numpy as np

# Read image
im = pilimg.open("./data/eight.jpg")
# Fetch image pixel data to numpy array
pix = np.array(im)
plt.imshow(pix)
plt.show()

pix2 = pix.reshape(1, 784)

print("Label: ", 8)
print("Prediction: ", sess.run(
    tf.argmax(RHypothesis, 1), feed_dict={RX: pix2}))

'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Set file and label
file_name = "./data/three.png"
label = 3

data_image = np.zeros((1, 784))

gray = cv2.imread(file_name, cv2.IMREAD_REDUCED_GRAYSCALE_2)
#gray = cv2.imread("./data/eight.jpg")
##print(">> Shape: {}".format(gray.shape))

print(">>>>>>>>>>--\n", gray)

gray = cv2.resize(255 - gray, (28, 28))
##print(">> Shape: {}".format(gray.shape))
print(">>>>>>>>>>++\n", gray)

plt.imshow(gray)
plt.show()

#cv2.imwrite("./eight_pre.png", gray)

flatten = gray.flatten() / 255.0
##print(">> Shape: {}".format(flatten.shape))
print(">>>>>>>>>>ff\n", flatten)

data_image = np.reshape(flatten, (1, 784))

print(">> Label: ", label)
##print(">> Shape: {}".format(images.shape))

print(">> Prediction: ", sess.run(
    tf.argmax(RHypothesis, 1), feed_dict={RX: data_image}))

# Close session
sess.close()