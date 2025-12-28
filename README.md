# Lead Intelligence Agent
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

**A modular data pipeline that matches identities across sources, enriches profiles, and scores leads probabilistically to produce a ranked list of high-intent prospects.**

This project is designed to be run end-to-end with a single command and is fully functional up to **Step 7** of the pipeline.

---

## 🚀 What This Project Does

The Lead Intelligence Agent performs three core operations:

1.  **Progressive Identity Matching (Step 5)**
    * Merges profiles from multiple sources (e.g., LinkedIn, PubMed) into unified identities.
2.  **Profile Enrichment (Step 6)**
    * Adds derived signals and intent features to each merged profile.
3.  **Probability Scoring & Ranking (Step 7)**
    * Computes a probabilistic lead score and outputs a ranked list of leads.

The final output is a CSV file of ranked leads, ready for downstream use (sales, outreach, analytics, etc.).

---

## 🧠 Pipeline Overview

```mermaid
graph TD;
    LinkedIn[LinkedIn Profiles] --> Step5[Step 5: Identity Matching];
    PubMed[PubMed Profiles] --> Step5;
    Step5 --> Step6[Step 6: Enrichment Engine];
    Step6 --> Step7[Step 7: Probability Scoring];
    Step7 --> Output[Final Ranked Leads CSV];
 ```  

project-root/
│
├── main.py                     
├── requirements.txt            
│
├── data/
│   ├── raw/
│   │   ├── linkedin_profiles.csv
│   │   └── pubmed_profiles.csv
│   │
│   └── processed/
│       ├── merged_profiles.csv
│       ├── enriched_profiles.csv
│       └── final_ranked_leads.csv
│
├── identification/
│   └── profile_merger.py       
│
├── enrichment/
│   └── enrichment_engine.py    
│
├── scoring/
│   └── probability_engine.py   
│
└── logs/
---
Requirements
Python 3.9+

Pandas

NumPy

All specific dependencies are listed in requirements.txt.

🛠️ Setup Instructions
1️⃣ Clone the repository

```Bash
git clone [https://github.com/Auth0r-C0dez/Intelligent-Business-Lead-Finder]
cd project-root
```
2️⃣ Create and activate a virtual environment
Windows:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

4️⃣ Add input data
Place the following files into the data/raw/ directory. The pipeline will not run without them.

data/raw/linkedin_profiles.csv
data/raw/pubmed_profiles.csv

▶️ How to Run the Project
Run the full pipeline (Steps 5–7) with one command:
```python main.py```
📤 Output
After successful execution, the final results will be generated at:

data/processed/final_ranked_leads.csv

This file contains:

Unified user profiles

Enriched attributes

Final probability scores

Ranked lead list



