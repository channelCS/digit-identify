# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 05:13:24 2018

@author: akshita
"""

import os
os.environ['KERAS_BACKEND']='tensorflow'
import keras
import os
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten,Input
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

batch_size = 128
num_classes = 10
epochs = 12
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# input image dimensions
img_rows, img_cols = 28, 28

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#Functional Api approach
inpx = Input(shape=input_shape,name='inpx')

x = Conv2D(filters=32,
           kernel_size=(3,3),
           data_format='channels_first',
           padding='same',
           activation='relu')(inpx)

hx = MaxPooling2D(pool_size=(2,2))(x)
h = Flatten()(hx)
wrap = Dense(128, activation='relu',name='wrap')(h)
score = Dense(num_classes,activation='softmax',name='score')(wrap)

model = Model([inpx],score)
model.summary()
model.compile(loss='categorical_crossentropy',
			  optimizer='adam',
			  metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


 


#save then model
model_json=model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)
    
model.save_weights("model.h5")
    

'''
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
'''
