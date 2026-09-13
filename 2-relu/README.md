# ⚡ ReLU Experiment
## Linear vs ReLU vs Sigmoid Activations — Ablation Study

### 🎯 What You'll Learn

The same neural network architecture trained with three different hidden activation functions:

- **Sigmoid** — The old standard (1997–2010)
- **ReLU** — The breakthrough (2010–present)
- **GELU** — The modern choice (2016–present in LLMs)

### 🔄 The Ablation

Everything identical except the activation function:
- Architecture: 2 input → 64 hidden → 1 output
- Loss: MSE
- Learning rate: 0.01
- Optimizer: SGD
- Data: same 4 datasets as Neurons experiment

Only the hidden layer activation changes.

### 📉 Why This Matters

**Sigmoid (1997)**
- Output: (0, 1) — interpretable as probability
- Problem: **Vanishing gradient** — derivative peaks at 0.25
- Effect: Deep networks don't train beyond ~3 layers

**ReLU (2010)**
- Output: max(0, x) — piecewise linear
- Advantage: Derivative is 1 for x>0 — gradient flows
- Effect: Networks can go deep (ResNet: 152 layers)

**GELU (2016)**
- Output: x·Φ(x) — smooth approximation to ReLU
- Advantage: Smooth, differentiable everywhere
- Effect: Better performance than ReLU in transformers

### 🏛 Philosophy

- **Sigmoid** — Aristotle's principle: "nature makes no leaps" (continuity)
- **ReLU** — Parmenides: "Being or Nothing" (binary: on/off)
- **GELU** — Heraclitus: "Everything flows" (smooth transition)

### 🚀 How to Use

1. Open `index.html`
2. Select a dataset
3. Press **AUTO TRAIN** to run all three simultaneously
4. Watch the training curves diverge
5. See how Sigmoid stalls around epoch 20

### 📊 What to Expect

- **Sigmoid**: Reaches ~60–70% accuracy, then plateaus
- **ReLU**: Reaches 85–95% quickly, continues improving
- **GELU**: Reaches 90–98%, smoothest curve

On **Spiral** dataset, ReLU and GELU may reach 100%, Sigmoid will cap at ~65%.

### 📐 Technical Formulas

```
Sigmoid(x) = 1 / (1 + e^(-x))
dSigmoid/dx = σ(x) · (1 - σ(x))  — max 0.25 at x=0

ReLU(x) = max(0, x)
dReLU/dx = { 1 if x>0, 0 if x<0 }

GELU(x) = x · Φ(x)  where Φ is the standard normal CDF
dGELU/dx = Φ(x) + x·φ(x)  — smooth, always defined
```

### 🔬 Research Background

- Nair & Hinton (2010) — *Rectified Linear Units*
- Hendrycks & Gimpel (2016) — *GELU*
- Glorot et al. (2011) — Xavier initialization (fixes Sigmoid)
- LeCun et al. (1991) — Early warning of vanishing gradient

### 📚 Sources

- Nair, V., & Hinton, G. E. (2010). Rectified linear units improve restricted Boltzmann machines.
- Hendrycks, D., & Gimpel, K. (2016). Gaussian Error Linear Units (GELUs).

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025