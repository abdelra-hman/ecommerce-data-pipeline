from src.ingestion import load_data
from src.cleaning import clean_data
from src.Transformation import prepare_sales_data
from src.analysis import (
    create_customer_summary,
    create_product_summary,
    create_Country_summary,
    create_monthly_summary
)
from src.reporting import (
    export_clean_data,
    export_customer_report,
    export_product_report,
    export_country_report,
    export_monthly_report,
    generate_data_quality_report,
    export_data_quality_report,
    generate_business_summary,
    export_business_summary,
    generate_business_insights,
    export_business_insights
)


# =========================
# Paths
# =========================

RAW_PATH = "Data/raw/online_retail_II.csv"

CLEAN_PATH = "Data/processed/clean_sales.csv"
CUSTOMER_PATH = "Data/processed/customer_summary.csv"
PRODUCT_PATH = "Data/processed/product_summary.csv"
COUNTRY_PATH = "Data/processed/country_summary.csv"
MONTHLY_PATH = "Data/processed/monthly_sales.csv"

QUALITY_PATH = "reports/data_quality_report.csv"
BUSINESS_SUMMARY_PATH = "reports/business_summary.csv"
BUSINESS_INSIGHTS_PATH = "reports/business_insights.txt"


def run_pipeline():

    print("Starting Pipeline...")

    # =========================
    # 1. Load
    # =========================

    print("\n1. Loading data...")

    raw_df = load_data(RAW_PATH)

    print(f"Raw Rows: {raw_df.shape[0]}")
    print(f"Raw Columns: {raw_df.shape[1]}")


    # =========================
    # 2. Cleaning
    # =========================

    print("\n2. Cleaning data...")

    clean_df = clean_data(raw_df.copy())

    print(f"Clean Rows: {clean_df.shape[0]}")
    print(f"Clean Columns: {clean_df.shape[1]}")


    # =========================
    # 3. Transformation
    # =========================

    print("\n3. Transforming data...")

    clean_df = prepare_sales_data(clean_df)


    # =========================
    # 4. Analysis
    # =========================

    print("\n4. Creating analysis summaries...")

    customer_summary = create_customer_summary(clean_df)

    product_summary = create_product_summary(clean_df)

    country_summary = create_Country_summary(clean_df)

    monthly_summary = create_monthly_summary(clean_df)


    # =========================
    # 5. Data Quality Report
    # =========================

    print("\n5. Generating data quality report...")

    data_quality_report = generate_data_quality_report(
        raw_df,
        clean_df
    )


    # =========================
    # 6. Business Summary
    # =========================

    print("\n6. Generating business summary...")

    business_summary = generate_business_summary(clean_df)


    # =========================
    # 7. Business Insights
    # =========================

    print("\n7. Generating business insights...")

    business_insights = generate_business_insights(
        clean_df,
        customer_summary,
        product_summary,
        country_summary,
        monthly_summary
    )


    # =========================
    # 8. Export
    # =========================

    print("\n8. Exporting results...")

    export_clean_data(
        clean_df,
        CLEAN_PATH
    )

    export_customer_report(
        customer_summary,
        CUSTOMER_PATH
    )

    export_product_report(
        product_summary,
        PRODUCT_PATH
    )

    export_country_report(
        country_summary,
        COUNTRY_PATH
    )

    export_monthly_report(
        monthly_summary,
        MONTHLY_PATH
    )

    export_data_quality_report(
        data_quality_report,
        QUALITY_PATH
    )

    export_business_summary(
        business_summary,
        BUSINESS_SUMMARY_PATH
    )

    export_business_insights(
        business_insights,
        BUSINESS_INSIGHTS_PATH
    )


    # =========================
    # Finished
    # =========================

    print("\nPipeline completed successfully!")

    print("\nGenerated files:")

    print("Data/processed/clean_sales.csv")
    print("Data/processed/customer_summary.csv")
    print("Data/processed/product_summary.csv")
    print("Data/processed/country_summary.csv")
    print("Data/processed/monthly_sales.csv")

    print("reports/data_quality_report.csv")
    print("reports/business_summary.csv")
    print("reports/business_insights.txt")


if __name__ == "__main__":
    run_pipeline()