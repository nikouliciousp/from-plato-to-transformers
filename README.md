# From Plato to Transformers 🏛️→🤖

A series of **5 interactive experiments** connecting ancient philosophy to modern AI. Each experiment is a live, playable visualization that shows how philosophical ideas became algorithms.

**Live:** [nikouliciousp.github.io/from-plato-to-transformers](https://nikouliciousp.github.io/from-plato-to-transformers)

---

## 📚 The Five Posts

| # | Title | Philosophical Connection | Live Experiment |
|---|-------|--------------------------|------------------|
| **1** | [Additive vs Divisive Neurons](#1-additive-vs-divisive-neurons) | Synthesis (Aristotle) vs Analysis (Plato) | `neurons_experiment.html` |
| **2** | [The ReLU Moment](#2-the-relu-moment) | Why nature made the bend (Aristotle) | `relu_experiment.html` |
| **3** | [5 Ways to Think](#3-5-ways-to-think) | Propositional, Predicate, Functional, Probabilistic, Inductive | `paradigms_experiment.html` |
| **4** | [Δεν Ξέρω (I Don't Know)](#4-δεν-ξέρω-i-dont-know) | Socratic humility vs hallucinations | `den_xero_experiment.html` |
| **5** | [The 4 Laws of Associationism](#5-the-4-laws-of-associationism) | Aristotle described ML in 350 BC | `associationism_experiment.html` |

---

## 1. Additive vs Divisive Neurons

**Φιλοσοφία:** Αριστοτέλης (σύνθεση — αθροίζει) vs Πλάτων (ανάλυση — διαιρεί)

Three types of neurons race to learn non-linear problems (XOR, spiral, circle, linear). Watch their **decision boundaries** form live as they train.

- **Additive:** z = Σw·x + b — Simple, fast, but can only draw straight lines
- **Divisive:** z = Σw⁺x / Σw⁻x — Naturally non-linear, normalises, but unstable
- **Hybrid:** 0.5·Additive + 0.5·Divisive — Balanced, like Leibniz's logos

**Δες το:** `neurons_experiment.html`

---

## 2. The ReLU Moment

**Φιλοσοφία:** Η κάμψη — "η φύση δεν κάνει άλματα" (Αριστοτέλης) → the golden mean (GELU)

Compare **6 activation functions** in real-time:
- Sigmoid (smooth, but vanishing gradient)
- Tanh (centered, but still vanishes)
- **ReLU** (sharp, lets gradient flow — revolution)
- Leaky ReLU (keeps signal when x<0)
- GELU (smooth ReLU — best of both)
- Swish (learnable, smooth, powerful)

**Δες το:** `relu_experiment.html`

---

## 3. Five Ways to Think

**Φιλοσοφία:** 5 Epistemic Paradigms

Given the same patient data, **5 completely different reasoning systems** make different diagnoses.

**Δες το:** `paradigms_experiment.html`

---

## 4. Δεν Ξέρω (I Don't Know)

**Φιλοσοφία:** Σωκράτης — "Ἓν οἶδα ὅτι οὐδὲν οἶδα"

**The deepest problem in AI:** It's not that models lie. It's that they **don't know they don't know.**

**Δες το:** `den_xero_experiment.html`

---

## 5. The 4 Laws of Associationism

**Φιλοσοφία:** Αριστοτέλης, 350 BC — The four laws of associative memory that became machine learning

**Δες το:** `associationism_experiment.html`

---

## 🛠️ Technical Stack

- **Frontend:** Plain HTML5, Canvas API, vanilla JavaScript (no frameworks)
- **Language:** Δίγλωσσο (Greek 🇬🇷 / English 🇬🇧)
- **Interactivity:** Real-time sliders, live canvas rendering
- **Math:** Implemented from first principles

---

## 👤 Author

**Perikles Nikoules**  
MSc AI, University of Essex, 2025

---

## 📜 License

MIT
