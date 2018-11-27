'''
The following code is tacken from keras document
The code mainly focuss on the use of keras, thus, it is mainly based on dummy data
'''

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([
	Dense(32, input_shape=(784,)), 
	Activation('relu'), 
	Dense(10), 
	Activation('softmax')])

# alternative
##model = Sequential()
##model.add(Dense(32, input_shape=784))

# compile the model
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metric=['accuracy'])


# example: single input model with 10 classes
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
# Q: how to set lr?
# Q: how to combine multiple loss?
model.compile(
	optimizer='rmsprop', 
	loss='categorical_crossentropy', 
	metric=['accuracy'])

# Generate dummy numpy data
import numpy as np

data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)
model.fit(data, labels, epochs=10, batch_size=32)


'''VGG-like convnet'''
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

# Generate dummy data
x_train = np.random.random((100, 100, 100, 3))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
x_test = np.random.random((20, 100, 100, 3))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

# 
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
# 0.25 means the probability for drop?
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=1e-1, decay=1e-6, momentum=0.9, nesterov=True)
# why not specify metric?
model.compile(optimizer=sgd, loss='categorical_crossentropy')
model.fit(x_train, y_train, epochs=10, batch_size=32)
score = model.evaluate(x_test, y_test, batch_size=32)











