'''
The following code is tacken from keras document
The code mainly focuss on the use of keras, thus, it is mainly based on dummy data
'''

from keras.layers import Input, Dense, Conv2D
from keras.models import Model

inputs = Input(shape=(784,))
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

model = Model(inputs=inputs, outputs=predictions)
##model.compile(optimizer='', loss='', metric='')
model.compile(
	optimizer='rmsprop', 
	loss='categorical_crossentropy', 
	metric=['accuracy'])
model.fit(data, labels)

# All models are callable, just like layers
x = Input(shape=(784,))
y = model(x)


## residual connection
x = Input(shape=(256, 256, 3))
y = Conv2D(3, (3, 3), activation='relu')(x)
output = keras.add([x, y])


## Inception model
from keras.layers import Conv2D, Maxpooling2D, Input

input_image = Input(shape=(256, 256, 3))
tower_1 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_image)
tower_1 = Conv2D(64, (3, 3), padding='same', activation='relu')(tower_1)

tower_2 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_image)
tower_2 = Conv2D(64, (5, 5), padding='same', activation='relu')(tower_2)

tower_3 = Maxpooling2D((3, 3), strides=(1,1), padding='same')(input_image)
tower_3 = Conv2D(64, (1, 1), padding='same', activation='relu')(tower_3)

output = keras.layers.concatnate([tower_1, tower_2, tower_3], axis=1)





















