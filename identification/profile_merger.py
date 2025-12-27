# identification/profile_merger.py

import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def load_csv(filepath):
    logger.info(f"Loading data from {filepath}")
    return pd.read_csv(filepath)

def merge_profiles(pubmed_df, linkedin_df):
    """
    Merge LinkedIn and PubMed profiles based on full name (exact match).
    """

    logger.info("Starting profile merge based on full name")

    # Normalize full names for matching
    linkedin_df["full_name_normalized"] = linkedin_df["name"].str.lower().str.strip()
    pubmed_df["full_name_normalized"] = pubmed_df["name"].str.lower().str.strip()

    # Merge LinkedIn + PubMed based on normalized full name
    merged = pd.merge(
        linkedin_df,
        pubmed_df,
        on="full_name_normalized",
        how="outer",  # Keep all profiles
        suffixes=("_linkedin", "_pubmed")
    )

    logger.info(f"Merged dataset contains {len(merged)} profiles")
    return merged

def save_to_csv(df, filepath):
    df.to_csv(filepath, index=False)
    logger.info(f"Saved merged profiles to {filepath}")
