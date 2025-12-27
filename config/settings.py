# config/settings.py

# ----------------------------
# PROJECT METADATA
# ----------------------------
PROJECT_NAME = "Lead Intelligence Agent"
VERSION = "0.1.0"

# ----------------------------
# TARGET JOB TITLES (IDENTIFICATION)
# ----------------------------
TARGET_TITLES = [
    "Director of Toxicology",
    "Head of Toxicology",
    "Director of Safety Assessment",
    "Head of Preclinical Safety",
    "VP Preclinical",
    "VP Toxicology"
]

# ----------------------------
# SCIENTIFIC KEYWORDS (INTENT)
# ----------------------------
SCIENTIFIC_KEYWORDS = [
    "Drug-Induced Liver Injury",
    "DILI",
    "Liver Toxicity",
    "Hepatic",
    "3D cell culture",
    "Organ-on-chip",
    "Hepatic spheroids",
    "Investigative Toxicology",
    "NAMs",
    "New Approach Methodologies"
]

# ----------------------------
# LOCATION HUBS (PRIORITY)
# ----------------------------
LOCATION_HUBS = [
    "Boston",
    "Cambridge",
    "San Francisco",
    "Bay Area",
    "Basel",
    "London",
    "Oxford",
    "Cambridge UK"
]

# ----------------------------
# SCORING WEIGHTS (0–100 SYSTEM)
# ----------------------------
SCORING_WEIGHTS = {
    "role_fit": 30,
    "scientific_intent": 40,
    "company_intent": 20,
    "location": 10
}

# ----------------------------
# FUNDING STAGE SCORES
# ----------------------------
FUNDING_SCORES = {
    "Series A": 15,
    "Series B": 20,
    "Series C": 20,
    "IPO": 20,
    "Grant Funded": 10,
    "Unknown": 0
}

# ----------------------------
# DATA LIMITS (DEMO SAFETY)
# ----------------------------
MAX_PROFILES = 100
