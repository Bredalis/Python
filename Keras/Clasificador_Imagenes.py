# Set de datos: MNIST
# 
# Contiene 60,000 datos de entrenamiento y 10,000 de validacion.
# Cada imagen es de 28x28 pixeles. La clasificacion se llevara a cabo
# Usando una red neuronal con una capa oculta que contiene 15 neuronas. 

# Importar librerias

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.utils import np_utils

import matplotlib.pyplot as plt
import numpy as np

# Lectura, visualizacion y pre-procesamiento de los datos

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Visualizaremos 16 imagenes aleatorias tomadas del set x_train

ids_imgs = np.random.randint(0, x_train.shape[0], 16)

for i in range(len(ids_imgs)):

	img = x_train[ids_imgs[i], :, :]

	plt.subplot(4, 4, i+1)
	plt.imshow(img, cmap = 'gray')
	plt.axis('off')
	plt.title(y_train[ids_imgs[i]])

plt.suptitle('16 imagenes del set MNIST')
plt.show()

# Pre-procesamiento: para introducir a la red neuronal debemos
# "aplanar" cada una de las imagenes con un vector de 28x28 = 780 valores

X_train = np.reshape( x_train, (x_train.shape[0], x_train.shape[1]*x_train.shape[2]) )
X_test = np.reshape( x_test, (x_test.shape[0], x_test.shape[1]*x_test.shape[2]) )

# Adicionalmente se normalizaran las intensidades al rango 0-1

X_train = X_train/255.0
X_test = X_test/255.0

# Finalmente, convertimos y_train y y_test a representacion "one-hot"

nclasses = 10
Y_train = np_utils.to_categorical(y_train, nclasses)
Y_test = np_utils.to_categorical(y_test, nclasses)

# Creacion del modelo:
# -- Capa de entrada: su dimension sera 784 (el tamaño de cada imagen aplanada)
# -- Capa oculta: 15 neuronas con activacion
# -- Capa de salida: funcion de activacion  ReLU
# total de 10 categorias

np.random.seed(1) # Para reproducibilidad del entrenamiento
input_dim = X_train.shape[1]
output_dim = Y_train.shape[1]

modelo = Sequential()
modelo.add( Dense(15, input_dim = input_dim, activation = 'relu') )
modelo.add( Dense(output_dim, activation = 'softmax') )
print(modelo.summary())

# Compilacion y entrenamiento: gradiente descendente, learning rate = 0.05, funcion
# de error: entropia cruzada, metrica de desempeño: precision 

sgd = SGD(lr = 0.2)
modelo.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])

# Para el entrenamiento se usaran 30 iteraciones y un batch_size de 1024

num_epochs = 50
batch_size = 1024
historia = modelo.fit(X_train, Y_train, epachs = num_epochs, batch_size = batch_size, verbose = 2)

# Resultados

# Error y precision vs iteraciones

plt.subplot(1,2,1)
plt.plot(historia.history['loss'])
plt.title('Perdida vs. iteraciones')
plt.ylabel('Perdida')
plt.xlabel('Iteracion')

plt.subplot(1,2,1)
plt.plot(historia.history['acc'])
plt.title('Perdida vs. iteraciones')
plt.ylabel('Perdida')
plt.xlabel('Iteracion')

plt.show()

# Calcular la precision sobre el set de validacion

puntaje = modelo.evaluate(X_test, Y_test, verbose = 0)
print('Precision en el set de validacion: {:.1f}%'.format(100*puntaje[1]))

# Realizar prediccion sobre el set de validacion y mostrar algunos ejemplos
# de la clasificacion resultante

Y_pred = modelo.predict_classes(X_test)

ids_imgs = np.random.randint(0, X_test.shape[0],9)

for i in range(len(ids_imgs)):

	idx = ids_imgs[i]
	img = X_test[idx, :].reshape(28, 28)

	cat_original = np.argmax(Y_test[idx, :])
	cat_prediccion = Y_pred[idx]

	plt.subplot(3, 3, i+1)
	plt.imshow(img, cmap = 'gray')
	plt.axis('off')
	plt.title('"{}" clasificacion en el set de validacion')

plt.suptitle('Ejemplos de clasificacion en el set de validacion')
plt.show()