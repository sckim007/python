#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Lab 7 Learning rate and Evaluation
import tensorflow as tf
import random
import matplotlib.pyplot as plt
import numpy as np
import cv2

'''
tf.set_random_seed(777)  # for reproducibility

from tensorflow.examples.tutorials.mnist import input_data
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
'''
# Assign path and filename
model_save_dir = "./model_save_dir/minist/10-3/"
model_save_meta_file = model_save_dir + "nn_xavier.meta"

# Assign file and label
file_name = "./data/eight.jpg"
label = 8

###############################################################################
# 테스트 이미지 준비
###############################################################################
data_image = np.zeros((1, 784))

gray = cv2.imread(file_name, cv2.IMREAD_REDUCED_GRAYSCALE_2)

gray = cv2.resize(255 - gray, (28, 28))

plt.imshow(gray)
plt.show()

flatten = gray.flatten() / 255.0

data_image = np.reshape(flatten, (1, 784))

###############################################################################
# Load model and prediction
###############################################################################
# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph(model_save_meta_file)
saver.restore(sess, tf.train.latest_checkpoint(model_save_dir))

# Launch the graph in a session.
graph = tf.get_default_graph()

# Read each trained variables
X = graph.get_tensor_by_name("X:0")
prediction = graph.get_tensor_by_name("prediction:0")

# 시작시간 마킹
from datetime import datetime
start = datetime.now()

print(">> Label: ", label)
print(">> Prediction: ", sess.run(prediction, feed_dict={X: data_image}))

# 총 수행시간출력
print("Took time >>>>>>>> ", str(datetime.now() - start))

# Close session
sess.close()