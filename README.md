# Lead Intelligence Agent



A modular data pipeline that matches identities across sources, enriches profiles, and scores leads probabilistically to produce a ranked list of high-intent prospects.

This project is designed to be run end-to-end with a single command and is usable up to **Step 7** of the pipeline.


## 🚀 What This Project Does

The Lead Intelligence Agent performs three core operations:

### Progressive Identity Matching (Step 5)
Merges profiles from multiple sources (e.g., LinkedIn, PubMed) into unified identities.

### Profile Enrichment (Step 6)
Adds derived signals and intent features to each merged profile.

### Probability Scoring & Ranking (Step 7)
Computes a probabilistic lead score and outputs a ranked list of leads.

The final output is a CSV file of ranked leads, ready for downstream use (sales, outreach, analytics, etc.).

---

## 🧠 Pipeline Overview

```mermaid



Raw Data
   │
   ├── LinkedIn Profiles
   ├── PubMed Profiles
   │
   ▼
[ Step 5 ] Identity Matching
   │
   ▼
[ Step 6 ] Enrichment Engine
   │
   ▼
[ Step 7 ] Probability Scoring
   │
   ▼
Final Ranked Leads (CSV)
📁 Project Structure
Plaintext

project-root/
│
├── main.py                     # Single entry point (Steps 5–7)
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
│   └── profile_merger.py       # Step 5
│
├── enrichment/
│   └── enrichment_engine.py    # Step 6
│
├── scoring/
│   └── probability_engine.py   # Step 7
│
└── logs/
⚙️ Requirements
Python 3.9+

Pandas

NumPy

All dependencies are listed in requirements.txt.

🛠️ Setup Instructions (New User)
1️⃣ Clone the repository
Bash

git clone [https://github.com/Auth0r-C0dez/Intelligent-Business-Lead-Finder](https://github.com/Auth0r-C0dez/Intelligent-Business-Lead-Finder)
cd project-root
2️⃣ Create and activate a virtual environment
Windows:

Bash

python -m venv venv
venv\Scripts\activate
macOS / Linux:

Bash

python -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
Bash

pip install -r requirements.txt
4️⃣ Add input data
Place the following files into the data/raw/ directory:

data/raw/linkedin_profiles.csv

data/raw/pubmed_profiles.csv

Note: These files are required. The pipeline will not run without them.

▶️ How to Run the Project (Up to Step 7)
Run the full pipeline with one command:

Bash

python main.py
This executes:

Step 5: Identity matching

Step 6: Profile enrichment

Step 7: Probability scoring

📤 Output
After successful execution, you will get:

data/processed/final_ranked_leads.csv

This file contains:

Unified profiles

Enriched attributes

Final probability score

Ranked lead list

This is the final product output of the project.



Do not run individual step files manually.

main.py is the only supported entry point.

The pipeline assumes CSV-based structured inputs.

🔧 Extensibility
This project is designed to be extended with:

Config files (config.yaml)

CLI arguments

Database or API inputs

Real-time or batch execution

✔ Production-ready pipeline core

📌 One-Line Usage Summary
Bash

python main.py
