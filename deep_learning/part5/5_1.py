# 5.1 간단한 커브넷 만들기
from keras import layers
from keras import models

model = models.Sequential()
# 컨볼루션 층
# output_depth = 32, 입력에 대해 32개의 필터를 적용함, 32개의 출력 채널이 발생
# 패치의 크기 = (3, 3), 입력에 대해 (3,3) 컨볼루션 연산 진행
# (28,28,1) = input의 크기를 지정, 28,28,1 크기의 특성맵을 입력을 받음 
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

model.add(layers.MaxPooling2D((2, 2)))
#컨볼루션층
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
'''
커브넷이 (image_height, image_width, image_channels) 크기의 입력텐서를 사용함
이 예제에서는 MNIST 이미지 포멧인 (28, 28, 1) 크기의 입력을 처리하도록 커브넷을 설정해야한다
그래서 입력층의 input_shape = (28, 28, 1)로 입
'''

# 5-2 컨브넷 위에 분류기 추가
# 완전연결층
model.add(layers.Flatten())
# 출력층
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
print(model.summary())

from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=64)


test_loss, test_acc = model.evaluate(test_images, test_labels)

print(test_acc)