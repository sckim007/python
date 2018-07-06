"""
Logistic Regression
y = sigmoid(X @ W + b)
"""
import numpy as np

# Load weight and bias array
W = np.load('./model_save_dir/0501-weight.npy')
b = np.load('./model_save_dir/0501-bias.npy')

# Print weight and bias values
print("Road Weight : ", W)
print("Road Bias   : ", b)
print("h(x) = {0}*x0 + {1}*x1 + {2}".format(W[0][0], W[1][0], b))

# Prediction string for input value
def get_result_str(value):
    if value > 0.5:
        return "True"
    elif value < 0.5:
        return "False"
    else:
        return "Unknown"

# Prediction for manual input
test_data = [[1, 2]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("prediction value = ", pred_value)
print("[[1, 2]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))
test_data = [[2, 3]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("[[2, 3]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))
test_data = [[3, 1]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("[[3, 1]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))
test_data = [[4, 3]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("[[4, 3]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))
test_data = [[5, 3]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("[[5, 3]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))
test_data = [[6, 2]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
print("[[6, 2]] prediction = {0}({1})".format(pred_value, get_result_str(pred_value)))

# Prediction for array input
x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]

for test_list_data in x_data:
    test_array_data = np.array(test_list_data) # list to np array
    pred_value = np.dot(test_array_data, W) + b
    print("{0}'s prediction = {1}({2})".format(test_list_data, pred_value, get_result_str(pred_value)))



