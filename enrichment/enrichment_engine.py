import pandas as pd
from urllib.parse import urlparse
from utils.logger import get_logger

logger = get_logger(__name__)

def enrich_company_info(df):
    logger.info("Starting company enrichment")

    # Placeholder enrichment (no external APIs yet)
    df["company_industry"] = "biotech/pharma"
    df["company_size"] = "unknown"
    df["company_hq_location"] = df.get("company_hq_location", "")
    df["company_website"] = ""

    df["company_enriched"] = True
    return df


def enrich_funding_info(df):
    logger.info("Starting funding enrichment")

    df["funding_stage"] = "unknown"
    df["last_funding_year"] = ""
    df["is_funded"] = False

    return df


def enrich_location_info(df):
    logger.info("Starting location enrichment")

    df["person_country"] = df["person_location"].fillna("").apply(
        lambda x: x.split()[-1] if x else ""
    )

    df["company_hq_country"] = df["company_hq_location"].fillna("").apply(
        lambda x: x.split()[-1] if x else ""
    )

    def location_type(row):
        if row["person_location"] and row["company_hq_location"]:
            return "remote" if row["person_location"] != row["company_hq_location"] else "hq"
        return "unknown"

    df["location_type"] = df.apply(location_type, axis=1)
    df["location_enriched"] = True

    return df


def enrich_contact_info(df):
    logger.info("Starting contact enrichment")

    df["business_email"] = ""
    df["phone_number"] = ""

    def extract_domain(website):
        if website:
            return urlparse(website).netloc.replace("www.", "")
        return ""

    df["email_domain"] = df["company_website"].apply(extract_domain)
    df["contact_enriched"] = False

    return df


def run_enrichment(input_path, output_path):
    logger.info(f"Loading merged profiles from {input_path}")
    df = pd.read_csv(input_path)

    df = enrich_company_info(df)
    df = enrich_funding_info(df)
    df = enrich_location_info(df)
    df = enrich_contact_info(df)

    df.to_csv(output_path, index=False)
    logger.info(f"Enriched profiles saved to {output_path}")
