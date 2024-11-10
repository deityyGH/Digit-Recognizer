from tensorflow import keras
from keras import layers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
from sklearn.model_selection import train_test_split

train_data = pd.read_csv('input/train.csv')
test_data = pd.read_csv('input/test.csv')

X = train_data.copy()
X_test = test_data.copy()
y = X.pop('label')
  
X = X / 255.0
X_test = X_test / 255.0


X = X.values.reshape(X.shape[0], 28, 28, 1)
X_test = X_test.values.reshape(X_test.shape[0], 28, 28, 1)

y = to_categorical(y, num_classes=10)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=11)

datagen = ImageDataGenerator(
    rotation_range=5,
    zoom_range=0.10,
    width_shift_range=0.10,
    height_shift_range=0.10,
)

datagen.fit(X_train)

model = keras.Sequential()

model.add(layers.Conv2D(filters=32, kernel_size=(5,5), input_shape=(28,28,1), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.1))
model.add(layers.Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Dropout(0.1))

model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dropout(0.2))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))

model.add(layers.Dense(10, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


model.fit(datagen.flow(X_train, y_train, batch_size=128), epochs=30, validation_data=(X_valid, y_valid))

model.save('models/handwritten.keras')


