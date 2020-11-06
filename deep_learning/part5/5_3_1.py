# 사전에 훈련된 컨브넷, 데이터 증식을 사용한 컨브넷
from keras.applications import VGG16
from keras import models
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras import optimizers
import os
import numpy as np

train_dir = './datasets/cats_and_dogs_small/train'
validation_dir = './datasets/cats_and_dogs_small/validation'
test_dir = './datasets/cats_and_dogs_small/test'

# 데이터 증식
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.1,
      height_shift_range=0.1,
      shear_range=0.1,
      zoom_range=0.1,
      horizontal_flip=True,
      fill_mode='nearest')
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        # 모든 이미지의 크기를 150 × 150로 변경합니다
        target_size=(256, 256),
        batch_size=20,
        # binary_crossentropy 손실을 사용하므로 이진 레이블이 필요합니다
        class_mode='binary')
validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(256, 256),
        batch_size=20,
        class_mode='binary')

# 테스트데이터로 모델 평가
test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(256, 256),
        batch_size=20,
        class_mode='binary')
        

# VGG16 model
model = models.Sequential()w
conv_base = VGG16(weights='imagenet',
                  include_top=False,  # 모든층 동결
                  input_shape=(256, 256, 3))
# #  합성곱 기반층 위에 완전 연결 분류기 추가한뒤 컴파일
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=2e-5),
              metrics=['acc'])
history = model.fit_generator(
      train_generator,
      steps_per_epoch=100,
      epochs=1,
      validation_data=validation_generator,
      validation_steps=50,
      verbose=2)

# # 미세조정 진행
# conv_base.trainable = True
# set_trainable = False
# for layer in conv_base.layers:
#     if layer.name == 'block5_conv1':
#         set_trainable = True
#     if set_trainable:
#         layer.trainable = True
#     else:
#         layer.trainable = False

# model.compile(loss='binary_crossentropy',
#               optimizer=optimizers.RMSprop(lr=1e-5),
#               metrics=['acc'])

# history = model.fit_generator(
#       train_generator,
#       steps_per_epoch=100,
#       epochs=100,
#       validation_data=validation_generator,
#       validation_steps=50)

# model.save('cats_and_dogs_small_4.h5') # 미세조정이후의 모델

# train_loss, train_acc = model.evaluate_generator(train_generator, steps=50)
# test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
# print('train_acc:', train_acc)
# print('test acc:', test_acc)


# # 그래프 시각화
# def smooth_curve(points, factor=0.8):
#   smoothed_points = []
#   for point in points:
#     if smoothed_points:
#       previous = smoothed_points[-1]
#       smoothed_points.append(previous * factor + point * (1 - factor))
#     else:
#       smoothed_points.append(point)
#   return smoothed_points

# plt.plot(epochs,
#          smooth_curve(acc), 'bo', label='Smoothed training acc')
# plt.plot(epochs,
#          smooth_curve(val_acc), 'b', label='Smoothed validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs,
#          smooth_curve(loss), 'bo', label='Smoothed training loss')
# plt.plot(epochs,
#          smooth_curve(val_loss), 'b', label='Smoothed validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.show()
