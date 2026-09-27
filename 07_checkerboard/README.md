# 🧩 Checkerboard Experiment
### How width and depth build a neural network — a 4×4 checkerboard

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Raw.githack-00d4ff?style=for-the-badge)](https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/07_checkerboard/checkerboard_experiment.html)
[![Language](https://img.shields.io/badge/Language-EN_/_ΕΛ-7c3aed?style=for-the-badge)](#)
[![MSc AI](https://img.shields.io/badge/MSc_AI-University_of_Essex-10b981?style=for-the-badge)](#)
[![Series](https://img.shields.io/badge/Series-Post_7-f59e0b?style=for-the-badge)](#)

> *The whole is more than the sum of its parts.* — Aristotle, adapted for the neural network

---

## 🎯 What It Shows

A visual and interactive explanation of how **width** and **depth** solve a non-linear classification problem.

The experiment uses a 4×4 checkerboard: points alternate between positive and negative classes across sixteen cells. The user follows the construction of a small network step by step:

1. **The sample** — 50 points in the `[0,1] × [0,1]` plane, arranged as a checkerboard.
2. **Two inputs** — `x₁` and `x₂`, the coordinates of each point.
3. **First hidden layer** — six neurons, each representing one straight cut: three vertical and three horizontal lines.
4. **Second hidden layer** — two neurons that combine the stripe information into column and row parity.
5. **Output neuron** — compares the two parity signals and produces the final checkerboard decision.

The final didactic architecture is:

```text
2 → 6 → 2 → 1
```

The central lesson is that **width cuts the original space into useful regions**, while **depth combines those regions into higher-level concepts**.

## 🧠 Width vs Depth

Each neuron in the first hidden layer corresponds to one straight boundary in the original input space. Six neurons create six cuts:

- three vertical cuts at `x₁ = 0.25`, `0.5`, and `0.75`
- three horizontal cuts at `x₂ = 0.25`, `0.5`, and `0.75`

These cuts identify the row and column of each point, but they do not yet express the checkerboard rule. The second hidden layer receives the outputs of the first layer and combines them through parity-like concepts.

The deeper layers still perform linear separations, but in the **concept space produced by the previous layer**, not directly in the original `x₁, x₂` plane. This is why depth can represent patterns that look like complex regions or polygons in the original space.

> **Important note:** The `2 - 6 - 2 - 1` network is a teaching simplification. A practically trainable network for a 4×4 checkerboard may require more neurons in the second hidden layer or an additional hidden layer, because parity over several values is a difficult problem.

## 🎛 Features

- 13-step animated explanation of the network construction
- Interactive scatter plot of the 4×4 checkerboard
- Cumulative vertical and horizontal decision boundaries
- Live neural-network diagram with animated data flow
- Individual thumbnails showing what each neuron sees
- Visualisation of column parity, row parity, and final output
- Width and depth annotations on the final architecture
- Play, pause, next, previous, restart, and step navigation controls
- Bilingual 🇬🇧 / 🇬🇷 · Responsive · Zero dependencies

## 🚀 Usage

```
https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/07_checkerboard/checkerboard_experiment.html
```

Or download `checkerboard_experiment.html` and open it in any modern browser.

## 🔗 Series: From Plato to Transformers

Post 7 of the series. It connects the geometry of classification with the architectural question that defines deep learning: **how many neurons do we need, and how many layers?**

## 📄 License

MIT License — free to use with attribution.

---
---

# 🧩 Checkerboard Experiment (Ελληνικά)
### Πώς το πλάτος και το βάθος χτίζουν ένα νευρωνικό δίκτυο — μια σκακιέρα 4×4

> *Το όλον είναι μεγαλύτερο από το άθροισμα των μερών του.* — Αριστοτέλης, προσαρμοσμένο για το νευρωνικό δίκτυο

## 🎯 Τι Δείχνει

Μια οπτική και διαδραστική εξήγηση για το πώς το **πλάτος** και το **βάθος** λύνουν ένα μη γραμμικό πρόβλημα ταξινόμησης.

Το πείραμα χρησιμοποιεί μια σκακιέρα 4×4: τα σημεία εναλλάσσονται ανάμεσα σε θετικές και αρνητικές κλάσεις μέσα σε δεκαέξι κελιά. Ο χρήστης παρακολουθεί βήμα-βήμα την κατασκευή ενός μικρού δικτύου:

1. **Το δείγμα** — 50 σημεία στο επίπεδο `[0,1] × [0,1]`, οργανωμένα σαν σκακιέρα.
2. **Δύο είσοδοι** — `x₁` και `x₂`, οι συντεταγμένες κάθε σημείου.
3. **Πρώτο κρυφό επίπεδο** — έξι νευρώνες, καθένας από τους οποίους αντιστοιχεί σε μία ευθεία τομή: τρεις κάθετες και τρεις οριζόντιες.
4. **Δεύτερο κρυφό επίπεδο** — δύο νευρώνες που συνδυάζουν την πληροφορία των λωρίδων σε parity στήλης και γραμμής.
5. **Νευρώνας εξόδου** — συγκρίνει τα δύο parity signals και παράγει την τελική απόφαση της σκακιέρας.

Η τελική διδακτική αρχιτεκτονική είναι:

```text
2 → 6 → 2 → 1
```

Το βασικό μάθημα είναι ότι το **πλάτος κόβει τον αρχικό χώρο** σε χρήσιμες περιοχές, ενώ το **βάθος συνδυάζει** αυτές τις περιοχές σε έννοιες υψηλότερου επιπέδου.

## 🧠 Πλάτος και Βάθος

Κάθε νευρώνας του πρώτου κρυφού επιπέδου αντιστοιχεί σε ένα όριο στον αρχικό χώρο εισόδου. Οι έξι νευρώνες δημιουργούν έξι τομές:

- τρεις κάθετες τομές στα `x₁ = 0.25`, `0.5` και `0.75`
- τρεις οριζόντιες τομές στα `x₂ = 0.25`, `0.5` και `0.75`

Οι τομές αυτές εντοπίζουν τη γραμμή και τη στήλη κάθε σημείου, αλλά δεν εκφράζουν ακόμη τον κανόνα της σκακιέρας. Το δεύτερο κρυφό επίπεδο λαμβάνει τις εξόδους του πρώτου και τις συνδυάζει σε έννοιες που μοιάζουν με parity.

Τα βαθύτερα επίπεδα εξακολουθούν να κάνουν γραμμικούς διαχωρισμούς, αλλά στον **χώρο εννοιών που δημιούργησε το προηγούμενο επίπεδο**, όχι απευθείας στο αρχικό επίπεδο `x₁, x₂`. Γι’ αυτό το βάθος μπορεί να αναπαριστά μοτίβα που φαίνονται σαν σύνθετες περιοχές ή πολύγωνα στον αρχικό χώρο.

> **Σημαντική σημείωση:** Το δίκτυο `2 - 6 - 2 - 1` είναι διδακτική απλοποίηση. Ένα πρακτικά εκπαιδεύσιμο δίκτυο για σκακιέρα 4×4 μπορεί να χρειάζεται περισσότερους νευρώνες στο δεύτερο κρυφό επίπεδο ή ένα επιπλέον κρυφό επίπεδο, επειδή το parity πολλών τιμών είναι δύσκολο πρόβλημα.

## 🎛 Χαρακτηριστικά

- 13 βήματα animated εξήγησης της κατασκευής του δικτύου
- Διαδραστικό scatter plot της σκακιέρας 4×4
- Συσσωρευτικές κάθετες και οριζόντιες γραμμές διαχωρισμού
- Live διάγραμμα του νευρωνικού δικτύου με animated ροή δεδομένων
- Ξεχωριστές μικρογραφίες που δείχνουν τι «βλέπει» κάθε νευρώνας
- Οπτικοποίηση του parity στήλης, του parity γραμμής και της τελικής εξόδου
- Ενδείξεις πλάτους και βάθους στην τελική αρχιτεκτονική
- Controls για αναπαραγωγή, παύση, επόμενο, προηγούμενο, επανεκκίνηση και επιλογή βήματος
- Δίγλωσσο 🇬🇷 / 🇬🇧 · Responsive · Μηδενικές εξαρτήσεις

## 🚀 Χρήση

```
https://raw.githack.com/nikouliciousp/from-plato-to-transformers/main/07_checkerboard/checkerboard_experiment.html
```

Ή κατέβασε το `checkerboard_experiment.html` και άνοιξέ το σε οποιονδήποτε σύγχρονο browser.

## 🔗 Σειρά: From Plato to Transformers

Post 7 της σειράς. Συνδέει τη γεωμετρία της ταξινόμησης με το αρχιτεκτονικό ερώτημα που ορίζει το deep learning: **πόσους νευρώνες χρειαζόμαστε και πόσα επίπεδα;**

## 📄 Άδεια

MIT License — ελεύθερη χρήση με αναφορά.

---

<div align="center">
Perikles Nikoules — MSc AI · University of Essex · 2025<br>
<i>All feedback is welcome — knowledge is built collectively.</i><br>
<i>Κάθε διόρθωση ή παρατήρηση είναι ευπρόσδεκτη — η γνώση χτίζεται συλλογικά.</i>
</div>
