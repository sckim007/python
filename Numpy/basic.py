'''
Extension to python for multi-dimensional arrays
Efficiency
For scientific computing
import numpy
'''

import numpy as np

list = [1,2,3,4]
ary=np.array(list)
print(type(list))
print(type(ary))
"""
<class 'list'>
<class 'numpy.ndarray'>
"""

print(list)
print(ary)

print(ary)
"""
[1, 2, 3, 4]
[1 2 3 4]
"""

'''
Creating Array with List/array
'''
d2 = np.array([[0,1,2],[3,4,5]])
print(d2)
print(d2.shape)
"""
[[0  1  2]
 [3  4  5]]
 (2, 3)
"""

d3 = np.array([d2, d2])
print(d3)
print(d3.shape)
"""
[[[0 1 2]
  [3 4 5]]

 [[0 1 2]
  [3 4 5]]]
(2, 2, 3)  
"""

'''
Create special array
np.arange(START,END,STEP): evenly spaced values within a given interval
np.linspace(START,END, NUM_OF_POINTS) : evenly spaced numbers over a specified interval
np.ones(SHAPE,TYPE) : a new array of given shape and type, filled with ones
np.zeros(SHAPE,TYPE) : a new array of given shape and type, filled with zeros
np.eye(ROWS,COLS) : a 2-D array with ones on the diagonal and zeros elsewhere
np.diag(ARRAY) : extract a diagonal or construct a diagonal array
'''
print(np.arange(5))
'''
[0 1 2 3 4]
'''
print(np.linspace(0, 1, 5))
'''
[0.   0.25 0.5  0.75 1.  ]
'''
# 모든 값이 1인 배열 생성
print(np.ones((2, 2)))
'''
[[1. 1.]
 [1. 1.]]
 '''
# 모든 값이 특정 상수인 배열 생성
print("============================")
print(np.full((2,2), 7))
'''
[[7 7]
 [7 7]]
'''
# 모든 값이 0인 배열 생성
print(np.zeros((2, 2)))
'''
[[0. 0.]
 [0. 0.]]
 '''
# 2x2 단위행렬 생성
print(np.eye(2))
'''
[[1. 0.]
 [0. 1.]]
 '''
print(np.diag([1, 2]))
'''
[[1 0]
 [0 2]]
 '''

'''
Random Array
np.random.rand(SHAPE) : random values in a given shape
np.random.randn(SHAPE) : normal distribution
try help(np.random)
'''
print(np.random.rand(5))
'''
[0.62376518 0.70172157 0.03102505 0.3753287  0.32457032]
'''
print(np.random.randn(5))
'''
[ 0.34900741 -0.1596873   1.94593245 -0.07410363 -0.11105143]
'''

'''
Data type of array values
Default type is float
'''
print(np.array([1, 2, 3]).dtype)
'''
int32
'''
print(np.array([1, 2, 3], dtype=float).dtype)
'''
float64
'''
print(np.array([1., 2, 3]).dtype)
'''
float64
'''
print(np.array([1+1j, 2+2j, 3+3j]).dtype)
'''
complex128
'''

'''
Indexing
- Use [] operator
- [x,y] for 2D array
- [x,y,z] for 3D array
'''
print(np.arange(10))
'''
[0 1 2 3 4 5 6 7 8 9]
'''
d = np.random.rand(3, 3)
print(d)
'''
[[0.9657631  0.4363726  0.37481362]
 [0.35722475 0.97664702 0.35455862]
 [0.20181833 0.72994413 0.04246434]]
'''
print(d.shape)
'''
(3, 3)
'''
print(np.diag(d))
'''
[0.9657631  0.97664702 0.04246434]
'''
d = np.random.rand(3, 3, 3)
print(d)
'''
[[[0.26874552 0.78878806 0.69732077]
  [0.8727247  0.30045889 0.30554777]
  [0.54841527 0.24135581 0.93080064]]

 [[0.12553842 0.52524688 0.63004087]
  [0.89886812 0.51711959 0.58392531]
  [0.44938961 0.52494796 0.86683466]]

 [[0.83622718 0.71696502 0.58372824]
  [0.97465486 0.77192595 0.60447509]
  [0.78233753 0.40957493 0.11404227]]]
'''
print(d.shape)
'''
(3, 3, 3)
'''

'''
Slicing
- Use[::] operator
- [x_start:x_end:x_step, y_start:y_end:y_step] for 2D array
'''
a = np.arange(10)
print(a)
'''
[0 1 2 3 4 5 6 7 8 9]
'''
print(a[5:8])
'''
[5 6 7]
'''
a[5:8]=10
print(a)
'''
[ 0  1  2  3  4 10 10 10  8  9]
'''
b = np.reshape(np.arange(16), (4,4))
print(b)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
print(b[1:3, 1:3])
'''
[[ 5  6]
 [ 9 10]]
 '''
print(b[:2, :2])
'''
[[0 1]
 [4 5]]
'''
print(b[::2, ::2])
'''
[[ 0  2]
 [ 8 10]]
 '''

'''
Slicing
- A slicing operation creates a view on the original array.
  . The original array is now copied.
'''
a = np.arange(10)
print(a)
'''
[0 1 2 3 4 5 6 7 8 9]
'''
b = a[::2]
print(b)
'''
[0 2 4 6 8]
'''
b[2]=999
print(b)
'''
[  0   2 999   6   8]
'''
print(a)
'''
[  0   1   2   3 999   5   6   7   8   9]
'''
print(np.may_share_memory(a, b))
'''
True
'''
c=b.copy()
print(np.may_share_memory(b, c))
'''
False
'''
c[2] = 1
print(b)
'''
[  0   2 999   6   8]
'''
print(c)
'''
[0 2 1 6 8]
'''

'''
Slicing
- Boolean mask
  . the sub-array is copied from the original array
'''
a = np.arange(20)
print(a % 3 == 0)
'''
[ True False False  True False False  True False False  True False False
  True False False  True False False  True False]
'''
print(a[a % 3 == 0])
'''
[ 0  3  6  9 12 15 18]
'''
a[a % 3 == 0] = 1
print(a)
'''
[ 1  1  2  1  4  5  1  7  8  1 10 11  1 13 14  1 16 17  1 19]
'''

'''
Slicing
- Indexing with an array
  . Extract a sub-array with the indexing array
    . the sub-array is copied from the original array.
'''
a = np.arange(20) * 10
print(a)
'''
[  0  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170
 180 190]
'''
print(a[[5, 7, 9]])
'''
[50 70 90]
'''
a[[5, 7, 9]] = -1
print(a)
'''
[  0  10  20  30  40  -1  60  -1  80  -1 100 110 120 130 140 150 160 170
 180 190]
'''

'''
Basic Operations
Arithmetic
  - +, -, *, **
'''
a = np.arange(5)
print(a)
'''
[0 1 2 3 4]
'''
b = np.arange(2, 7)
print(b)
'''
[2 3 4 5 6]
'''
print(a+1)
'''
[1 2 3 4 5]
'''
print(a**2)
'''
[ 0  1  4  9 16]
'''
print(a+b)
'''
[ 2  4  6  8 10]
'''
print(a * b)
'''
[ 0  3  8 15 24]
'''

'''
Basic Operations
Logical
  ==, >, <, np.logical_or, np.logical_and
'''
a = np.array([0, 1, 2, 3, 4, 5])
b = np.array([1, 0, 2, 5, 3, 4])
print(a == b)
'''
[False False  True False False False]
'''
print(a > b)
'''
[False  True False False  True  True]
'''
print(np.logical_and(a, b))
'''
[False False  True  True  True  True]
'''
print(np.logical_or(a, b))
'''
[ True  True  True  True  True  True]
'''

'''
Simple Statistics
  - np.sum, np.min, np.argmin, np.all, np.any, np.mean, np.median, np.std
'''
a = np.arange(10)
print("sum = {}".format(np.sum(a)))
print("min = {}".format(np.min(a)))
print("max = {}".format(np.max(a)))
print("argmin = {}".format(np.argmin(a)))
print("mean = {}".format(np.mean(a)))
print("median = {}".format(np.median(a)))
print("std = {}".format(np.std(a)))
print("all = {}".format(np.all(a)))
print("any = {}".format(np.any(a)))
'''
sum = 45
min = 0
max = 9
argmin = 0
mean = 4.5
median = 4.5
std = 2.8722813232690143
all = False
any = True
'''

'''
Broadcasting
'''
a = np.array([[0, 0, 0],[10, 10, 10], [20, 20, 20],[30, 30, 30]])
b = np.array([0, 1, 2])
print(a)
'''
[[ 0  0  0]
 [10 10 10]
 [20 20 20]
 [30 30 30]]'''
print(b)
'''
[0 1 2]
'''
print(a + b)
'''
[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
'''
a = np.array([[0], [10], [20], [30]])
print(a)
'''
[[ 0]
 [10]
 [20]
 [30]]
'''
print(a + b)
'''
[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
'''

'''
Array Reshape
  - array.T, np.reshape()
'''
a = np.array([[1, 2, 3], [4, 5, 6]])
print("array a = \n{}".format(a))
'''
array a = 
[[1 2 3]
 [4 5 6]]
 '''
b = a.T
print('array a.T=\n{}'.format(b))
'''
array a.T=
[[1 4]
 [2 5]
 [3 6]]
'''
print("array a's shape : {}".format(a.shape))
'''
array a's shape : (2, 3)
'''
print("array a's reshape = \n{}".format(a.reshape((3,2))))
'''
array a's reshape =
[[1 2]
 [3 4]
 [5 6]]
'''
print("array a's reshape = \n{}".format(a.reshape((3,-1))))
'''
array a's reshape = 
[[1 2]
 [3 4]
 [5 6]]
'''
print(np.arange(4*4).reshape((4,4)))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''

'''
Linear Algebra
  - Matrix Multiplication, np.dot(), np.linalg.multi_dot()
'''
a = np.arange(9).reshape((3,3))
print("array a = \n{}".format(a))
'''
array a = 
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print("array a * a = \n{}".format(a * a))
'''
array a * a = 
[[ 0  1  4]
 [ 9 16 25]
 [36 49 64]]
'''
print("array a dot = \n{}".format(np.dot(a, a)))
'''
array a dot = 
[[ 15  18  21]
 [ 42  54  66]
 [ 69  90 111]]
'''
a = np.arange(6).reshape((2, 3))
b = np.arange(15).reshape((3, 5))
c = np.arange(10).reshape((5, 2))
print("multi_dot(a,b,c) = \n{}".format(np.linalg.multi_dot([a, b, c])))
'''
multi_dot(a,b,c) = 
[[ 680  835]
 [2120 2590]]
'''

'''
Linear Algebra  : ??????????????????
  - np.inner(), np.outer(), np.linalg.matrix_power(M,n)
'''
a = [1, 2]
b = [2, 3]
print(np.inner(a, b))
'''
8
'''
print(np.outer(a, b))
'''
[[2 3]
 [4 6]]
'''
m = [[1, 2], [3, 4]]
print(np.linalg.matrix_power(m, 10))
'''
[[ 4783807  6972050]
 [10458075 15241882]]
'''

'''
Linear Algebra  : ??????????????????
  - Eigenvalue, eigenvector: np.linalg.eig()
  - Determinant: np.linalg.det()
  - Inverse of a Matrix: np.linalg.inv()
'''
a = np.arange(4).reshape((2, 2))
print(a)
'''
[[0 1]
 [2 3]]
'''
print(np.linalg.eig(a))
'''
(array([-0.56155281,  3.56155281]), array([[-0.87192821, -0.27032301],
       [ 0.48963374, -0.96276969]]))
'''
print(np.linalg.det(a))
'''
-2.0
'''
print(np.linalg.inv(a))
'''
[[-1.5  0.5]
 [ 1.   0. ]]
'''
print(np.dot(np.linalg.inv(a), a))
'''
[[1. 0.]
 [0. 1.]]
'''

'''
Linear Algebra  : ??????????????????
  - np.linalg.solve() : Solve a system of linear equations
'''
a = np.array([[3, 1],[1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
print(x)
'''
[[1. 0.]
 [0. 1.]]
[2. 3.]
'''
print(np.allclose(np.dot(a,x),b))
'''
True
'''

'''
-------------------------------------------------------------------------------
File
   - np.loadtxt()
     . Load data from a text file.
     . Each row in the text file must have the same number of values.
     ref : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.loadtxt.html
-------------------------------------------------------------------------------
'''
from io import StringIO
c = StringIO('0 1\n2 3')
print(np.loadtxt(c))
'''
[[0. 1.]
 [2. 3.]]
'''
d = StringIO('M 21 72\nF 35 58')
print(np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
                           'formats': ('S1', 'i4', 'f4')}))
'''
[(b'M', 21, 72.) (b'F', 35, 58.)]
'''



