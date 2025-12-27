# identification/linkedin_identifier.py

import pandas as pd
from config.settings import TARGET_TITLES
from utils.logger import get_logger

logger = get_logger(__name__)


def load_linkedin_profiles(filepath):
    """
    Loads LinkedIn-style profile data from CSV.
    """
    logger.info("Loading LinkedIn profiles")
    return pd.read_csv(filepath)


def filter_relevant_profiles(df):
    """
    Filters profiles based on target job titles.
    """
    logger.info("Filtering LinkedIn profiles by target titles")

    def is_relevant(title):
        return any(target.lower() in title.lower() for target in TARGET_TITLES)

    filtered_df = df[df["title"].apply(is_relevant)].copy()
    filtered_df["source"] = "LinkedIn"

    logger.info(f"Filtered down to {len(filtered_df)} relevant LinkedIn profiles")
    return filtered_df
