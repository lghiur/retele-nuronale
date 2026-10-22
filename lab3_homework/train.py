from perceptron import perceptron
from memory_store import make_params
from helpers import load_dataset, split_dataset, prepare_trainset, normalize_x, normalize_y, cross_entropy, update_params, softmax
import numpy as np
import matplotlib.pyplot as plt
import time

def train(x, y, read_params, save_params, epochs=200, batch_size=64):
  history = []
  times = []
  start_time = time.perf_counter()

  for epoch in range(epochs):
    for start in range(0, len(x), batch_size):
      batch_x = x[start:start+batch_size]
      batch_y = y[start:start+batch_size]

      w, b, lr = read_params()
      z = perceptron(batch_x, w, b)
      t = softmax(z)
      e = batch_y - t
      new_w, new_b = update_params(w, b, lr, e, batch_x)
      save_params(new_w, new_b)

    w, b, lr = read_params()
    z = perceptron(x, w, b)
    t = softmax(z)
    epoch_loss = cross_entropy(y, t)
    history.append(epoch_loss)
    times.append(time.perf_counter() - start_time)
    print(f"epoch {epoch + 1}: loss = {epoch_loss:.5f}, time = {times[-1]:.1f}s")
  return history, times

def plot_loss_vs_time(loss_history, times):
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
  
  epochs = range(1, len(loss_history) + 1)

  ax1.plot(epochs, loss_history, marker="o")
  ax1.set_xlabel("epoch")
  ax1.set_ylabel("Cross-entropy on training data")
  ax1.set_title("Error per epoch")
  ax1.grid(alpha=0.3)

  ax2.plot(epochs, times, marker="o")
  ax2.set_xlabel("epoch")
  ax2.set_ylabel("time since start (seconds)")
  ax2.set_title("Training time")
  ax2.grid(alpha=0.3)

  fig.tight_layout()
  fig.savefig("training_curve.png", dpi=150)

def main():
  x, y = load_dataset("trainset/train.npz")
  x_train, y_train, _, _ = split_dataset(x, y)
  nr_features, nr_classes = prepare_trainset(x_train)
  get_params, set_params = make_params(nr_features, nr_classes)
  normalized_x = normalize_x(x_train)
  normalized_y = normalize_y(y_train, nr_classes)
  history, times = train(normalized_x, normalized_y, get_params, set_params)
  w, b, _ = get_params()
  np.savez("model.npz", w=w, b=b)
  plot_loss_vs_time(history, times)

if __name__ == "__main__":
    main()
