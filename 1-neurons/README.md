# 🧠 Neurons Experiment
## Additive vs Divisive vs Hybrid Neurons — Live Training

### 🎯 What You'll Learn

Watch three different neuron types train in real-time on four datasets:

- **Additive Neuron** — Σ(w·x + b) — Aristotelian synthesis
- **Divisive Neuron** — Σ(w⁺·|x|) / Σ(w⁻·|x|) — Platonic division (diaeresis)
- **Hybrid Neuron** — 50% additive + 50% divisive — Leibnizian logos

### 📊 Datasets

- **XOR**: Non-linear problem — both classes interleaved
- **Circle**: Radial pattern — requires circular boundary
- **Spiral**: Complex intertwined structure — hardest challenge
- **Linear**: Linearly separable — easiest case

### 🏛 Philosophy

The **Divisive Neuron** corresponds to:
- **Plato's Diaeresis** — division of genus into species
- **Divisive Normalization** — the actual mechanism in the visual cortex (Carandini & Heeger, 2012)
- **Core of Attention** — softmax(QKᵀ/√d)·V in Transformers

The **Hybrid Neuron** represents Leibniz's insight: *reason encompasses both synthesis and analysis*.

### 🚀 How to Use

1. Open `index.html` in your browser
2. Choose a dataset
3. Press **AUTO** to watch training or **+20/+100** for manual steps
4. Watch the **Decision Boundaries** evolve in real-time
5. Compare **Loss** and **Accuracy** across all three

### 📐 Technical Details

**Additive:** Standard sigmoid neuron with MSE loss and backpropagation.

**Divisive:** 
```
num = Σ(w⁺ᵢ · |xᵢ|)
den = Σ(w⁻ᵢ · |xᵢ|) + ε
z = num / den
ŷ = σ(z)
```
Backprop is analytical (chain rule carefully applied to division).

**Hybrid:** Combines both with 50% weighting on each branch during backprop.

### 🔬 Research Background

- Divisive Normalization is empirically found in the visual system
- It provides natural non-linearity without saturation
- The attention mechanism in Transformers uses this principle

### 📚 Sources

- Carandini & Heeger (2012) — *Normalization as a canonical neural computation*
- Vaswani et al. (2017) — *Attention Is All You Need*

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025