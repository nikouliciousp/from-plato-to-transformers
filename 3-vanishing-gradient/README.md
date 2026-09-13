# 📉 Vanishing Gradient Experiment
## Why Deep Networks Failed (Before ReLU)

### 🎯 The Problem

When you multiply small numbers many times, you get exponentially smaller numbers:

**0.25¹⁰ ≈ 0.0000095** — essentially zero

This is why Sigmoid (max derivative: 0.25) killed deep networks.

### 📊 Visualization

A **depth slider** shows you:

1. **Gradient at each layer** — how much the weights actually update
2. **Signal attenuation** — what fraction of the original gradient survives
3. **The math**: `g_L = g_0 · (dσ/dx)^L`

Watch it approach zero as depth increases.

### 🏛 Philosophy

- **Zeno's Paradox** — "To go anywhere, you must travel half the distance. Then half again..." — asymptotic approach to zero
- **Heraclitus** — "Everything flows" — but gradient flow eventually stops
- **Aristotle** — "The golden mean" — GELU finds the balance

### 🚀 How to Use

1. Open `index.html`
2. Drag the **Depth slider** from 1 to 20 layers
3. Watch the gradient bar shrink exponentially
4. See the formula update in real-time
5. Compare Sigmoid vs ReLU vs GELU

### 📐 The Math

**Sigmoid chain rule:**
```
g_L = g_0 · (dσ/dx)¹ · (dσ/dx)² · ... · (dσ/dx)^L
g_L = g_0 · (0.25)^L  (worst case)
```

Depth 10: `g_10 = g_0 · (0.25)^10 ≈ g_0 · 10^-6`

**ReLU chain rule:**
```
g_L = g_0 · (1.0)^L = g_0
```
Gradient preserved perfectly (no saturation).

**GELU chain rule:**
```
g_L ≈ g_0 · (0.5 to 0.9)^L  — smoothly interpolated
```

### 🔬 Historical Context

**Before 2010:** Neural networks believed limited to 3–4 layers max.

**2010:** Nair & Hinton propose ReLU → GPUs + ReLU → ResNet (2015, 152 layers) → Modern transformers (96+ layers).

### 💡 Why ReLU Wins

ReLU has derivative = 1 for any positive x:
- No saturation
- Gradient flows unattenuated
- But: Dead neurons (if x stays negative)

GELU smooths this out:
- Smooth derivative everywhere
- Still allows strong gradients
- Fewer dead neurons

### 📚 Sources

- Hochreiter (1991) — *Untersuchungen zur Dynamik neuronaler Netze* (first warning)
- Glorot & Bengio (2010) — Understanding the difficulty of training deep networks
- Nair & Hinton (2010) — Rectified Linear Units
- He et al. (2015) — Deep Residual Learning

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025