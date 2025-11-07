import streamlit as st
import torch
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Load model and tokenizer once
@st.cache_resource
def load_model_and_tokenizer():
    repo_id = "tsid7710/distillbert-emotion-model"

    with st.spinner("🔄 Loading model and tokenizer... please wait"):
        tokenizer = AutoTokenizer.from_pretrained(repo_id)
        model = AutoModelForSequenceClassification.from_pretrained(repo_id)
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        time.sleep(1.5)

    return tokenizer, model, device


tokenizer, model, device = load_model_and_tokenizer()


# Show success message only the first time it loads (not on reruns)
if "model_loaded" not in st.session_state:
    st.success("✅ Model loaded successfully!")
    st.session_state.model_loaded = True


############## Streamlit Code #################

st.title("💬 Emotion Classifier")

st.markdown("""
### 🧠 About This Project
This app uses a fine-tuned **DistilBERT** model to detect emotions from text.  
It classifies your sentence into one of six emotions — **sadness**, **joy**, **love**, **anger**, **fear**, or **surprise**.  
Simply type a sentence below and click **Find Emotion** to see what the model predicts!
""")

user_input = st.text_input("✍️ Enter a sentence to analyze its emotion:")

classes = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] 

def find_emotion(user_input: str) -> str:
    inputs = tokenizer(text = user_input, return_tensors = "pt", truncation=True, padding=True).to(device)
    with torch.inference_mode():
        output = model(**inputs)
        logits = output.logits
        pred = torch.argmax(logits, dim = -1).item()
    
    print("Prediction: ", pred)
    return classes[pred]


if st.button('Find Emotion'):
    if user_input.strip():
        with st.spinner("🧠 Analyzing emotion..."):
            time.sleep(1) # Short delay for UX
            result = find_emotion(user_input)

        st.success(f"Predicted Emotion: **{result}**")
    else:
        st.warning("⚠️ Please enter a sentence before clicking the button.")