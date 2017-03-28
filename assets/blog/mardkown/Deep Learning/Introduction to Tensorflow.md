Tensorflow is an open source software library for numerical computation using data flow graphs. It was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

## How to install Tensorflow
Installation for tensorflow is really easy. Based on my experience of installation on my mac, it is far easier than Caffe which is another deep learning framework.
### Environment
This tutorial is based on:

- Mac OSX 10.12.1
- python 3.6.0
- Tensorflow 1.0 release

### Installation of python virtual environment
Python usually has a lot of different versions which is always a headache for beginners, especially you have projects with different dependencies of various versions of python.
To solve this problem, I recommend you use python version manager such as `virtualenv`, `pyenv` and `conda`.
In this tutorial, I use `conda` as an example.
You can refer to this link for more information: [Help Docs for Conda](https://conda.io/docs/get-started.html)

- install Anaconda, download it from: [Downloads of Anaconda](https://www.continuum.io/downloads). And install it follow the instructions of this website. This is an GUI version which is more user-friendly. 

-  Open your terminal and test if you can use conda:

```bash
$ conda -V
conda 4.2.13 # output
```
-  create a new virtual environment for Tensorflow

```bash
$ conda create -name <yourenvname> python=3.6
```
-  switch to virtual environment you just created

```bash
$ source activate <yourenvname>
$ python -V # use it to check the current version
Python 3.6.0 # output
```
Here you have created a new virtual envronment ready for installation of Tensorflow. And you will find the name of python env appears at the beginning of your command line:

```bash
(<yourenvname>) $ # your command
```
### Installation of Tensorflow
-  Then you can install tensorflow in your virtual environment with just one command! Suppose the name of this environment is:`tensorlfow`

```bash
(tensorlfow) $ conda install tensorflow
```
- You are all set! You can run python script in your command line to test whether it will work, but I recommend to use spider mentioned in the next section.

**Note:** If you want to exit your virtual environment, you can simply type `source deactivate` in your terminal.

## Test your tensorflow
-  Open your anaconda, then you will find your virtualenv here:
![Screen Shot 2017-03-28 at 17.30.50](/assets/blog/article_img/Screen%20Shot%202017-03-28%20at%2017.30.50.png)
choose tensorflow (you should choose your virtual environment you just created) and then install "spyder" in the panel.
- Lauch spyder and try to run the script below:

```py
'''
A linear regression learning algorithm example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

from __future__ import print_function

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50

# Training Data
train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    # Testing example, as requested (Issue #2)
    test_X = numpy.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
    test_Y = numpy.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])

    print("Testing... (Mean square loss Comparison)")
    testing_cost = sess.run(
        tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing cost=", testing_cost)
    print("Absolute mean square loss difference:", abs(
        training_cost - testing_cost))

    plt.plot(test_X, test_Y, 'bo', label='Testing data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
```
- If you can get the result of this linear regression then you are done!

Have fun with it!






