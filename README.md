# ⚖️ Legal Document Contradiction Detection using NLP

An AI-powered application that detects **contradictions between legal statements** using Natural Language Processing (NLP) and Machine Learning.

This project helps identify whether two legal sentences are **Contradictory, Neutral, or Entailment**, making it useful for legal analysis and document verification.

---

## 🚀 Features

* 🔹 Detect contradictions between two legal statements

* 🔹 **Manual Prediction**

  * Input two sentences
  * Get relationship (Contradiction / Neutral / Entailment)

* 🔹 **Bulk Scanner**

  * Upload CSV file
  * Analyze multiple sentence pairs

* 🔹 Built using NLP techniques

* 🔹 Interactive Streamlit interface

---

## 📂 Project Structure

```id="v6u2l9"
Legal_Document_Contrdiction/
│
├── pages/                                 # Streamlit pages (Bulk Scanner)
├── Legal Document Anli.ipynb              # Model training notebook
├── Manual_Prediction.py                  # Manual prediction app
├── p.py                                  # Helper / main script
├── Report.pdf                            # Project report
├── Legal Document Contradiction Report.docx
├── requirements.txt                      # Dependencies
└── README.md                             # Documentation
```

---

## 🧠 Model Details

* **Task:** Natural Language Inference (NLI)

* **Classes:**

  * Contradiction ❌
  * Neutral ⚖️
  * Entailment ✅

* **Techniques Used:**

  * Text preprocessing
  * Vectorization (TF-IDF / embeddings)
  * Machine Learning model

---

## 🛠️ Installation

### 1. Clone the repository

```bash id="qk5r4d"
git clone https://github.com/nimit-datahub/Legal_Document_Contrdiction.git
cd Legal_Document_Contrdiction
```

### 2. Install dependencies

```bash id="3rkxq8"
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash id="7x8zv2"
streamlit run Manual_Prediction.py
```

---

## 📊 How to Use

### 🔹 Manual Prediction

* Enter **Statement 1**
* Enter **Statement 2**
* Get relationship output:

  * Contradiction
  * Neutral
  * Entailment

### 🔹 Bulk Scanner

* Upload CSV file
* Required format:

```id="o4v4hg"
Sentence1,Sentence2
The contract is valid,The contract is invalid
Payment is required,Payment must be made
```

---

## 📸 Screenshots

*Add screenshots of your app here (recommended)*

---

## 📈 Future Improvements

* 🔹 Use advanced models (BERT, Legal-BERT)
* 🔹 Improve semantic understanding
* 🔹 Deploy on cloud
* 🔹 Add real-time legal document analysis

---

## 👨‍💻 Author

**Nimit Singh**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
