# # Import libraries
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense
# import tensorflow.compat.v2 as tf
# from keras import models

# # Define input data and output labels
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])

# # Define the neural network architecture
# model = Sequential()
# model.add(Dense(units=4, input_dim=2, activation='relu'))
# model.add(Dense(units=1, activation='sigmoid'))

# # Compile the model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Train the model
# model.fit(X, y, epochs=1000, verbose=0)

# # Evaluate the model on new data
# test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# predictions = model.predict(test_data)
# print(predictions)
# ---------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# Create a random dataset
X = np.random.rand(100, 1)
y = np.sin(2 * np.pi * X) + np.random.normal(0, 0.1, (100, 1))

# Define the neural network model
model = Sequential()
model.add(Dense(10, input_shape=(1,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mse', optimizer='adam')

# Train the model
history = model.fit(X, y, epochs=50, batch_size=10, verbose=0)

# Visualize the model's performance
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

