# 로이터 데이터셋 로드하기
from keras.datasets import reuters
import numpy as np
from keras.utils.np_utils import to_categorical
from keras import models
from keras import layers

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

# 훈련 데이터 벡터 변환
x_train = vectorize_sequences(train_data)
# 테스트 데이터 벡터 변환
x_test = vectorize_sequences(test_data)

# 레이블을 벡터로 변환합니다.
one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)


# 모델 정의하기
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
# 마지막층에 softmax를 사용하여 클래스의 확률 분포를 출력합니다. 
model.add(layers.Dense(46, activation='softmax'))

# 모델 컴파일 하기
# model.compile(optimizer='rmsprop',
#                 # 정수레이블을 사용할때는 아래 손실함수를 사용합니다.
#                 # 수학적으로는 categorical_crossentropy와 같습니다
#                 loss='sparse_categorical_crossentropy',
#                 metrics=['acc'])


model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 훈련과 검증데이터로 나눕니다.
x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

# model.fit(partial_x_train,
#           partial_y_train,
#           epochs=9,
#           batch_size=512,
#           validation_data=(x_val, y_val))
model.fit(partial_x_train,
                    partial_y_train,
                    epochs=9,
                    batch_size=512,
                    validation_data=(x_val, y_val))

results = model.evaluate(x_test, one_hot_test_labels)

print(results)

predictions = model.predict(x_test)

print(predictions[0].shape)
print(predictions)