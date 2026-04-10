import gdown
import os
import joblib

MODEL_PATH = "legal_ANLI_model.joblib"
VECTORIZER_PATH = "legal_ANLI_model_vectorizer.joblib"

MODEL_URL = "https://drive.google.com/uc?id=1K0uh_QKe6AKZ-TuqcI61x_KqnGNvQaqK"
VECTORIZER_URL = "https://drive.google.com/uc?id=10aE587ZFD3wQaRn2SVEUBSaAYCGujosR"

if not os.path.exists(MODEL_PATH):
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

if not os.path.exists(VECTORIZER_PATH):
    gdown.download(VECTORIZER_URL, VECTORIZER_PATH, quiet=False)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)