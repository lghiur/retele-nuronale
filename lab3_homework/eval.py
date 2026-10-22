from helpers import load_dataset, split_dataset, load_parameters, normalize_x
from perceptron import perceptron
import numpy as np

def main():
  x, y = load_dataset("trainset/train.npz")
  _, _, x_val, y_val = split_dataset(x, y)

  w, b = load_parameters("model.npz")
  normalized_x = normalize_x(x_val)
  z = perceptron(normalized_x, w, b)

  predictions = np.argmax(z, axis=1)
  acc = np.mean(predictions == y_val)

  print(f"Accuracy: {acc * 100:.2f}%") 

if __name__ == "__main__":
    main()