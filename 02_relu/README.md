# ⚡ ReLU Experiment
### Linear vs ReLU vs Sigmoid — Which activation function wins, and why

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-GitHub_Pages-00d4ff?style=for-the-badge)](https://nikouliciousp.github.io/relu_experiment/)
[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Series](https://img.shields.io/badge/Series-Post_2-f59e0b?style=for-the-badge)](#)

> *"Everything flows, nothing stands still."* — Heraclitus &nbsp;·&nbsp; *"Nature makes no leaps."* — Aristotle

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

```
https://nikouliciousp.github.io/relu_experiment/
```
Or download `relu_experiment.html` and open it in any browser.

## 🔗 Series: From Plato to Transformers

Post 2 of the series. → Post 1: [Neurons Experiment](https://github.com/nikouliciousp/neurons-experiment)

## 📄 License

MIT License — free to use with attribution.

---
---

# ⚡ ReLU Experiment (Ελληνικά)
### Linear vs ReLU vs Sigmoid — Ποια activation function κερδίζει και γιατί

> *"Τα πάντα ρει, ουδέν μένει."* — Ηράκλειτος &nbsp;·&nbsp; *"Η φύση δεν κάνει άλματα."* — Αριστοτέλης

## 🎯 Τι Δείχνει

Ένα **ablation study**: τρία δίκτυα με **ίδια αρχιτεκτονική** (1 hidden layer, 6 νευρώνες, Sigmoid output) — αλλάζει **μόνο** η activation function του hidden layer.

| Δίκτυο | Hidden Activation | Φιλόσοφος |
|---|---|---|
| **Linear** | Καμία | Παρμενίδης — στατικό |
| **ReLU** | `max(0,x)` | Ηράκλειτος — απότομη αλλαγή |
| **Sigmoid** | `σ(x)` | Αριστοτέλης — ομαλότητα |

Η φυσική κατάληξη: **GELU** (Leibniz — αρμονία) — ό,τι χρησιμοποιούν σήμερα GPT, BERT, Claude.

## 🔬 Το Επιστημονικό Υπόβαθρο

Δείχνει γιατί η Sigmoid στα hidden layers υποφέρει από **vanishing gradient** (μέγιστη παράγωγος 0.25), ενώ η ReLU (παράγωγος 1 για θετικά) το λύνει — αλλά φέρνει το πρόβλημα των **dead neurons**.

Αναφορές: Minsky & Papert (1969), Nair & Hinton (2010), Hendrycks & Gimpel (2016, GELU).

## 🎛 Χαρακτηριστικά

- Ablation study — δίκαιη σύγκριση, μόνο το hidden activation αλλάζει
- Σωστό analytical backpropagation και στα τρία δίκτυα
- 4 datasets, live decision boundaries, loss curve, accuracy
- Καρτέλες: Πείραμα · Μαθηματικά · Φιλοσοφία
- Δίγλωσσο 🇬🇷 / 🇬🇧 · Responsive · Μηδενικές εξαρτήσεις

## 🚀 Χρήση

```
https://nikouliciousp.github.io/relu_experiment/
```
Ή κατέβασε το `relu_experiment.html` και άνοιξέ το σε οποιονδήποτε browser.

## 🔗 Σειρά: From Plato to Transformers

Post 2 της σειράς. → Post 1: [Neurons Experiment](https://github.com/nikouliciousp/neurons-experiment)

## 📄 Άδεια

MIT License — ελεύθερη χρήση με αναφορά.

---

<div align="center">
Perikles Nikoules — MSc AI · University of Essex · 2025<br>
<i>All feedback is welcome — knowledge is built collectively.</i><br>
<i>Κάθε διόρθωση ή παρατήρηση είναι ευπρόσδεκτη — η γνώση χτίζεται συλλογικά.</i>
</div>
