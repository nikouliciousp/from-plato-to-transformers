# ⚡ ReLU Experiment
### Linear vs ReLU vs Sigmoid — Which activation function wins, and why

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-relu_experiment.html-00d4ff?style=for-the-badge)](#)
[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Series](https://img.shields.io/badge/Series-Post_2-f59e0b?style=for-the-badge)](#)

> *"Everything flows, nothing stands still."* — Heraclitus · *"Nature makes no leaps."* — Aristotle

---

## 🎯 What It Shows

An **ablation study**: three networks with the **same architecture** (1 hidden layer, 6 neurons, Sigmoid output) — only the hidden layer activation changes.

| Network | Hidden Activation | Philosopher |
|---|---|---|
| **Linear** | None | Parmenides — static |
| **ReLU** | `max(0,x)` | Heraclitus — abrupt change |
| **Sigmoid** | `σ(x)` | Aristotle — smoothness |

The natural conclusion: **GELU** (Leibniz — harmony) — what GPT, BERT and Claude use today.

## 🔬 Scientific Background

Shows why Sigmoid in hidden layers suffers from **vanishing gradient** (max derivative 0.25), while ReLU (derivative 1 for positives) solves it — but introduces the **dead neurons** problem.

References: Minsky & Papert (1969), Nair & Hinton (2010), Hendrycks & Gimpel (2016, GELU).

## 🎛 Features

- Ablation study — fair comparison, only the hidden activation changes
- Correct analytical backpropagation in all three networks
- 4 datasets, live decision boundaries, loss curve, accuracy
- Tabs: Experiment · Mathematics · Philosophy
- Bilingual 🇬🇧 / 🇬🇷 · Responsive · Zero dependencies

## 🚀 Usage

Open `relu_experiment.html` in any browser.

## 📄 License

MIT License — free to use with attribution.
