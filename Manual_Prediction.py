import os
os.system("pip install joblib")
import streamlit as st
import joblib
import os
import gdown

MODEL_PATH = "legal_ANLI_model.joblib"
VECTORIZER_PATH = "legal_ANLI_model_vectorizer.joblib"

MODEL_URL = "https://drive.google.com/uc?id=1K0uh_QKe6AKZ-TuqcI61x_KqnGNvQaqK"
VECTORIZER_URL = "https://drive.google.com/uc?id=10aE587ZFD3wQaRn2SVEUBSaAYCGujosR"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

    if not os.path.exists(VECTORIZER_PATH):
        gdown.download(VECTORIZER_URL, VECTORIZER_PATH, quiet=False)

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

model, vectorizer = load_model()
# Label mapping
label_map = {0: "Contradiction ❌", 1: "Entailment ✅", 2: "Neutral ⚖️"}

# Title
st.title("⚖️ Legal ANLI Contradiction Detection System")
st.expander("ℹ️ About this tool").write(
    """
This tool uses a machine learning model to evaluate logical relationships between two statements.

🔍 Input:
- Premise: Original statement  
- Hypothesis: Statement to evaluate  

📊 Output:
- Entailment  
- Contradiction  
- Neutral  

Designed for legal document analysis and contradiction detection.
"""
)
with st.expander("ℹ️ How this works"):
    st.write(
        """
    - Enter a Premise and Hypothesis  
    - Click Predict  
    - The model analyzes semantic meaning  
    - Output shows logical relationship  
    """
    )
st.markdown("---")
# Inputs
premise = st.text_area("Enter Premise")
hypothesis = st.text_area("Enter Hypothesis")

# Button
if st.button("Predict"):
    if premise and hypothesis:

        # Combine text
        text = premise + " " + hypothesis

        # Vectorize
        vec = vectorizer.transform([text])

        # Predict
        pred = model.predict(vec)[0]

        # Output
        st.write("Prediction:", label_map[pred])

    else:
        st.write("Please enter both fields")
