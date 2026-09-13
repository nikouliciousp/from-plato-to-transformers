# 🔗 Associationism Experiment
## Aristotle's 4 Laws of Memory → Machine Learning

### 🎯 The Idea

**350 BC:** Aristotle wrote *On Memory and Recollection*. He described four ways the mind links ideas.

**2024:** Those same four laws sit at the heart of modern neural networks.

### 📌 The Four Laws

#### 1️⃣ Law of Contiguity
**Aristotle:** "When two things occur close in time or space, the mind links them."

**ML:** Hebb's Rule — "Neurons that fire together, wire together"

**Formula:** `w_ij ∝ Correlation(neuron_i, neuron_j)`

**Experiment:** A slider shows two neurons activating. The stronger they sync, the stronger the connection weight.

---

#### 2️⃣ Law of Frequency
**Aristotle:** "The more frequently two things co-occur, the stronger the association."

**ML:** Gradient descent — each training iteration strengthens useful connections

**Formula:** `Δw = -α · ∂L/∂w`  (weight update proportional to error)

**Experiment:** Watch a curve show how loss decreases logarithmically with training iterations. The first repetitions matter most (law of diminishing returns).

---

#### 3️⃣ Law of Similarity
**Aristotle:** "The thought of one thing triggers the thought of a similar one."

**ML:** Embeddings + cosine similarity

**Formula:** `similarity(a, b) = (a · b) / (||a|| · ||b||)`

**Experiment:** A 2D vector space shows concepts clustering by meaning. Select "apple" and the nearest point is "pear." Select "dog" and the nearest is "cat."

---

#### 4️⃣ Law of Contrast
**Aristotle:** "Seeing one thing can trigger memory of its opposite."

**ML:** Contrastive learning (SimCLR, CLIP)

**Formula:** `Loss = -log(sim(x, x+) / Σ_neg sim(x, x_neg))`

**Experiment:** Watch two interleaved point clouds gradually separate as the network learns to pull similar points together and push dissimilar ones apart.

### 🏛 Philosophy → Math

Aristotle was describing **the fundamental operations of neural networks**:
- Contiguity = correlation = synaptic plasticity
- Frequency = repetition = weight updates
- Similarity = feature space = embeddings
- Contrast = differentiation = contrastive loss

**This is not metaphor. It is structural correspondence.**

### 📊 Interactive Sliders

For each law, drag sliders to control:
- **Contiguity:** Firing synchrony 0–100%
- **Frequency:** Training iterations 0–100
- **Similarity:** Concept selector (apple, pear, dog, cat, car)
- **Contrast:** Training progress 0–100%

Watch the visualizations update live.

### 🚀 How to Use

1. Open `index.html`
2. Click through the four tabs
3. Adjust the slider for each law
4. Watch the canvas visualization evolve
5. Read the insight box for the mathematical connection
6. Check the summary tab for a table of all four

### 📚 Sources

- Aristotle — *On Memory and Recollection* (Περὶ μνήμης καὶ ἀναμνήσεως) — 350 BC
- Hebb, D. O. (1949) — *The Organization of Behavior*
- Chen et al. (2020) — *A Simple Framework for Contrastive Learning of Visual Representations* (SimCLR)
- Radford et al. (2021) — *Learning Transferable Visual Models From Natural Language Supervision* (CLIP)

### 💡 The Insight

23 centuries separate Aristotle from Hebb. Yet the principles are identical.

This suggests: **We haven't invented neural networks. We've discovered them.** They reflect something fundamental about how information processing works.

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025