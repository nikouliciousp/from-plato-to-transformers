# 📉 Vanishing Gradient Experiment
### Why Sigmoid killed deep networks for 10 years — and how ReLU saved them

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-GitHub_Pages-00d4ff?style=for-the-badge)](https://nikouliciousp.github.io/vanishing_gradient_experiment/)
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

```
https://nikouliciousp.github.io/vanishing_gradient_experiment/
```
Or download `vanishing_gradient_experiment.html` and open it in any browser.

## 🔗 Series: From Plato to Transformers

Post 3 of the series.

## 📄 License

MIT License — free to use with attribution.

---
---

# 📉 Vanishing Gradient Experiment (Ελληνικά)
### Γιατί η Sigmoid σκότωνε τα βαθιά δίκτυα για 10 χρόνια — και πώς η ReLU τα έσωσε

> *Το βέλος δεν φτάνει ποτέ — διαιρείται επ' άπειρον.* — Ζήνων ο Ελεάτης

## 🎯 Τι Δείχνει

Ένα σήμα εκπαίδευσης (gradient) ξεκινά από το τελευταίο layer με 100% και ταξιδεύει προς τα πίσω. Σε κάθε layer πολλαπλασιάζεται με την παράγωγο της activation. Ο χρήστης κουνά το **βάθος** (1-30 layers) και βλέπει πόσο σήμα φτάνει στο πρώτο layer.

| Activation | Μέγιστη Παράγωγος | Vanishing; | Dead Neurons; |
|---|---|---|---|
| **Sigmoid** | 0.25 | ❌ Ναι | ✅ Όχι |
| **Tanh** | 1.0 | ⚠ Σε βάθος | ✅ Όχι |
| **ReLU** | 1.0 | ✅ Όχι | ❌ Ναι |
| **GELU** | ~1.0 | ✅ Όχι | ✅ Όχι |

**Ο πυρήνας:** `0.25¹⁰ ≈ 1 στο εκατομμύριο` → το σήμα εξαφανίζεται. `1¹⁰⁰ = 1` → η ReLU το διατηρεί.

## 🎛 Χαρακτηριστικά

- Live slider βάθους με signal bars ανά activation
- Γραφήματα των συναρτήσεων **και** των παραγώγων τους (εκεί κρύβεται το πρόβλημα)
- Χρονολόγιο 1986→2016: Sigmoid → Hochreiter (1991) → ReLU → AlexNet (2012) → GELU
- Φιλοσοφική ανάγνωση: Ζήνων → Sigmoid, Ηράκλειτος → ReLU, Αριστοτέλης → GELU
- Καρτέλες: Πείραμα · Καμπύλες · Μαθηματικά · Ιστορία · Φιλοσοφία
- Δίγλωσσο 🇬🇷 / 🇬🇧 · Responsive · Μηδενικές εξαρτήσεις

## 🔬 Επαληθευμένα Μαθηματικά

Οι τύποι ελέγχθηκαν προγραμματικά: `σ'(0)=0.25`, `ReLU'(5)=1`, `ReLU'(−5)=0`, `0.25¹⁰ < 10⁻⁶`.

## 🚀 Χρήση

```
https://nikouliciousp.github.io/vanishing_gradient_experiment/
```
Ή κατέβασε το `vanishing_gradient_experiment.html` και άνοιξέ το σε οποιονδήποτε browser.

## 🔗 Σειρά: From Plato to Transformers

Post 3 της σειράς.

## 📄 Άδεια

MIT License — ελεύθερη χρήση με αναφορά.

---

<div align="center">
Perikles Nikoules — MSc AI · University of Essex · 2025<br>
<i>All feedback is welcome — knowledge is built collectively.</i><br>
<i>Κάθε διόρθωση ή παρατήρηση είναι ευπρόσδεκτη — η γνώση χτίζεται συλλογικά.</i>
</div>
