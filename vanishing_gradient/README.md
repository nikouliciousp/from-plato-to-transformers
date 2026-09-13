# 📉 Vanishing Gradient Experiment
### Why Sigmoid killed deep networks for 10 years — and how ReLU saved them

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-vanishing_gradient_experiment.html-00d4ff?style=for-the-badge)](#)
[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Series](https://img.shields.io/badge/Series-Post_3-f59e0b?style=for-the-badge)](#)

> *The arrow never arrives — it divides infinitely.* — Zeno of Elea

---

## 🎯 What It Shows

A training signal (gradient) starts at the last layer with 100% and travels backwards. At each layer it is multiplied by the activation derivative. The user drags the **depth** (1-30 layers) and sees how much signal reaches the first layer.

| Activation | Max Derivative | Vanishing? | Dead Neurons? |
|---|---|---|---|
| **Sigmoid** | 0.25 | ❌ Yes | ✅ No |
| **Tanh** | 1.0 | ⚠ At depth | ✅ No |
| **ReLU** | 1.0 | ✅ No | ❌ Yes |
| **GELU** | ~1.0 | ✅ No | ✅ No |

**The core:** `0.25¹⁰ ≈ 1 in a million` → the signal vanishes. `1¹⁰⁰ = 1` → ReLU preserves it.

## 🎛 Features

- Live depth slider with signal bars per activation
- Charts of the functions **and** their derivatives (where the problem hides)
- Timeline 1986→2016: Sigmoid → Hochreiter (1991) → ReLU → AlexNet (2012) → GELU
- Philosophical reading: Zeno → Sigmoid, Heraclitus → ReLU, Aristotle → GELU
- Tabs: Experiment · Curves · Mathematics · History · Philosophy
- Bilingual 🇬🇧 / 🇬🇷 · Responsive · Zero dependencies

## 🔬 Verified Mathematics

The formulas were checked programmatically: `σ'(0)=0.25`, `ReLU'(5)=1`, `ReLU'(−5)=0`, `0.25¹⁰ < 10⁻⁶`.

## 🚀 Usage

Open `vanishing_gradient_experiment.html` in any browser.

## 📄 License

MIT License — free to use with attribution.
