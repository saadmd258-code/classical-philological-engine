```markdown
# 📜 Classical Arabic Philological & Prosodic Reasoning Engine
> **A Deterministic & AI-Orchestrated System for Classical Arabic Computational Metrics (العروض), Morphology (الصرف), and Deep Syntactic Anatomy (الإعراب).**

---

## 🏛️ Epistemological Overview
Standard Large Language Models frequently fail at the precise mathematical and grammatical boundaries of classical Arabic philology. This project resolves that gap by coupling a **deterministic phonetic-prosodic rule engine** with a **structured neural agent pipeline**, enforcing classical grammatical conventions from the historical Basra and Kufa traditions.

---

## 🔬 Tri-Layered Architecture

1. **Prosodic Rule Engine (`core_engine.py`):** 
   - Converts fully diacritized Arabic text into phonetic binary metrics (`/` for movement, `o` for quiescence).
   - Dynamically scans and identifies classical poetic meters (أبحر الخليل الستة عشر).

2. **Philological Reasoning Pipeline (`ai_pipeline.py`):**
   - Dissects every token into its root (*الجذر*), morphological measure (*الوزن الصرفي*), and syntactic role (*الموقع الإعرابي*).
   - Validated via strict Pydantic schemas with automatic schema sanitization for functional particles (*حروف المعاني*).
   - Resilient multi-tier model routing and retry fallbacks.

3. **Philological Dashboard (`app.py`):**
   - Dark-mode, typography-focused classical interface powered by Streamlit.

---

## 🛠️ Local Installation & Execution

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/classical-philological-engine.git](https://github.com/your-username/classical-philological-engine.git)
cd classical-philological-engine

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Configure Secrets

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### 4. Run the Engine

```bash
streamlit run app.py

```

---

## 📜 Academic Integrity & License

Distributed under the MIT License. Designed for academic research, philological preservation, and computational Arabic linguistics.