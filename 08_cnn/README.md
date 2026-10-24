# 08 · CNN — From the Cave to the Idea

Eighth experiment of **From Plato to Transformers**.

A Convolutional Neural Network is presented as the Platonic ascent from the cave: pixels → edges → textures → parts → object. The interactive HTML walks through the hierarchy; the Python app lets you test a trained MNIST model on your own hand-drawn digit.

## Files

| File | Purpose |
|------|---------|
| `cnn_experiment.html` | Interactive tool, bilingual EL/EN. Open in any browser. |
| `train_mnist.py` | Trains a small CNN on MNIST (5 epochs, ~99% test accuracy) and saves `mnist_cnn.keras`. |
| `digit_tester.py` | Tkinter window that loads `mnist_cnn.keras`, lets you draw a digit, and shows the prediction. |
| `mnist_cnn.keras` | Produced by `train_mnist.py`. Not committed, generate it locally. |

## Running the HTML experiment

Open `cnn_experiment.html` in any modern browser. No install, no dependencies, works on desktop and mobile.

Or online, through raw.githack after you push to GitHub:
`https://raw.githack.com/<user>/from-plato-to-transformers/main/08_cnn/cnn_experiment.html`

## Running the Python digit tester

**Step 1 — install dependencies.**
```
pip install tensorflow numpy pillow
```
On some Linux distributions you also need `python3-tk`:
```
sudo apt install python3-tk
```

**Step 2 — train the model** (only once; produces `mnist_cnn.keras` in this folder).
```
python train_mnist.py
```

**Step 3 — run the tester.**
```
python digit_tester.py
```

Both scripts resolve their paths relative to their own location, so they work regardless of which folder you run them from.

### Why the preprocessing matters

A naive resize of a 280×280 drawing to 28×28 produces digits that look nothing like the MNIST training data. The `preprocess()` function reproduces MNIST's pipeline:

1. Crop to the bounding box of the drawing.
2. Scale so the longest side becomes 20 pixels.
3. Centre the digit by its centre of mass inside a 28×28 canvas.
4. Normalise to the [0, 1] range.

Without this, predictions degrade sharply even for a model that is accurate on the MNIST test set.

## The philosophical thread

Plato describes in *Republic* VII an ascent from shadows on the cave wall, to reflections, to the things themselves, to the sun. A CNN follows the same path: raw pixels → edges → textures → parts → whole object. The engineers did not predict Plato, they rediscovered the structure of hierarchical abstraction that Plato was pointing at.

The experiment makes the mapping concrete, step by step, with the original Greek passage from the Republic shown at each rung of the ascent.

## Honest notes

- The HTML experiment visualises a four-rung hierarchy for clarity. A production CNN (ResNet, EfficientNet) has dozens of layers and millions of parameters, but obeys the same three principles.
- Convolution itself predates deep learning by two centuries (d'Alembert, Euler, Laplace). What is new in CNNs is that the kernel weights are learned, not hand-designed.
- The `digit_tester.py` script has not been tested on this machine (no tkinter, no GPU, MNIST download blocked). It is provided as working source; verify locally and report issues.

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025
*Part of the From Plato to Transformers series.*
