"""
train_mnist.py — Trains a simple CNN on MNIST and saves it as mnist_cnn.keras.

Run this once before using digit_tester.py:
    python train_mnist.py

It will download MNIST (first time only, ~11 MB), train a small CNN for 5 epochs,
and save the model next to this script. On a modern CPU it takes a few minutes.
Test accuracy is typically ~99%.

Requires:
    pip install tensorflow numpy

Perikles Nikoules — MSc AI, University of Essex, 2025
Part of the 'From Plato to Transformers' series.
"""

import os
import numpy as np
import keras
from keras import layers

# Save next to this script, not in the current working directory.
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mnist_cnn.keras")

# ---- 1. Load MNIST ----
print("Loading MNIST...")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(f"  train: {x_train.shape}, test: {x_test.shape}")

# Normalise to [0, 1] and add channel dimension
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# ---- 2. Build a small CNN ----
# Architecture: 2 conv-pool blocks → flatten → dense → softmax
# This mirrors the hierarchy shown in cnn_experiment.html:
# Layer 1 finds edges (32 filters), Layer 2 finds shapes (64 filters),
# the dense layer combines them into the Idea (10 classes).
model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu", name="conv1_edges"),
    layers.MaxPooling2D((2, 2), name="pool1"),
    layers.Conv2D(64, (3, 3), activation="relu", name="conv2_shapes"),
    layers.MaxPooling2D((2, 2), name="pool2"),
    layers.Flatten(name="flatten"),
    layers.Dense(64, activation="relu", name="hidden"),
    layers.Dropout(0.3, name="dropout"),
    layers.Dense(10, activation="softmax", name="output"),
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

print("\nModel architecture:")
model.summary()

# ---- 3. Train ----
print("\nTraining...")
model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=128,
    validation_split=0.1,
    verbose=1,
)

# ---- 4. Evaluate on test set ----
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc * 100:.2f}%")
print(f"Test loss:     {test_loss:.4f}")

# ---- 5. Save ----
model.save(MODEL_PATH)
print(f"\nModel saved to: {MODEL_PATH}")
print("You can now run: python digit_tester.py")
