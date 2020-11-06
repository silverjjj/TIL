'''
영화리뷰분류 : 이진분류 예제
'''
from keras.datasets import imdb
import numpy as np
from keras import models
from keras import layers
import matplotlib.pyplot as plt

# 1. 학습을 위한 입력형식만들기
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# 정수 시퀀스를 이진행렬로 변환
def vectorize_sequences(sequences, dimension=10000):
    # 크기가 (len(sequences), dimension))이고 모든 원소가 0인 행렬을 만듭니다
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # results[i]에서 특정 인덱스의 위치를 1로 만듭니다
    return results

# 훈련 데이터를 벡터로 변환합니다
x_train = vectorize_sequences(train_data)
# 테스트 데이터를 벡터로 변환합니다
x_test = vectorize_sequences(test_data)

# 레이블을 벡터로 바꿉니다
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# 2-1. original 모델 만들기
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

origin_history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))
origin_dict = origin_history.history
print(origin_dict)
# 2-2 small 모델 만들기
model = models.Sequential()
model.add(layers.Dense(6, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(6, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

small_history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))
                    
small_dict = small_history.history

model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

large_history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))
large_dict = large_history.history
# acc = origin_dict['acc']
val_loss = origin_dict['val_loss']
val2_loss = small_dict['val_loss']
val3_loss = large_dict['val_loss']
epochs = range(1,21)
# ‘bo’는 파란색 점을 의미합니다
plt.plot(epochs, val2_loss, 'b', label='small model')
# ‘b’는 파란색 실선을 의미합니다
plt.plot(epochs, val_loss, 'r', label='origin model')
plt.plot(epochs, val3_loss, 'g', label='large model')
plt.title('origin, small, large model validation')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()