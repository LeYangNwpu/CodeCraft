'''
Reference:
https://zhuanlan.zhihu.com/p/30487008
'''
# begin tensorflow
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow')
sess = tf.Session()
print(sess.run(hello))

# tf with constant
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
	print('a=2, b=3')
	print('Addition with constants: '% sess.run(a+b))
	print('Multiplication  with constants: ' % sess.run(a*b))

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
	print('Multiplication with constant matrixs: ' % sess.run(product))


# tf with placeholder
import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.mul(a, b)
with tf.Session() as sess:
	print('Addition with variables: ', sess.run(add, feed_dict={a:2, b:3}))
	print('Multiplication with variables: ', sess.run(mul, feed_dict={a:2, b:3}))
	

# Linear regression
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

# parameters
learning_rate = 0.01
training_epochs = 2000
display_step = 50

# training data
train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

# tf graph input
# tf.float or "float"?
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# create model
# set model weight
W = tf.variable(rng.randn(), name='weight')
b = tf.variable(rng.randn(), name='bias')
# construct a linear model
# is tf.mul(X, W) same as tf.mul(W, X)?
activation = tf.add(tf.mul(X, W), b)

# minimize the squared error
cost = tf.reduce_sum(tf.pow(activation-Y, 2)) / (2*n_samples)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# initialize the variables
init = tf.initialize_all_variables()

# launch the graph
with tf.Session() as sess:
	sess.run(init)
	
	# fit all training data
	for epoch in range(training_epochs):
		for x, y in zip(train_X, train_Y):
			sess.run(optimizer, feed_dict={X: x, Y: y})
		
		# Diaplay logs per epoch step
		if epoch % display_step == 0:
			print('Epoch: ', '%04d' % (epoch+1), 'cost=', \
			'{:.9f}'.format(sess.run(cost, feed_dict={X:train_X, Y:train_Y})), \
			'W=', sess.run(W), 'b=', sess.run(b))
			
	print('Optimization Finished!')
	print('cost=', sess.run(cost, feed_dict={X:train_X, Y:train_Y}), \
		'W=', sess.run(W), 'b=', sess.run(b))
	
	# Graphic display
	plt.plot(train_X, train_Y, 'ro', label='Original data')
	# is this fifty points or a line?
	plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
	plt.legend()
	plt.show()
		

# logistic regression

import tensorflow as tf
# MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)

# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# tf.float or "float"?
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])

# create model
# set model weight
# what about name='***'?
W = tf.variable(tf.zeros([784, 10]), name='weight')
b = tf.variable(tf.zeros([10]), name='bias')

pred = tf.nn.softmax(tf.matmul(X, W) + b)
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(pred), reduction_indices=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# initialize the variables
init = tf.initialize_all_variables()

# launch the graph
with tf.Session() as sess:
	sess.run(init)
	
	# training cycles
	for epoch in training_epochs:
		avg_cost = 0
		total_batch = int(mnist.train.number_examples/batch_size)
		
		for i in range(total_batch):
			batch_xs, batch_ys = mnist.train.next_batch(batch_size)
			# run optimization and cost op to get the value
			_, cost = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
			
			# average loss
			avg_cost += cost/total_batch
		
		# Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
	
	print('Optimization Finished')
	
	# Test model
	correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(Y, 1))
	# Calculate accuracy
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print('Accuracy:', accuracy.eval({X: mnist.test.images, Y: mnist.test.labels}))
		
	