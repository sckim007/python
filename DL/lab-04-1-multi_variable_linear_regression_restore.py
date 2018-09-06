# Lab 4 Multi-variable linear regression
import tensorflow as tf

x1_data = [73., 93., 89., 96., 73.]
x2_data = [80., 88., 91., 98., 66.]
x3_data = [75., 93., 90., 100., 70.]

y_data = [152., 185., 180., 196., 142.]

# Create session with enabled gpu option
config=tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Restore trained model's variable
saver = tf.train.import_meta_graph('./model_save_dir/0401-linear.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model_save_dir'))

# Launch the graph in a session.
graph = tf.get_default_graph()

# Read each trained variables
RX1 = graph.get_tensor_by_name("holder_x1:0")
RX2 = graph.get_tensor_by_name("holder_x2:0")
RX3 = graph.get_tensor_by_name("holder_x3:0")
#RWeight = graph.get_tensor_by_name("weight:0")
#RBias = graph.get_tensor_by_name("bias:0")
RHypothesis = graph.get_tensor_by_name("hypothesis:0")

# 시작시간 마킹
import time
start = time.time()
time.sleep(1)

# Ask prediction for input value.
i = 0
for _ in y_data:
    print(i, "st prediction = ", sess.run(RHypothesis, feed_dict={RX1:x1_data[i], RX2:x2_data[i], RX3:x3_data[i]}))
    i += 1

# Close session
sess.close()

# 총 수행시간출력
print("Took time >>>>>>>> ", str(time.time() - start))