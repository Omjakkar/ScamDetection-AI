# scam_email_logistic_final.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from scipy.sparse import hstack
from sklearn.preprocessing import StandardScaler
import pickle
import os

# -------------------------
# 1. Load dataset
# -------------------------
df = pd.read_csv(r"C:\\Users\\hp\\projects\\ScamDetection-AI\\data\\processed\\Enron_sample_1000.csv", 
                 low_memory=False, 
                 quotechar='"', 
                 encoding='utf-8')

# -------------------------
# 2. Handle missing values
# -------------------------
# Drop rows with missing target
df = df.dropna(subset=['label'])

# Fill missing text fields
df['subject'] = df['subject'].fillna('').astype(str)
df['body'] = df['body'].fillna('').astype(str)
df['text'] = df['subject'] + ' ' + df['body']

# Optional meta feature
df['subject_length'] = df['subject'].apply(len)

# -------------------------
# 3. Features and labels
# -------------------------
X_text = df['text']
X_meta = df[['subject_length']]
y = df['label']

# Double-check no NaNs remain
assert y.isna().sum() == 0, "Target y contains NaNs!"
assert X_text.isna().sum() == 0, "Text feature contains NaNs!"
assert X_meta.isna().sum().sum() == 0, "Meta features contain NaNs!"

# -------------------------
# 4. Check class distribution
# -------------------------
print("Class distribution:\n", y.value_counts())

# -------------------------
# 5. Train-test split (stratified)
# -------------------------
X_text_train, X_text_test, X_meta_train, X_meta_test, y_train, y_test = train_test_split(
    X_text, X_meta, y, test_size=0.2, random_state=42, stratify=y
)

print("Train class distribution:\n", y_train.value_counts())
print("Test class distribution:\n", y_test.value_counts())

# -------------------------
# 6. TF-IDF vectorization for text
# -------------------------
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_text_train_tfidf = vectorizer.fit_transform(X_text_train)
X_text_test_tfidf = vectorizer.transform(X_text_test)

# -------------------------
# 7. Scale meta features
# -------------------------
scaler = StandardScaler()
X_meta_train_scaled = scaler.fit_transform(X_meta_train)
X_meta_test_scaled = scaler.transform(X_meta_test)

# -------------------------
# 8. Combine text + meta features
# -------------------------
X_train_combined = hstack([X_text_train_tfidf, X_meta_train_scaled])
X_test_combined = hstack([X_text_test_tfidf, X_meta_test_scaled])

# -------------------------
# 9. Train Logistic Regression
# -------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_combined, y_train)

# -------------------------
# 10. Evaluate model
# -------------------------
y_pred = model.predict(X_test_combined)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# -------------------------
# 11. Save artifacts for inference
# -------------------------
os.makedirs("artifacts", exist_ok=True)

with open("artifacts/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("artifacts/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("artifacts/logistic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model and artifacts saved successfully!")
