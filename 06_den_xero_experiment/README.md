# 🤐 "Δεν Ξέρω" Experiment — Uncertainty & Calibration

**Bonus: Γιατί τα AI μαντεύουν αντί να πουν "δεν ξέρω"**

## 📌 Τι μαθαίνεις

Τρεις σημαντικές ιδέες:

1. **Hallucination Problem:** Τα LLMs παράγουν αποδεκτά-ακουόμενα αλλά ψευδή texts
2. **Incentive Problem:** Δεν συμφέρει στα μοντέλα να πουν "δεν ξέρω"
3. **Calibration Problem:** Το confidence score δεν λέει αν το μοντέλο έχει δίκιο

## 🎮 Πώς παίζεις

### 🎭 Quiz Section
5 ερωτήσεις, 3 από αυτές είναι **παγίδες** (πράγματα που δεν υπάρχουν)

- Μαντέψεις ποια είναι αληθινή
- Το μοντέλο απαντά με confidence %
- Κάνε κλικ "Αποκάλυψη" για να δεις το αποτέλεσμα

### 🎛 Incentive Lab
Αλλάξε την ποινή για λάθος απάντηση και δες πώς αλλάζει η βέλτιστη στρατηγική

- **Penalty = 0:** Η μαντεψιά έχει πάντα θετική αναμενόμενη τιμή
- **Penalty = -2:** Τώρα υπάρχει λόγος να πεις "δεν ξέρω"

### 📊 Calibration Section
Σύγκρινε:
- **Τυπικό LLM:** Overconfident (95% λέει, 74% έχει δίκιο)
- **Calibrated Model:** Ακριβής (90% λέει, 89% έχει δίκιο)

## 🔬 Key Findings

| Problem | Αιτία | Λύση |
|---------|-------|------|
| **Hallucination** | Το μοντέλο δεν ξέρει τα όρια του | Explicit penalty + calibration |
| **Overconfidence** | RLHF βελτιστοποιεί το "ακούγεται σίγουρο" | PPO-M / PPO-C training |
| **Wrong Benchmarks** | Λάθος = 0, "δεν ξέρω" = 0 (ίδια ποινή) | Κάνε visible τη penalty στο prompt |

## 📚 Real World Impact

- **SimpleQA Benchmark:** o4-mini φαίνεται καλύτερο από GPT-5-mini — γιατί μαντεύει σε όλα
- **Medical Diagnosis:** Δεν θέλεις overconfident μοντέλο που σε λέει λάθος με σιγουριά 95%

## 🏛️ Φιλοσοφία

**Σωκράτης:** "ἓν οἶδα ὅτι οὐδὲν οἶδα" — Μόνο γνώση των ορίων σου είναι αληθινή γνώση

---

## 🧬 Live Demo

**[Άνοιξε το πείραμα →](./den_xero_experiment.html)**

---

## 📚 References

- Kalai, N., Vempala, S., & Zhang, Y. (2025). "Why Language Models Hallucinate"
- Leng, K., Huang, J., Zhu, W., & Huang, Y. (2025). "Taming Overconfidence in LLMs: Reward Calibration in RLHF" (ICLR 2025)
- Orgad, H. et al. (2024). "LLMs Know More Than They Show"
- Cheang, K. et al. (2025). "Do LLMs Really Know What They Don't Know?"
- Guo, C. et al. (2017). "On Calibration of Modern Neural Networks"

**Δημιουργός:** Perikles Nikoules | 2025
