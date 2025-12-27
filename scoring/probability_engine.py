import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

# --- Scoring helpers ---

def score_role_fit(title):
    if not isinstance(title, str):
        return 0
    t = title.lower()
    if any(k in t for k in ["toxicology", "safety", "hepatic", "3d"]):
        return 30
    return 0

def score_company_intent(is_funded, funding_stage):
    if is_funded and funding_stage in ["series a", "series b"]:
        return 20
    return 0

def score_technographic(company_industry):
    if isinstance(company_industry, str) and "biotech" in company_industry.lower():
        return 15
    return 0

def score_location(hq_country):
    hubs = ["usa", "switzerland", "uk", "germany"]
    if isinstance(hq_country, str) and hq_country.lower() in hubs:
        return 10
    return 0

import pandas as pd

def score_scientific_intent(paper_title, publication_year):
    if (
        isinstance(paper_title, str)
        and pd.notna(publication_year)
        and int(publication_year) >= 2023
    ):
        keywords = ["toxicity", "in vitro", "liver", "safety", "3d"]
        if any(k in paper_title.lower() for k in keywords):
            return 40
    return 0


# --- Main scoring ---

def compute_score(row):
    score = 0
    score += score_role_fit(row.get("title"))
    score += score_company_intent(row.get("is_funded"), row.get("funding_stage"))
    score += score_technographic(row.get("company_industry"))
    score += score_location(row.get("company_hq_country"))
    score += score_scientific_intent(row.get("paper_title"), row.get("publication_year"))
    return min(score, 100)

def run_scoring(input_path, output_path):
    logger.info(f"Loading enriched profiles from {input_path}")
    df = pd.read_csv(input_path)

    logger.info("Computing propensity scores")
    df["probability_score"] = df.apply(compute_score, axis=1)

    logger.info("Ranking leads")
    df = df.sort_values(by="probability_score", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1

    df.to_csv(output_path, index=False)
    logger.info(f"Ranked leads saved to {output_path}")
