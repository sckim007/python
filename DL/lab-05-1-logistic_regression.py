"""
Logistic Regression
y = sigmoid(X @ W + b)
"""
import numpy as np

x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]

X_train = np.array(x_data, dtype=np.float32)
y_train = np.array(y_data).reshape(-1, 1)

N = X_train.shape[0]
D = X_train.shape[1]

C = 1
LEARNING_RATE = 0.1
MAX_ITER = 1000

W = np.random.standard_normal((D, C))
b = np.zeros((C,))


def sigmoid(x):
    """Sigmoid function """
    sigmoid = 1 / (1 + np.exp(-x))

    return sigmoid


def sigmoid_cross_entropy(logit, labels):
    """Compute a binary cross entropy loss
    z = logit = X @ W + b
    p = sigmoid(z)
    loss_i = y * - log(p) + (1 - y) * - log(1 - p)
    Args:
        logit (2-D Array): Logit array of shape (N, 1)
        labels (2-D Array): Binary Label array of shape (N, 1)
    Returns:
        float: mean(loss_i)
    """
    assert logit.shape == (N, C)
    assert labels.shape == (N, C)

    probs = sigmoid(logit)
    loss_i = labels * -np.log(probs + 1e-8)
    loss_i += (1 - labels) * -np.log(1 - probs + 1e-8)

    loss = np.mean(loss_i)

    return loss


def grad_sigmoid_cross_entropy(logit, labels):
    """Returns
    d_loss_i       d_sigmoid
    --------   *   ---------
    d_sigmoid      d_z
    z = logit = X * W + b
    Args:
        logit (2-D Array): Logit array of shape (N, 1)
        labels (2-D Array): Binary Label array of shape (N, 1)
    Returns:
        2-D Array: Backpropagated gradients of loss (N, 1)
    """
    return sigmoid(logit) - labels


def affine_forward(X, W, b):
    """Returns a logit
    logit = X @ W + b
    Args:
        X (2-D Array): Input array of shape (N, D)
        W (2-D Array): Weight array of shape (D, 1)
        b (1-D Array): Bias array of shape (1,)
    Returns:
        logit (2-D Array): Logit array of shape (N, 1)
    """
    return np.dot(X, W) + b


for i in range(MAX_ITER):

    logit = affine_forward(X_train, W, b)
    loss = sigmoid_cross_entropy(logit, y_train)
    d_loss = grad_sigmoid_cross_entropy(logit, y_train)

    d_W = np.dot(X_train.T, d_loss) / N
    d_b = np.sum(d_loss) / N

    W -= LEARNING_RATE * d_W
    b -= LEARNING_RATE * d_b

    if i % (MAX_ITER // 10) == 0:
        prob = affine_forward(X_train, W, b)
        prob = sigmoid(prob)
        pred = prob > 0.5
        acc = (pred == y_train).mean()

        print("[Step: {:5}] Loss: {:<5.3} Accuracy: {:>5.2%}".format(i, loss, acc))

print("Weight : ", W)
print("Bias   : ", b)
print("h(x) = {0}*x0 + {1}*x1 + {2}".format(W[0][0], W[1][0], b))

###############################################################################
# 학습 데이터 저장
###############################################################################
# Weight
np.save('./model_save_dir/0501-weight.npy', W)
# Bias
np.save('./model_save_dir/0501-bias.npy', b)

# Prediction for input value
def get_result_str (value):
    if value > 0.5:
        return "True"
    elif value < 0.5:
        return "False"
    else:
        return "Unknown"

test_data = [[1, 2]]
pred_value = (test_data[0][0] * W[0][0] + test_data[0][1] * W[1][0]) + b
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


for test_list_data in x_data:
    test_array_data = np.array(test_list_data) # list to np array
    pred_value = np.dot(test_array_data, W) + b
    print("{0}'s prediction = {1}({2})".format(test_list_data, pred_value, get_result_str(pred_value)))



