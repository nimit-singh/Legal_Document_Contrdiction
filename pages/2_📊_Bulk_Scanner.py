import streamlit as st
import pandas as pd
import json
import joblib
from io import BytesIO

bytes = BytesIO()
st.set_page_config(layout="centered")
st.title("Legal ANLI Bulk Scanner")
st.markdown("---")
st.header("🔎 Bulk Premium Scanner")

MODEL_PATH = "legal_ANLI_model.joblib"
VECTORIZER_PATH = "legal_ANLI_model_vectorizer.joblib"
def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer
model, vectorizer = load_model()
st.header("1. Download Sample Templates")

col1, col2, col3 = st.columns(3)

sample_csv = pd.DataFrame(
    [
        {
            "Premise": "The contract is valid for two years.",
            "Hypothesis": "The agreement lasts for 24 months.",
        },
        {
            "Premise": "The tenant must pay rent by the 5th of each month.",
            "Hypothesis": "Rent is due before the 10th of every month.",
        },
        {
            "Premise": "The company is not liable for damages caused by natural disasters.",
            "Hypothesis": "The company is responsible for damages caused by floods.",
        },
        {
            "Premise": "Employees are entitled to 20 days of paid leave annually.",
            "Hypothesis": "Workers receive 20 paid vacation days each year.",
        },
        {
            "Premise": "The agreement will terminate if either party breaches the terms.",
            "Hypothesis": "The contract continues even after a breach.",
        },
        {
            "Premise": "Payment must be made in USD.",
            "Hypothesis": "Payment can be made in euros.",
        },
        {
            "Premise": "The policy covers only fire-related damages.",
            "Hypothesis": "The policy includes coverage for theft.",
        },
        {
            "Premise": "The service is available 24/7.",
            "Hypothesis": "The service is not available at night.",
        },
        {
            "Premise": "The license is non-transferable.",
            "Hypothesis": "The license can be transferred to another person.",
        },
        {
            "Premise": "Delivery will occur within 7 business days.",
            "Hypothesis": "Delivery will take more than two weeks.",
        },
    ]
)
sample_excel = pd.DataFrame(
    [
        {
            "Premise": "The contract is valid for two years.",
            "Hypothesis": "The agreement lasts for 24 months.",
        },
        {
            "Premise": "The tenant must pay rent by the 5th of each month.",
            "Hypothesis": "Rent is due before the 10th of every month.",
        },
        {
            "Premise": "The company is not liable for damages caused by natural disasters.",
            "Hypothesis": "The company is responsible for damages caused by floods.",
        },
        {
            "Premise": "Employees are entitled to 20 days of paid leave annually.",
            "Hypothesis": "Workers receive 20 paid vacation days each year.",
        },
        {
            "Premise": "The agreement will terminate if either party breaches the terms.",
            "Hypothesis": "The contract continues even after a breach.",
        },
        {
            "Premise": "Payment must be made in USD.",
            "Hypothesis": "Payment can be made in euros.",
        },
        {
            "Premise": "The policy covers only fire-related damages.",
            "Hypothesis": "The policy includes coverage for theft.",
        },
        {
            "Premise": "The service is available 24/7.",
            "Hypothesis": "The service is not available at night.",
        },
        {
            "Premise": "The license is non-transferable.",
            "Hypothesis": "The license can be transferred to another person.",
        },
        {
            "Premise": "Delivery will occur within 7 business days.",
            "Hypothesis": "Delivery will take more than two weeks.",
        },
    ]
)
sample_json = pd.DataFrame(
    [
        {
            "Premise": "The contract is valid for two years.",
            "Hypothesis": "The agreement lasts for 24 months.",
        },
        {
            "Premise": "The tenant must pay rent by the 5th of each month.",
            "Hypothesis": "Rent is due before the 10th of every month.",
        },
        {
            "Premise": "The company is not liable for damages caused by natural disasters.",
            "Hypothesis": "The company is responsible for damages caused by floods.",
        },
        {
            "Premise": "Employees are entitled to 20 days of paid leave annually.",
            "Hypothesis": "Workers receive 20 paid vacation days each year.",
        },
        {
            "Premise": "The agreement will terminate if either party breaches the terms.",
            "Hypothesis": "The contract continues even after a breach.",
        },
        {
            "Premise": "Payment must be made in USD.",
            "Hypothesis": "Payment can be made in euros.",
        },
        {
            "Premise": "The policy covers only fire-related damages.",
            "Hypothesis": "The policy includes coverage for theft.",
        },
        {
            "Premise": "The service is available 24/7.",
            "Hypothesis": "The service is not available at night.",
        },
        {
            "Premise": "The license is non-transferable.",
            "Hypothesis": "The license can be transferred to another person.",
        },
        {
            "Premise": "Delivery will occur within 7 business days.",
            "Hypothesis": "Delivery will take more than two weeks.",
        },
    ]
)

csv_data = sample_csv.to_csv(index=False)
with col1:
    st.download_button(
        label="Download Sample CSV",
        data=csv_data,
        file_name="sample.csv",
        mime="text/csv",
    )
sample_excel = sample_excel.to_excel(bytes, index=False)
with col2:
    st.download_button(
        label="Download Sample Excel",
        data=bytes.getvalue(),
        file_name="sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
json_data = sample_json.to_json(orient="records", indent=4)
with col3:
    st.download_button(
        label="Download Sample JSON",
        data=json_data,
        file_name="sample.json",
        mime="application/json",
    )

st.markdown("---")

st.header("2. Upload Your File")
st.write(
    "Upload a CSV, Excel, or JSON file with 'Premise' and 'Hypothesis' columns to get predictions in bulk."
)
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

label_map = {0: "Contradiction ❌", 1: "Entailment ✅", 2: "Neutral ⚖️"}

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, encoding="utf-8")
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".json"):
        data = json.load(uploaded_file)
        df = pd.DataFrame(data)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    else:
        st.error("Unsupported file type. Please upload a CSV, Excel, or JSON file.")
        st.stop()

    if "Premise" not in df.columns or "Hypothesis" not in df.columns:
        st.error("File must contain 'Premise' and 'Hypothesis' columns.")
        st.stop()

    if st.button("Predict in Bulk"):
        df["Combined"] = df["Premise"] + " " + df["Hypothesis"]
        vec = vectorizer.transform(df["Combined"])
        df["Prediction"] = model.predict(vec)
        df["Prediction"] = df["Prediction"].map(label_map)
        st.write("Predictions:")
        st.dataframe(df[["Premise", "Hypothesis", "Prediction"]])
        output_csv = df[["Premise", "Hypothesis", "Prediction"]].to_csv(index=False)

        st.header("3. Download Your Predictions")
        st.success("Click the button below to download predictions as a CSV file.")
        st.download_button(
            label="Download Predictions as CSV",
            data=output_csv,
            file_name="predictions.csv",
            mime="text/csv",
        )
