import numpy as np

def load_dataset(path):
  data = np.load(path)
  x = data["data"]
  y = data["labels"] if "labels" in data.files else None
  return x, y


def split_dataset(x, y, val_fraction=0.1):
  split = int(len(x) * (1 - val_fraction))
  x_train, x_val = x[:split], x[split:]
  y_train, y_val = y[:split], y[split:]
  return x_train, y_train, x_val, y_val

def load_parameters(path):
  params = np.load(path)
  w = params["w"]
  b = params["b"]

  return w, b

def prepare_trainset(x_train, y_train):
  n_features = len(x_train[0])
  n_classes = int(y_train.max()) + 1

  return n_features, n_classes

def normalize_x(x):
  x_float = x.astype(np.float32)
  return x_float / 255

def normalize_y(y, nr_classes):
  ln = len(y)
  norm_y = np.zeros((ln, nr_classes))
  rows = np.arange(ln)
  norm_y[rows, y] = 1

  return norm_y

def mse(y, z):
  return np.mean((y - z) ** 2)

def cross_entropy(y, z):
  return -np.mean(np.sum(y * np.log(z + 1e-12), axis=1))

def update_params(current_w, current_b, lr, err, x):
  updated_w = current_w + lr * x.transpose() @ err / len(x)
  updated_b = current_b + lr * err.sum(axis=0) / len(x)
  return updated_w, updated_b

def softmax(z):
  row_max = np.max(z, axis=1, keepdims=1)
  new_z = np.exp(z - row_max) / np.sum(np.exp(z - row_max), axis = 1, keepdims=True)

  return new_z
