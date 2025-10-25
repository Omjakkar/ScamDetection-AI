# scam_email_file_inference.py

import pickle
import numpy as np
from scipy.sparse import hstack
import email
from email import policy

# -------------------------
# 1. Load saved artifacts
# -------------------------
with open("artifacts/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("artifacts/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("artifacts/logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------------
# 2. Function to parse email file
# -------------------------
def parse_email(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        msg = email.message_from_file(f, policy=policy.default)
    
    subject = msg['subject'] or ""
    
    # Extract body (handle plain text and multipart)
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_content()
    else:
        body = msg.get_content()
    
    return subject, body

# -------------------------
# 3. Function to predict
# -------------------------
def predict_email(subject, body):
    text = subject + " " + body
    text_tfidf = vectorizer.transform([text])
    
    subject_length = np.array([[len(subject)]])
    subject_length_scaled = scaler.transform(subject_length)
    
    X_combined = hstack([text_tfidf, subject_length_scaled])
    
    pred = model.predict(X_combined)[0]
    
    return "Real Email (Ham)" if pred == 0 else "Scam Email (Spam)"

# -------------------------
# 4. Example usage
# -------------------------
if __name__ == "__main__":
    file_path = r"C:\\Users\\hp\\Downloads\\ScamDetectionDataSets\\demoEmailreal.eml"
    
    subject, body = parse_email(file_path)
    result = predict_email(subject, body)
    
    print("\nPrediction:", result)
