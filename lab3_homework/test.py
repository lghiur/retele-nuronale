from helpers import load_dataset, load_parameters, normalize_x, normalize_y, prepare_trainset
from perceptron import perceptron
import numpy as np

def save_submission(predictions, path="submission.csv"):
  ids = np.arange(len(predictions))
  rows = np.column_stack((ids, predictions))
  np.savetxt(path, rows, fmt="%d", delimiter=",", header="ID,target", comments="")

def main():
  x, _ = load_dataset("trainset/test.npz")

  w, b = load_parameters("model.npz")
  normalized_x = normalize_x(x)

  z = perceptron(normalized_x, w, b)

  predictions = np.argmax(z, axis=1)

  print(f"Predictions: {predictions}") 
  save_submission(predictions)

if __name__ == "__main__":
    main()