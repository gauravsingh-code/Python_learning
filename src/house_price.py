import tensorflow as tf
import numpy as np

# Normalize data
x = np.array([0.5,1,1.5,2,2.5,3,3.5,4], dtype=float)
y = np.array([50,100,150,200,250,300,350,400], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(
    optimizer='adam',   # safer than SGD
    loss='mean_squared_error'
)

model.fit(x, y, epochs=2000, verbose=1)

# Predict for 3000 sq ft → 3.0 after scaling
prediction = model.predict(np.array([[3.0]]))

print("Predicted price:", prediction[0][0])
