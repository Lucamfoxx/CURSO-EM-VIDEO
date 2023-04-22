import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Carrega o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normaliza as imagens
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Adiciona uma dimensão para as imagens em escala de cinza
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

# Cria o modelo CNN
model = keras.Sequential(
    [
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(10, activation="softmax"),
    ]
)

# Compila o modelo
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Treina o modelo
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Avalia o modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc}")
