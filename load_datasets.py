from tensorflow.keras.datasets import fashion_mnist, imdb, mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = imdb.load_data()
(x_train, y_train), (x_test, y_test) = mnist.load_data()
