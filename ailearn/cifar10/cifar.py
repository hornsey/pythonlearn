import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train.shape:', X_train.shape)
print('y_train.shape:', y_train.shape)
print('X_train[0]:', X_train[0], '\ny_train[0]', y_train[0])


print('\n\n\n\n\n\n数据预处理')

height, width, nb_class = 32,32,10

# X部分做归一化
X_train = X_train/255
X_test = X_test/255

# 处理标签y
y_train = np_utils.to_categorical(y_train, nb_class)
y_test = np_utils.to_categorical(y_test, nb_class)

gen = ImageDataGenerator()

print('X_train.shape:', X_train.shape)
print('y_train.shape:', y_train.shape)
print('X_train[0]:', X_train[0], '\ny_train[0]', y_train[0])


print('\n\n\n\n\n搭建神经网络')

# 生成模型
model = Sequential()
# 添加输入层
model.add(Conv2D(32,3, padding='same', input_shape=X_train[1:], activation='relu'))
# 添加卷积和池化层
model.add(Conv2D(32, 3, activation = 'relu'))
model.add(MaxPool2D(2))
# 添加Dropout层
model.add(Dropout(0.25))

# 再添加卷积、池化和失活层
model.add(Conv2D(64, 3, padding='same', activation='relu'))
model.add(Conv2D(64, 3, activation='relu'))
model.add(MaxPool2D(2))
model.add(Dropout(0.25))

# 添加展示层
model.add(Flatten())

# 添加全连接层、失活层以及输出层
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_class, activation='softmax'))

model.summary()


        
