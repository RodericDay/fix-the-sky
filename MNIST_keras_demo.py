import numpy as np 
np.random.seed(123)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from matplotlib import pyplot as plt


# get data
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print (X_train.shape)
plt.imshow(X_train[0])

#plt.show()


#reshape data - ATTN to which backend is being used: https://stackoverflow.com/questions/41651628/negative-dimension-size-caused-by-subtracting-3-from-1-for-conv2d

#theano
#X_train = X_train.reshape(X_train.shape[0],1,28,28)
#X_test = X_test.reshape(X_test.shape[0],1,28,28)

#tf
X_train = X_train.reshape(X_train.shape[0],28,28,1)
X_test = X_test.reshape(X_test.shape[0],28,28,1)


print(X_train.shape)


X_train =X_train.astype('float32')

X_test = X_test.astype('float32')

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

print(Y_train.shape)


#build some layers
model = Sequential()

#theano
#model.add(Convolution2D(32,3,3,activation = 'relu',input_shape=(1,28,28)))

#tf
model.add(Convolution2D(32,3,3,activation = 'relu',input_shape=(28,28,1)))

print (model.output_shape)

model.add(Convolution2D(32,3,3,activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

#compile and train model
model.compile(loss= 'categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,Y_train,batch_size=32, nb_epoch=5,verbose=1)

score = model.evaluate(X_test, Y_test, verbose = 0)
print(score)