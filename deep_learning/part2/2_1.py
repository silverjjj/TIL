'''
이번 예제의 경우 케라스를 완벽하게 이해하지 않아도 된다.
이번 예제는 케라스의 전체적인 구성과 코드의 흐름만 파악하도록 하자 
'''
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# 2-1 케라스에서 MNIST 데이터셋 적제하기
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()

'''
MNIST 데이터셋은 넘파이 배열형태로 케라스에 이미 포함되어있음
'''

# 2-2 이미지 데이터 준비하기
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

'''
훈련을 시작하기전 데이터를 네트워크에 맞는 크기로 바꾸고, 모든 값을 0과 1 사이로 스케일을 조정한다.
예를 들어 앞서 우리의 훈련이미지는 [0, 255] 사이의 값인 unit8타입의 (60000, 28, 28) 크기의 배열로 저장되어있다.
이 데이터를 0과 1사이의 값을 가지는 float32 타입의 (60000, 28*28) 크기인 데이터로 변환
'''

# 2-3 신경망 구조
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

'''
신경망의 핵심 구성요소는 데이터 처리 필터인 layer(층)이라고 할수있다.
신경망층인 Dence층 2개가 연속되어, 두번째 층은 10개의 확률점수가 들어있는 배열을 반환하는
softmax 층입니다.
'''

# 2-4 컴파일 단계
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

'''
신경망이 훈련을 마치기 위해 컴파일 단계에서 3가지가 더 필요
손실함수(loss fuction) : 훈련데이터에서 신경망의 성능을 측정하는방법으로 네트워크가 옳은 방향으로 학습될수있도록 도와줌
옵티마이저(optimizer) : 입력된 데이터와 손실함수를 기반으로 네트워크를 업데이트하는 메커니즘
훈련과 테스트 과정을 모니터링할 지표 : 여기에서는 정확도만 고려하겠습니다.
'''

# 2-5 레이블 준비하기
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

'''
이부분은 3장에서 자세히할 예정
'''

network.fit(train_images, train_labels, epochs=5, batch_size=128)
'''
fit 메서드를 호출하여 훈련데이터에 모델을 학습시킴
네트워크가 128개 샘플씩 미니배치로 훈련데이터를 다섯번 반복합니다.
각 반복마다 네트워크가 배체에서 손실에 대한 가중치의 그래디언트를 계산하고 가중치응 업데이트해 나갑니다.
1번의 에포크동안 469번의 그래디언트 업데이트를 수행합니다. (6만개의 훈련데이터를 128개씩 배치를 나누면 469개의 배치가 만들어진다.)
'''
print("========================================================")

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)