# 데이터 증식
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras.preprocessing import image

# 5-13 데이터 증식을 활용하여 새로운 컨브넷 만들기

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
# 적은수의 원본이미지에서 만들어졌기 때문에 여전히 입력데이터들 사이 상호연관성이 큼
# 연결 분류기 직전 Dropout층을 추가하여 과대적합을 억제
# 과대적합(overfitting)은 모델이 훈련데이터에 너무 잘 맞지만 일반성이 떨어진다는 의미, 
# 너무 훈련데이터에 맞추어져 있기 때문에 훈련데이터의 다양한 변수에는 대응하기 힘들어짐
# Dropout이란 말 그대로 네트워크의 일부를 생략하는것이다. 학습 사이클이 진행되는동안 무작위로 일부 뉴런을 생략함

model.add(layers.Dropout(0.5))  
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# 5-14 데이터 증식 제너레이터를 사용하여 컨브넷 훈련하기
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=40,        # 랜덤하게 사진을 회전시킬 각도 범위
      width_shift_range=0.2,    # 사진을 수평으로 랜덤하게 평행이동
      height_shift_range=0.2,   # 사진을 수직으로 랜덤하게 평행이동
      shear_range=0.2,          # 랜덤하게 shearing transformation을 적용할 각도 범위
      zoom_range=0.2,           # 랜덤하게 사진을 확대
      horizontal_flip=True)     # 랜덤하게 이미지를 수평으로 뒤집음


# 검증 데이터는 증식되어서는 안 됩니다!
test_datagen = ImageDataGenerator(rescale=1./255)

train_dir = './datasets/cats_and_dogs_small/train'
validation_dir = './datasets/cats_and_dogs_small/validation'

train_generator = train_datagen.flow_from_directory(
        # 타깃 디렉터리
        train_dir,
        # 모든 이미지를 150 × 150 크기로 바꿉니다
        target_size=(150, 150),
        batch_size=32,
        # binary_crossentropy 손실을 사용하기 때문에 이진 레이블을 만들어야 합니다
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

history = model.fit_generator(
      train_generator,
      steps_per_epoch=100,
      epochs=20,
      validation_data=validation_generator,
      validation_steps=50)

model.save('cats_and_dogs_small_2.h5')

# 데이터 증식을 사용했을때 훈련 정확도와 검증 정확도
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()