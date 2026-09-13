# 🚫 Vanishing Gradient Experiment

**Το πρόβλημα που έσταψε το Deep Learning για 10 χρόνια (1991-2012)**

## 📌 Τι μαθαίνεις

Πώς το gradient **εξαφανίζεται** σε βαθιά δίκτυα:

- **Sigmoid:** 0.25^30 ≈ 0 (τίποτα δεν φτάνει στο πρώτο layer)
- **ReLU:** 1.0^30 = 1.0 (σήμα περνά αναλλοίωτο)

## 🎮 Πώς παίζεις

Κούνα το **depth slider** και δες πόσο σήμα φτάνει στο πρώτο layer

## 📈 Ιστορία

| Έτος | Ανακάλυψη |
|------|-----------|
| **1986** | Sigmoid + Backpropagation |
| **1991** | Hochreiter περιγράφει το vanishing gradient problem |
| **2011** | Glorot et al. — ReLU λύνει το πρόβλημα |
| **2012** | AlexNet κερδίζει ImageNet με ReLU — 6× ταχύτερα! |

## 🏛️ Φιλοσοφία

- **Ζήνων ο Ελεάτης** → Sigmoid: "Το βέλος δεν φτάνει ποτέ"
- **Ηράκλειτος** → ReLU: "Η ροή δεν σταματά"

---

## 🧬 Live Demo

**[Άνοιξε το πείραμα →](./vanishing_gradient_experiment.html)**

---

## 📚 References

- Hochreiter, S. (1991). "Untersuchungen zu dynamischen neuronalen Netzen"
- Glorot, X., Bordes, A., & Bengio, Y. (2011). Deep Sparse Rectifier Neural Networks
- Krizhevsky, A., Sutskever, I., & Hinton, G. (2012). ImageNet Classification with Deep Convolutional Neural Networks

**Δημιουργός:** Perikles Nikoules | 2025
