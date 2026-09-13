# 🤔 Δεν Ξέρω (I Don't Know)
## Why Language Models Guess Instead of Admitting Ignorance

### 🎯 The Core Problem

**The model can say "I don't know."**

The phrase exists in its vocabulary. The issue: **it doesn't pay to say it.**

### 📌 The Experiment: Four Scenes

#### Scene 1: The Quiz
Five questions. Three are **traps** — fabricated facts that sound plausible. Two are real.

The model answers all five with a confidence score. Your task: guess which are traps.

**Result:** Confidence on traps ≈ Confidence on truth. You can't tell them apart.

#### Scene 2: The Incentives
A **payoff matrix** shows:

- If penalty for wrong = 0 (same as "I don't know"), model always guesses
- If penalty for wrong = −2, model abstains when <67% confident
- If penalty for wrong = −5, model abstains when <83% confident

**Finding:** The model is rational. We just didn't give it the right incentives.

#### Scene 3: Calibration
**Typical LLM:** Says "95% confident" but is right only 74% of the time (overconfident).

**Calibrated LLM:** Says "95%" and is right 94–96% of the time.

**Why the gap?** RLHF reward models have bias toward high-confidence outputs.

#### Scene 4: Philosophy
**Socrates:** "I know one thing — that I know nothing" (epistemologically sound).

**Dunning-Kruger:** To see a gap in knowledge, you need the knowledge you lack.

**The thesis:** We didn't build a machine that lies. We built one that is afraid to say "I don't know" — exactly like us.

### 🔬 Research Background

- **Kalai et al. (2025)** — *Why Language Models Hallucinate* (OpenAI → Nature)
- **Leng et al. (2025)** — *Taming Overconfidence in LLMs* (ICLR 2025) — shows calibration is fixable
- **Guo et al. (2017)** — On Calibration of Modern Neural Networks

### 💡 The Proposal

Change three things:

1. **Benchmarks:** Explicit penalty for wrong (−X), zero for "I don't know"
2. **Prompt:** State the penalty clearly
3. **Training:** Use calibrated reward models (PPO-M, PPO-C from ICLR 2025)

### 🚀 How to Use

1. Open `index.html`
2. **Quiz tab:** Guess which facts are traps, then reveal
3. **Incentives tab:** Drag the penalty slider to see when honesty becomes optimal
4. **Calibration tab:** Compare typical vs. well-trained models
5. **Philosophy tab:** Explore Socrates, Dunning-Kruger, and the core thesis

### 🎓 Key Takeaway

The model doesn't *fail* to know its limits. **It was never asked to value knowing them.**

We're building systems that will make medical diagnoses, legal decisions, military targeting decisions.

**The question is not "how intelligent are they?"**

**The question is: Do they know when to stay silent?**

### 📚 Sources

- Kalai, Nachum, Vempala & Zhang (2025) — *Why Language Models Hallucinate*
- Leng, Huang, Zhu & Huang (2025) — *Taming Overconfidence in LLMs*
- Guo et al. (2017) — *On Calibration of Modern Neural Networks*
- Dunning & Kruger (1999) — *Unskilled and Unaware of It*
- Orgad et al. (2024) — *LLMs Know More Than They Show*

---

**Perikles Nikoules** — MSc AI · University of Essex · 2025