from keras.datasets import imdb
from keras import preprocessing
from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

max_features = 10000
maxlen = 20

# IMDB 데이터(리뷰데이터)에서 빈도수가 높은 1만개의 단어를 추출하고 최대 길이를 20으로 제한하여 추출합니다.
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
# pad_sequences : 리스트를 2D 정수 텐서로 변환
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen= maxlen)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen= maxlen)



model = Sequential()
# Embedding 층 : 1만개의 단어에 대해 8차원의 임베딩 학습하여 정수 시퀀수(2D 정수 텐서)에서 임베딩 시퀀스(3D 실수형 텐서)로 변환
model.add(Embedding(10000, 8, input_length = maxlen))

# 2D로 펼쳐서 분류를 위한 Dense층을 훈련준비
model.add(Flatten())

model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

model.summary()

model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

