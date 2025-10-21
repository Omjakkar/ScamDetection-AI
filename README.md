# ScamDetection-AI

#### **⚠️ This project is currently in development. Some features and documentation may be incomplete. ⚠️**

This software project is an AI Based Scam detection system. It scans Emails, Messages and detects suspicious intention.



---

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Logic](#logic)
- [Example Usage](#example-usage)
- [AI Model](#AI-Model)
- [License](#license)

---

## Features

- 

---

## Directory Structure

```
email-legitimacy-detector/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── docker-compose.yml
├── setup.py
│
├── backend/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_auth.py          # Gmail/Yahoo/Microsoft OAuth endpoints
│   │   ├── routes_scan.py          # Upload .eml or scan inbox endpoint
│   │   ├── routes_user.py          # Manage users, feedback
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py               # Environment & app configuration
│   │   ├── security.py             # Token, API key, session security
│   │   ├── logger.py               # Logging configuration
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email_parser.py         # Parse MIME/.eml and extract parts
│   │   ├── feature_extractor.py    # Build ML features from email
│   │   ├── model_inference.py      # Load & run AI model predictions
│   │   ├── url_analyzer.py         # Detect suspicious URLs/domains
│   │   ├── dkim_spf_checker.py     # DKIM/SPF/DMARC validation
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── email_scan_request.py   # Pydantic input schema
│   │   ├── email_scan_response.py  # Pydantic output schema
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py                   # SQLAlchemy engine/session
│   │   ├── schemas.py              # ORM models (user, scan_log)
│   │   ├── crud.py                 # CRUD operations
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       ├── hashing.py
│
├── model/
│   ├── pipeline.py                 # Unified train → save pipeline
│   │
│   ├── training/
│   │   ├── preprocess.py           # Clean + normalize datasets
│   │   ├── feature_engineering.py  # Extract header/body/link features
│   │   ├── train_baseline.py       # Train logistic/XGBoost model
│   │   ├── train_bert.py           # Fine-tune transformer model
│   │   ├── evaluate.py             # Evaluate & generate metrics
│   │
│   ├── artifacts/
│   │   ├── vectorizer.pkl
│   │   ├── baseline_model.pkl
│   │   └── transformer_model/
│   │       ├── config.json
│   │       ├── pytorch_model.bin
│   │       └── tokenizer.json
│
├── data/
│   ├── raw/
│   │   ├── enron/
│   │   ├── spamassassin/
│   │   ├── phishing_kaggle/
│   │
│   ├── processed/
│   │   ├── combined_train.csv
│   │   └── combined_test.csv
│   │
│   └── external/
│       ├── domain_reputation.csv
│       └── url_blacklist.csv
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   ├── components/
│   │   │   ├── UploadEmail.jsx     # .eml upload UI
│   │   │   ├── ScanResultCard.jsx  # Shows AI risk result
│   │   │   └── AuthButton.jsx      # OAuth buttons
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── Login.jsx
│   │   └── assets/
│   │       ├── logo.png
│   │       └── styles.css
│
├── scripts/
│   ├── init_db.py
│   ├── fetch_emails_gmail.py
│   ├── verify_spf_dkim.py
│   └── clean_data.py
│
├── config/
│   ├── config.yaml
│   ├── logging.conf
│   ├── model_config.json
│   └── secrets.json.example
│
├── tests/
│   ├── test_email_parser.py
│   ├── test_feature_extractor.py
│   ├── test_model_inference.py
│   └── test_routes.py
│
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.model
│   ├── nginx.conf
│   └── entrypoint.sh
│
└── docs/
    ├── architecture.png
    ├── data_flow_diagram.png
    ├── oauth_flow.png
    ├── API_REFERENCE.md
    ├── MODEL_OVERVIEW.md
    └── DEPLOYMENT_GUIDE.md


```

---


## Logic

```


```


## Example Usage


### Graphical Mode

```
```

---

## AI Models

 

--- 


### Manual (Python 3.8 +)

```bash
pip install -r requirement.txt
```

---

## License

This project is licensed under the MIT License

---
