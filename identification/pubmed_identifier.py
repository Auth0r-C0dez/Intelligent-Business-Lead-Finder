# identification/pubmed_identifier.py

import requests
from datetime import datetime
from config.settings import SCIENTIFIC_KEYWORDS, MAX_PROFILES
from utils.logger import get_logger
import xml.etree.ElementTree as ET

logger = get_logger(__name__)

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def search_pubmed():
    """
    Searches PubMed for recent papers using scientific keywords.
    """
    logger.info("Starting PubMed search")

    query = " OR ".join(SCIENTIFIC_KEYWORDS)

    params = {
        "db": "pubmed",
        "term": query,
        "retmax": MAX_PROFILES,
        "retmode": "json",
        "sort": "pub+date"
    }

    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()

    data = response.json()
    id_list = data.get("esearchresult", {}).get("idlist", [])

    logger.info(f"Found {len(id_list)} PubMed articles")
    return id_list

def fetch_paper_details(pubmed_ids):
    """
    Fetches paper details including authors and publication dates.
    """
    logger.info("Fetching paper details from PubMed")

    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }

    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()

    return response.text




def parse_pubmed_xml(xml_data):
    """
    Parses PubMed XML to extract authors and paper metadata.
    """
    root = ET.fromstring(xml_data)
    profiles = []

    for article in root.findall(".//PubmedArticle"):
        title_elem = article.find(".//ArticleTitle")
        date_elem = article.find(".//PubDate/Year")

        title = title_elem.text if title_elem is not None else "Unknown"
        year = int(date_elem.text) if date_elem is not None else None

        for author in article.findall(".//Author"):
            last = author.find("LastName")
            first = author.find("ForeName")

            if last is None or first is None:
                continue

            profiles.append({
                "name": f"{first.text} {last.text}",
                "paper_title": title,
                "publication_year": year,
                "source": "PubMed"
            })

    logger.info(f"Extracted {len(profiles)} author profiles")
    return profiles
