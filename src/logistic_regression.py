import numpy as np

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])

w = 0.0
b = 0.0
lr = 0.1
epochs = 1000

def sigmoid(z):
    return 1/(1 + np.exp(-z))

n = len(x)

for _ in range(epochs):
    z = w*x + b
    p = sigmoid(z)

    dw = (1/n)*np.sum((p-y)*x)
    db = (1/n)*np.sum(p-y)

    w -= lr*dw
    b -= lr*db

print("Weight:", w)
print("Bias:", b)


def predict(x):
    z = w * x + b
    p = sigmoid(z)
    return 1 if p >= 0.5 else 0

print(predict(3.5))
