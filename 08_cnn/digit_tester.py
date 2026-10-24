"""
digit_tester.py — Hand-drawn digit tester for the MNIST CNN.

Opens a tkinter window with a 280x280 black canvas. You draw a digit with
the mouse, press Predict, and the trained CNN tells you which digit it sees.

Requires:
    - A trained Keras model saved as 'mnist_cnn.keras' in the same folder.
    - Python packages: tensorflow (or keras), numpy, pillow.
      Install:  pip install tensorflow numpy pillow
    - tkinter (ships with most Python installs; on some Linux distros
      install python3-tk separately).

Why preprocessing matters: a naive resize to 28x28 produces digits that
look nothing like what MNIST contains. The network was trained on digits
that are scaled to fit in a 20x20 box and then centred by their centre
of mass in a 28x28 image. The preprocess() function below reproduces
exactly that transformation.

Perikles Nikoules — MSc AI, University of Essex, 2025
Part of the 'From Plato to Transformers' series.
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw
import keras

# Resolve model path relative to THIS script, not the current working directory.
# This way the tester works no matter where you launch it from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "mnist_cnn.keras")
CANVAS_SIZE = 280
BRUSH = 10


def preprocess(img):
    """Turn a 280x280 grayscale drawing into the (1, 28, 28, 1) tensor
    the MNIST CNN expects. Mimics the MNIST preprocessing pipeline:
    crop to bounding box, scale so the longest side is 20 px, then centre
    by centre of mass inside a 28x28 canvas, finally normalise to [0, 1].
    """
    bbox = img.getbbox()
    if bbox is None:
        return None
    digit = img.crop(bbox)
    w, h = digit.size
    scale = 20.0 / max(w, h)
    new_w, new_h = max(1, round(w * scale)), max(1, round(h * scale))
    digit = digit.resize((new_w, new_h), Image.LANCZOS)

    d = np.array(digit, dtype="float32")
    ys, xs = np.indices(d.shape)
    cy = (ys * d).sum() / d.sum()
    cx = (xs * d).sum() / d.sum()

    left = min(max(int(round(14 - cx)), 0), 28 - new_w)
    top = min(max(int(round(14 - cy)), 0), 28 - new_h)
    canvas = Image.new("L", (28, 28), 0)
    canvas.paste(digit, (left, top))

    arr = np.array(canvas, dtype="float32") / 255.0
    return arr.reshape(1, 28, 28, 1)


class DigitApp:
    def __init__(self, root, model):
        self.model = model
        root.title("MNIST digit tester")

        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE,
                                bg="black", cursor="cross")
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Hidden image: strokes are drawn here too, and this is what the model reads.
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
        self.draw = ImageDraw.Draw(self.image)
        self.last = None

        self.canvas.bind("<Button-1>", self.start)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop)

        tk.Button(root, text="Predict", command=self.predict).grid(row=1, column=0, sticky="ew")
        tk.Button(root, text="Clear", command=self.clear).grid(row=1, column=1, sticky="ew")
        self.label = tk.Label(root, text="Draw a digit, then press Predict",
                              font=("Arial", 14), justify="left")
        self.label.grid(row=2, column=0, columnspan=2)

    def start(self, event):
        self.last = (event.x, event.y)

    def stop(self, event):
        self.last = None

    def paint(self, event):
        if self.last is None:
            self.last = (event.x, event.y)
        x0, y0 = self.last
        self.canvas.create_line(x0, y0, event.x, event.y, fill="white",
                                width=BRUSH * 2, capstyle="round")
        self.draw.line([x0, y0, event.x, event.y], fill=255, width=BRUSH * 2)
        self.draw.ellipse([event.x - BRUSH, event.y - BRUSH,
                           event.x + BRUSH, event.y + BRUSH], fill=255)
        self.last = (event.x, event.y)

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, CANVAS_SIZE, CANVAS_SIZE], fill=0)
        self.label.config(text="Draw a digit, then press Predict")

    def predict(self):
        x = preprocess(self.image)
        if x is None:
            self.label.config(text="The canvas is empty")
            return
        probs = self.model.predict(x, verbose=0)[0]
        top3 = np.argsort(probs)[::-1][:3]
        lines = [f"Prediction: {top3[0]}  ({probs[top3[0]] * 100:.1f}%)"]
        lines += [f"   {d}: {probs[d] * 100:.1f}%" for d in top3[1:]]
        self.label.config(text="\n".join(lines))


if __name__ == "__main__":
    if not os.path.isfile(MODEL_PATH):
        print(f"ERROR: Model file not found at:\n  {MODEL_PATH}\n")
        print("Train the model first by running:")
        print("  python train_mnist.py")
        print("\nMake sure train_mnist.py is in the same folder as digit_tester.py.")
        sys.exit(1)

    print(f"Loading model from: {MODEL_PATH}")
    model = keras.models.load_model(MODEL_PATH)
    print("Model loaded. Opening window...")

    root = tk.Tk()
    DigitApp(root, model)
    root.mainloop()
