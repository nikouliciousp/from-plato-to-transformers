# 🏛 CNN Experiment
### From the Cave to the Idea — Convolutional Neural Networks

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Raw.githack-00d4ff?style=for-the-badge)](https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/08_cnn/cnn_experiment.html)
[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Series](https://img.shields.io/badge/Series-Post_8-f59e0b?style=for-the-badge)](#)

> *"Ἡ παιδεία περιαγωγή ψυχῆς ἐστιν."* — Education is a turning of the soul. Plato, *Republic* VII

---

## 🎯 What It Shows

A Convolutional Neural Network presented as the Platonic ascent from the cave: **pixels → edges → shapes → the Idea**.

The experiment follows one single digit, the **"7"**, from the input to the output of a CNN. Each rung of the ascent shows how the same digit is transformed, paired with the original Greek passage from *Republic* VII:

1. **The shadows, only pixels** — the CNN sees only 28×28 = 784 brightness values. No meaning, only light.
2. **The filter scans** — a 3×3 kernel slides across the image and writes one value per position into a feature map.
3. **First rung, three edges** — several filters, each finding a different edge: vertical, horizontal, diagonal.
4. **Second rung, corners and shapes** — the second layer combines the edges of the first into corners and parts.
5. **Third rung, the Idea** — a fully connected layer produces 10 scores; softmax turns them into probabilities and "7" wins.
6. **The three principles of a CNN** — local connectivity, parameter sharing, hierarchical features.
7. **The return to the cave** — once trained, the CNN goes back to raw pixels and says what it sees.

## 🧠 The Three Principles

| Principle | What it means |
|---|---|
| **Local connectivity** | Each neuron sees only a small neighbourhood of the image, not the whole of it. |
| **Parameter sharing** | The same filter is applied at every position, so a "7" is recognised wherever it appears. |
| **Hierarchical features** | Simple patterns combine into complex ones, layer after layer. |

$$(I * K)[i,j] = \sum_{u,v} I[i+u,\,j+v] \cdot K[u,v]$$

> **Honest note:** The experiment visualises a short hierarchy for clarity. A production CNN (ResNet, EfficientNet) has dozens of layers and millions of parameters, but obeys the same three principles. Convolution itself predates deep learning by two centuries (d'Alembert, Euler, Laplace). What is new in CNNs is that the kernel weights are **learned**, not hand-designed.

## 🎛 Features

- 7-rung animated walkthrough of a single digit through a CNN
- Live kernel scan producing a feature map
- Original Greek passages from *Republic* VII at every rung
- Equations rendered with MathJax
- Play, pause, next, previous, restart, and step navigation controls
- Bilingual 🇬🇧 / 🇬🇷 · Responsive
- **Bonus:** a Python app to test a trained MNIST CNN on your own hand-drawn digit

## 🐍 Python Digit Tester

| File | Purpose |
|------|---------|
| `train_mnist.py` | Trains a small CNN on MNIST (5 epochs, ~99% test accuracy) and saves `mnist_cnn.keras`. |
| `digit_tester.py` | Tkinter window that loads `mnist_cnn.keras`, lets you draw a digit, and shows the prediction. |
| `mnist_cnn.keras` | Produced by `train_mnist.py`. Not committed, generate it locally. |

```
pip install tensorflow numpy pillow     # on some Linux distros also: sudo apt install python3-tk
python train_mnist.py                   # once, produces mnist_cnn.keras
python digit_tester.py                  # draw a digit and press Predict
```

Both scripts resolve their paths relative to their own location, so they work from any folder.

**Why the preprocessing matters.** A naive resize of a 280×280 drawing to 28×28 produces digits that look nothing like MNIST. `preprocess()` reproduces MNIST's pipeline: crop to the bounding box → scale the longest side to 20 px → centre by centre of mass in a 28×28 canvas → normalise to `[0, 1]`. Without it, predictions degrade sharply even for a model that is accurate on the MNIST test set.

## 🚀 Usage

```
https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/08_cnn/cnn_experiment.html
```

Or download `cnn_experiment.html` and open it in any modern browser.

## 🔬 Scientific Background

Sources: Plato, *Republic* VII (the Allegory of the Cave) · LeCun, Bottou, Bengio & Haffner (1998) *Gradient-Based Learning Applied to Document Recognition* · MNIST dataset.

## 🔗 Series: From Plato to Transformers

Post 8 of the series. After width and depth (Post 7), it shows how a network built for images climbs from raw sensation to abstraction. The engineers did not predict Plato; they rediscovered the structure of hierarchical abstraction he was pointing at.

## 📄 License

MIT License — free to use with attribution.

---
---

# 🏛 CNN Experiment (Ελληνικά)
### Από το Σπήλαιο στην Ιδέα — Convolutional Neural Networks

> *«Ἡ παιδεία περιαγωγή ψυχῆς ἐστιν.»* — Πλάτων, Πολιτεία Ζ΄

## 🎯 Τι Δείχνει

Ένα Convolutional Neural Network παρουσιασμένο ως η πλατωνική άνοδος από το σπήλαιο: **pixels → ακμές → σχήματα → η Ιδέα**.

Το πείραμα ακολουθεί ένα και μόνο ψηφίο, το **«7»**, από την είσοδο ως την έξοδο ενός CNN. Κάθε σκαλί της ανόδου δείχνει πώς μετασχηματίζεται το ίδιο ψηφίο, μαζί με το πρωτότυπο απόσπασμα από την *Πολιτεία* Ζ΄:

1. **Οι σκιές, μόνο pixels** — το CNN βλέπει μόνο 28×28 = 784 τιμές φωτεινότητας. Καμία σημασία, μόνο ένταση φωτός.
2. **Το φίλτρο σαρώνει** — ένα 3×3 kernel γλιστράει πάνω στην εικόνα και γράφει μία τιμή ανά θέση σε ένα feature map.
3. **Πρώτο σκαλί, τρεις ακμές** — πολλά φίλτρα, καθένα βρίσκει διαφορετική ακμή: κάθετη, οριζόντια, διαγώνια.
4. **Δεύτερο σκαλί, γωνίες και σχήματα** — το δεύτερο layer συνδυάζει τις ακμές του πρώτου σε γωνίες και μέρη.
5. **Τρίτο σκαλί, η Ιδέα** — ένα fully connected layer παράγει 10 scores· το softmax τα κάνει πιθανότητες και το «7» κερδίζει.
6. **Οι τρεις αρχές του CNN** — local connectivity, parameter sharing, hierarchical features.
7. **Η επιστροφή στο σπήλαιο** — μόλις μάθει, το CNN γυρίζει στα pixels και λέει τι βλέπει.

## 🧠 Οι Τρεις Αρχές

| Αρχή | Τι σημαίνει |
|---|---|
| **Local connectivity** | Κάθε νευρώνας βλέπει μόνο μια μικρή γειτονιά της εικόνας, όχι ολόκληρη. |
| **Parameter sharing** | Το ίδιο φίλτρο εφαρμόζεται σε κάθε θέση, άρα ένα «7» αναγνωρίζεται όπου κι αν εμφανιστεί. |
| **Hierarchical features** | Απλά μοτίβα συνδυάζονται σε σύνθετα, layer μετά από layer. |

> **Σημείωση ειλικρίνειας:** Το πείραμα δείχνει μια σύντομη ιεραρχία για λόγους σαφήνειας. Ένα CNN παραγωγής (ResNet, EfficientNet) έχει δεκάδες layers και εκατομμύρια παραμέτρους, αλλά υπακούει στις ίδιες τρεις αρχές. Η συνέλιξη προϋπάρχει του deep learning κατά δύο αιώνες (d'Alembert, Euler, Laplace). Το καινούργιο στα CNN είναι ότι τα βάρη των kernels **μαθαίνονται**, δεν σχεδιάζονται με το χέρι.

## 🎛 Χαρακτηριστικά

- 7 σκαλιά animated διαδρομής ενός ψηφίου μέσα σε ένα CNN
- Live σάρωση kernel που παράγει feature map
- Πρωτότυπα αποσπάσματα από την *Πολιτεία* Ζ΄ σε κάθε σκαλί
- Εξισώσεις με MathJax
- Controls για αναπαραγωγή, παύση, επόμενο, προηγούμενο, επανεκκίνηση και επιλογή βήματος
- Δίγλωσσο 🇬🇷 / 🇬🇧 · Responsive
- **Bonus:** εφαρμογή Python για να δοκιμάσεις ένα εκπαιδευμένο MNIST CNN στο δικό σου ζωγραφισμένο ψηφίο

## 🐍 Python Digit Tester

| Αρχείο | Σκοπός |
|--------|--------|
| `train_mnist.py` | Εκπαιδεύει ένα μικρό CNN στο MNIST (5 epochs, ~99% test accuracy) και αποθηκεύει το `mnist_cnn.keras`. |
| `digit_tester.py` | Παράθυρο Tkinter που φορτώνει το `mnist_cnn.keras`, σε αφήνει να ζωγραφίσεις ψηφίο και δείχνει την πρόβλεψη. |
| `mnist_cnn.keras` | Παράγεται από το `train_mnist.py`. Δεν γίνεται commit, δημιούργησέ το τοπικά. |

```
pip install tensorflow numpy pillow     # σε κάποιες διανομές Linux επίσης: sudo apt install python3-tk
python train_mnist.py                   # μία φορά, παράγει το mnist_cnn.keras
python digit_tester.py                  # ζωγράφισε ένα ψηφίο και πάτα Predict
```

**Γιατί μετράει το preprocessing.** Ένα απλό resize από 280×280 σε 28×28 δίνει ψηφία που δεν μοιάζουν καθόλου με το MNIST. Η `preprocess()` αναπαράγει τη διαδικασία του MNIST: crop στο bounding box → κλιμάκωση της μεγαλύτερης πλευράς στα 20 px → κεντράρισμα με βάση το κέντρο μάζας σε καμβά 28×28 → κανονικοποίηση στο `[0, 1]`.

## 🚀 Χρήση

```
https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/08_cnn/cnn_experiment.html
```

Ή κατέβασε το `cnn_experiment.html` και άνοιξέ το σε οποιονδήποτε σύγχρονο browser.

## 🔬 Επιστημονικό Υπόβαθρο

Πηγές: Πλάτων, *Πολιτεία* Ζ΄ (η αλληγορία του σπηλαίου) · LeCun, Bottou, Bengio & Haffner (1998) *Gradient-Based Learning Applied to Document Recognition* · MNIST dataset.

## 🔗 Σειρά: From Plato to Transformers

Post 8 της σειράς. Μετά το πλάτος και το βάθος (Post 7), δείχνει πώς ένα δίκτυο φτιαγμένο για εικόνες ανεβαίνει από την ωμή αίσθηση στην αφαίρεση. Οι μηχανικοί δεν προέβλεψαν τον Πλάτωνα· ξαναβρήκαν τη δομή της ιεραρχικής αφαίρεσης που εκείνος περιέγραφε.

## 📄 Άδεια

MIT License — ελεύθερη χρήση με αναφορά.

---

<div align="center">
Perikles Nikoules — MSc AI · University of Essex · 2025<br>
<i>All feedback is welcome — knowledge is built collectively.</i><br>
<i>Κάθε διόρθωση ή παρατήρηση είναι ευπρόσδεκτη — η γνώση χτίζεται συλλογικά.</i>
</div>
