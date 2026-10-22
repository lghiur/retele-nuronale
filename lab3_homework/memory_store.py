import numpy as np

def make_params(nr_features, nr_classes):
    w = np.zeros((nr_features, nr_classes))
    b = np.zeros(nr_classes)
    lr = 0.07

    def get_params():
        return w, b, lr

    def set_params(new_w, new_b):
        nonlocal w, b
        w, b = new_w, new_b

    return get_params, set_params