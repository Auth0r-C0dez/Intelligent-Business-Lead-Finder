from identification.profile_merger import run_profile_merge
from enrichment.enrichment_engine import run_enrichment
from scoring.probability_engine import run_scoring

def main():
    run_profile_merge(
        linkedin_path="data/raw/linkedin_profiles.csv",
        pubmed_path="data/raw/pubmed_profiles.csv",
        output_path="data/processed/merged_profiles.csv"
    )

    run_enrichment(
        input_path="data/processed/merged_profiles.csv",
        output_path="data/processed/enriched_profiles.csv"
    )

    run_scoring(
        input_path="data/processed/enriched_profiles.csv",
        output_path="data/processed/final_ranked_leads.csv"
    )

    print("Pipeline completed successfully (Steps 5–7)")

if __name__ == "__main__":
    main()

