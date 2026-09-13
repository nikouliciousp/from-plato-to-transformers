# 🏛 From Plato to Transformers
### An interactive series connecting ancient Greek philosophy with modern Machine Learning

[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Tools](https://img.shields.io/badge/Interactive_Tools-6-00d4ff?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](#)

> *"The unexamined life is not worth living."* — Socrates

---

## 📖 About This Series

**From Plato to Transformers** is a collection of interactive, browser-based tools that explore modern Machine Learning concepts — and the striking ways ancient Greek philosophers described similar ideas.

Each tool is a single self-contained HTML file: no installation, no dependencies, fully bilingual (🇬🇧 / 🇬🇷), and mobile-responsive. All the ML content is technically accurate and, where it matters, backed by peer-reviewed sources.

**A note on the philosophy:** The philosophical mappings are offered as *analogies that aid understanding* — not as claims that ancient thinkers literally predicted neural networks. Some connections run deeper than others; all are documented.

---

## 🧪 The Tools

| # | Tool | Topic | Philosopher(s) |
|---|------|-------|----------------|
| 1 | **Neurons** | Additive vs Divisive vs Hybrid neurons | Plato · Aristotle · Leibniz |
| 2 | **ReLU** | Linear vs ReLU vs Sigmoid activations | Parmenides · Heraclitus · Aristotle |
| 3 | **Vanishing Gradient** | Why deep networks stopped learning | Zeno · Heraclitus · Aristotle |
| 4 | **Paradigms** | 5 thinking paradigms solve one problem | Parmenides · Aristotle · Leibniz · Hume · Epicurus |
| 5 | **Δεν Ξέρω** | Why AI doesn't know it doesn't know | Socrates |
| 6 | **Associationism** | Aristotle's 4 laws of memory → ML | Aristotle |

### 1. 🧠 [Neurons Experiment](01_neurons/neurons_experiment.html)
Three neuron types trained live. The **Divisive Neuron** corresponds to a real brain mechanism (Divisive Normalization) and the core of Transformer attention (`QKᵀ/√d`).

### 2. ⚡ [ReLU Experiment](02_relu/relu_experiment.html)
An ablation study: same architecture, only the hidden activation changes. Shows why Sigmoid causes vanishing gradient and why ReLU (and then GELU) won.

### 3. 📉 [Vanishing Gradient Experiment](04_vanishing_gradient/vanishing_gradient_experiment.html)
A depth slider shows how `0.25¹⁰ ≈ 1 in a million` — why Sigmoid killed deep networks, and how ReLU preserved the signal. Verified mathematics.

### 4. 🧩 [Paradigms Experiment](03_paradigms/paradigms_experiment.html)
The same problem (cardiac risk) solved five ways — rule-based, predicate logic, neural network, Bayes, kNN — with live evaluation metrics and a radar chart.

### 5. 🤔 [Δεν Ξέρω (I Don't Know)](05_den_xero/den_xero_experiment.html)
Why language models guess instead of abstaining. Four scenes, fact-checked against OpenAI/Nature (2025) and ICLR 2025. Connected to the book «I DON'T KNOW».

### 6. 🔗 [Associationism Experiment](06_associationism/associationism_experiment.html)
Aristotle's four laws of associative memory (350 BC) mapped to Hebb's rule, gradient descent, embeddings and contrastive learning.

---

## 🎯 Who Is This For?

- **AI / ML students** — free, structured, interactive study material
- **Career-switchers into AI** — intuitive entry points to hard concepts
- **Educators** — ready-to-use classroom demonstrations
- **The curious** — anyone who wants to understand what AI really does

---

## 🚀 Usage

Every tool is one HTML file. Open it in any browser — that's it. No build step, no server, no dependencies.

For GitHub Pages: rename the file to `index.html` in its repository, then enable Pages (Settings → Pages → main → root).

---

## 🔬 Accuracy & Sources

Where claims could be checked, they were. Key references:

- Carandini & Heeger (2012) — Divisive Normalization
- Nair & Hinton (2010) — ReLU · Hendrycks & Gimpel (2016) — GELU
- Hochreiter (1991) — Vanishing gradient · Glorot et al. (2011)
- Kalai, Nachum, Vempala & Zhang (2025) — *Why Language Models Hallucinate* (OpenAI → Nature)
- Leng et al. (2025) — *Taming Overconfidence in LLMs* (ICLR 2025)
- Aristotle — *On Memory and Recollection* · Hebb (1949) · Chen et al. (2020, SimCLR) · Radford et al. (2021, CLIP)

---

## 📄 License

MIT License — free to use, modify and share with attribution.

---
---

# 🏛 From Plato to Transformers (Ελληνικά)
### Μια διαδραστική σειρά που συνδέει την αρχαία ελληνική φιλοσοφία με το σύγχρονο Machine Learning

> *"Ὁ ἀνεξέταστος βίος οὐ βιωτὸς ἀνθρώπῳ."* — Σωκράτης

---

## 📖 Σχετικά με τη Σειρά

Το **From Plato to Transformers** είναι μια συλλογή διαδραστικών εργαλείων που τρέχουν στον browser και εξερευνούν έννοιες του σύγχρονου Machine Learning — και τους εντυπωσιακούς τρόπους με τους οποίους αρχαίοι ελληνικοί φιλόσοφοι περιέγραψαν παρόμοιες ιδέες.

Κάθε εργαλείο είναι ένα αυτόνομο αρχείο HTML: χωρίς εγκατάσταση, χωρίς εξαρτήσεις, πλήρως δίγλωσσο (🇬🇷 / 🇬🇧) και responsive σε mobile. Όλο το ML περιεχόμενο είναι τεχνικά ακριβές και, όπου σχετικό, υποστηρίζεται από peer-reviewed πηγές.

**Σημείωση για τη φιλοσοφία:** Οι φιλοσοφικές αντιστοιχίες προσφέρονται ως *αναλογίες που βοηθούν την κατανόηση* — όχι ως ισχυρισμοί ότι αρχαίοι στοχαστές κυριολεκτικά προέβλεψαν τα νευρωνικά δίκτυα. Ορισμένες συνδέσεις είναι βαθύτερες από άλλες· όλες τεκμηριώνονται.

---

## 🧪 Τα Εργαλεία

| # | Εργαλείο | Θέμα | Φιλόσοφος(οι) |
|---|----------|------|---------------|
| 1 | **Neurons** | Additive vs Divisive vs Hybrid νευρώνες | Πλάτων · Αριστοτέλης · Leibniz |
| 2 | **ReLU** | Linear vs ReLU vs Sigmoid activations | Παρμενίδης · Ηράκλειτος · Αριστοτέλης |
| 3 | **Vanishing Gradient** | Γιατί τα βαθιά δίκτυα σταμάτησαν να μαθαίνουν | Ζήνων · Ηράκλειτος · Αριστοτέλης |
| 4 | **Paradigms** | 5 παραδείγματα σκέψης λύνουν ένα πρόβλημα | Παρμενίδης · Αριστοτέλης · Leibniz · Hume · Επίκουρος |
| 5 | **Δεν Ξέρω** | Γιατί το AI δεν ξέρει ότι δεν ξέρει | Σωκράτης |
| 6 | **Associationism** | Οι 4 νόμοι μνήμης του Αριστοτέλη → ML | Αριστοτέλης |

### 1. 🧠 [Neurons Experiment](01_neurons/neurons_experiment.html)
Τρεις τύποι νευρώνα εκπαιδεύονται ζωντανά. Ο **Divisive Neuron** αντιστοιχεί σε πραγματικό μηχανισμό του εγκεφάλου (Divisive Normalization) και στο κέντρο του Transformer attention (`QKᵀ/√d`).

### 2. ⚡ [ReLU Experiment](02_relu/relu_experiment.html)
Ablation study: ίδια αρχιτεκτονική, αλλάζει μόνο το hidden activation. Δείχνει γιατί η Sigmoid προκαλεί vanishing gradient και γιατί η ReLU (και μετά GELU) νίκησαν.

### 3. 📉 [Vanishing Gradient Experiment](04_vanishing_gradient/vanishing_gradient_experiment.html)
Ένα slider βάθους δείχνει ότι `0.25¹⁰ ≈ 1 στο εκατομμύριο` — γιατί η Sigmoid σκότωνε τα βαθιά δίκτυα, και πώς η ReLU διατήρησε το σήμα. Επαληθευμένα μαθηματικά.

### 4. 🧩 [Paradigms Experiment](03_paradigms/paradigms_experiment.html)
Το ίδιο πρόβλημα (καρδιακός κίνδυνος) λυμένο με πέντε τρόπους — rule-based, predicate logic, neural network, Bayes, kNN — με live δείκτες αξιολόγησης και radar chart.

### 5. 🤔 [Δεν Ξέρω (I Don't Know)](05_den_xero/den_xero_experiment.html)
Γιατί τα γλωσσικά μοντέλα μαντεύουν αντί να απέχουν. Τέσσερις σκηνές, επαληθευμένες ως προς OpenAI/Nature (2025) και ICLR 2025. Συνδεδεμένη με το βιβλίο «I DON'T KNOW».

### 6. 🔗 [Associationism Experiment](06_associationism/associationism_experiment.html)
Οι τέσσερις νόμοι συνειρμικής μνήμης του Αριστοτέλη (350 π.Χ.) αντιστοιχισμένοι στον κανόνα Hebb, το gradient descent, τα embeddings και contrastive learning.

---

## 🎯 Για Ποιον Είναι;

- **Φοιτητές AI / ML** — δωρεάν, οργανωμένο, διαδραστικό υλικό μελέτης
- **Επαγγελματίες που στρέφονται στο AI** — διαισθητικά σημεία εισόδου σε δύσκολες έννοιες
- **Εκπαιδευτικούς** — έτοιμες επιδείξεις για την τάξη
- **Τους περίεργους** — όποιον θέλει να καταλάβει τι πραγματικά κάνει το AI

---

## 🚀 Χρήση

Κάθε εργαλείο είναι ένα αρχείο HTML. Άνοιξέ το σε οποιονδήποτε browser — τίποτα άλλο. Χωρίς build, χωρίς server, χωρίς εξαρτήσεις.

Για GitHub Pages: μετονόμασε το αρχείο σε `index.html` στο repository του, μετά ενεργοποίησε το Pages (Settings → Pages → main → root).

---

## 🔬 Ακρίβεια & Πηγές

Όπου οι ισχυρισμοί μπορούσαν να ελεγχθούν, ελέγχθηκαν. Βασικές αναφορές:

- Carandini & Heeger (2012) — Divisive Normalization
- Nair & Hinton (2010) — ReLU · Hendrycks & Gimpel (2016) — GELU
- Hochreiter (1991) — Vanishing gradient · Glorot et al. (2011)
- Kalai, Nachum, Vempala & Zhang (2025) — *Why Language Models Hallucinate* (OpenAI → Nature)
- Leng et al. (2025) — *Taming Overconfidence in LLMs* (ICLR 2025)
- Aristotle — *On Memory and Recollection* · Hebb (1949) · Chen et al. (2020, SimCLR) · Radford et al. (2021, CLIP)

---

## 📄 Άδεια

MIT License — ελεύθερη χρήση, τροποποίηση και διαμοιρασμός με αναφορά.

---

<div align="center">

**Perikles Nikoules** — MSc AI · University of Essex · 2025

<i>All feedback is welcome — knowledge is built collectively.</i><br>
<i>Κάθε διόρθωση ή παρατήρηση είναι ευπρόσδεκτη — η γνώση χτίζεται συλλογικά.</i>

</div>
