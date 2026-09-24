


def export_clean_data(df, path): 
    df.to_csv(path,index=False)
    return "Done"



def export_customer_report(customer_summary, path):
    customer_summary.to_csv(path,index=False)
    return "Done"


def export_product_report(product_summary, path):
    product_summary.to_csv(path,index=False)
    return "Done"

def export_country_report(country_summary, path):
      country_summary.to_csv(path,index=False)
      return "Done"

def export_monthly_report(monthly_report, path):
      monthly_report.to_csv(path,index=False)
      return "Done"


def generate_data_quality_report(before_df, after_df):

    from pandas import DataFrame

    report = DataFrame({
        'Metric': ['Rows', 'Columns', 'Duplicate', 'MissingValues'],

        'Before': [
            before_df.shape[0],
            before_df.shape[1],
            before_df.duplicated().sum(),
            before_df.isna().sum().sum()
        ],

        'After': [
            after_df.shape[0],
            after_df.shape[1],
            after_df.duplicated().sum(),
            after_df.isna().sum().sum()
        ]
    })

    return report
