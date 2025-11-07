## 💬 Emotion Classifier — DistilBERT Fine-Tuned Model

### 🧠 Overview

The **Emotion Classifier** is a lightweight web app built using **Streamlit** and **Hugging Face Transformers**.
It uses a **fine-tuned DistilBERT model** to detect the **underlying emotion** expressed in text.
The model predicts one of six emotions:
**`sadness`**, **`joy`**, **`love`**, **`anger`**, **`fear`**, or **`surprise`**.

This project demonstrates how transformer-based models can be fine-tuned for **emotion detection** and deployed as an **interactive NLP application**.

---

### Demo

Try the live app on Streamlit Cloud:

👉 [**Live Demo on Streamlit Cloud**](https://huggingface.co/spaces/tsid7710/emotion-classifier)

---

### 📊 Example Outputs

| Input Sentence                               | Predicted Emotion |
| -------------------------------------------- | ----------------- |
| “I’m so excited for tomorrow!”               | 😄 Joy            |
| “This makes me really sad.”                  | 😢 Sadness        |
| “You’re the best thing that happened to me.” | ❤️ Love           |
| “I can’t believe this happened again.”       | 😠 Anger          |
| “I’m worried about the results.”             | 😨 Fear           |
| “Wow! That’s amazing!”                       | 😲 Surprise       |

---

### ⚙️ Model Details

* **Base Model:** `distilbert-base-uncased`
* **Fine-tuned Dataset:** [**dair-ai/emotion**](https://huggingface.co/datasets/dair-ai/emotion)
* **Number of Classes:** 6
* **Evaluation Metrics:** Accuracy, F1-score

---

### 🖥️ How to Run Locally

#### 1. Clone the repository

```bash
git clone https://github.com/sudharshanreddyt/emotion-classifier.git
cd emotion-classifier
```

#### 2. Create and sync the environment

```bash
uv sync
```

#### 3. Run the Streamlit app

   ```bash
   streamlit run main.py
   ```

#### 4. Open in your browser:
   `http://localhost:8501`

---

### 👨‍💻 Author

**Sudharshan Reddy Thammaiahgari**
📍 Passionate about NLP, ML, and AI-driven applications
🔗 [GitHub](https://github.com/sudharshanreddyt/) | [Hugging Face](https://huggingface.co/tsid7710)
