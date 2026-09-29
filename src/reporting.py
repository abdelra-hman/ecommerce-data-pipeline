


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
    report['Difference'] = report['After'] - report['Before']

    return report

def generate_business_summary(df):
    import pandas as pd
    total_revenue = df['Revenue'].sum()
    total_quantity = df['Quantity'].sum()
    CustomerCount = df['Customer ID'].nunique()
    CountriesCount = df['Country'].nunique()
    summary = pd.DataFrame({
    'Metric': [
        'Total Revenue',
        'Total Quantity',
        'Customer Count',
        'Countries Count'
    ],

    'Value': [
        total_revenue,
        total_quantity,
        CustomerCount,
        CountriesCount
    ]
    })
    return summary


def export_business_summary(business_summary, path):
      business_summary.to_csv(path,index=False)
      return "Done"


def generate_business_insights(df,customer_summary,product_summary, country_summary,monthly_summary):
    insights = []

    total_revenue = df['Revenue'].sum()
    insights.append(f"Total Revenue: {total_revenue}")

    total_quantity = df['Quantity'].sum()
    insights.append(f"Total Quantity: {total_quantity}")

    top_customer = customer_summary.sort_values(
        'Revenue',
        ascending=False
    ).iloc[0]

    insights.append(
        f"Top Customer: {top_customer['Customer ID']} | "
        f"Revenue: {top_customer['Revenue']}"
    )

    top_product = product_summary.sort_values(
        'Revenue',
        ascending=False
    ).iloc[0]

    insights.append(
        f"Top Product: {top_product['StockCode']} | "
        f"Revenue: {top_product['Revenue']}"
    )

    top_country = country_summary.sort_values(
        'Revenue',
        ascending=False
    ).iloc[0]

    insights.append(
        f"Top Country: {top_country['Country']} | "
        f"Revenue: {top_country['Revenue']}"
    )

    top_month = monthly_summary.sort_values(
        'Revenue',
        ascending=False
    ).iloc[0]

    insights.append(
        f"Top Month: {top_month['Year']}-{top_month['Month']} | "
        f"Revenue: {top_month['Revenue']}"
    )

    return insights


def export_business_insights(business_insights, path):
    with open(path, 'w', encoding='utf-8') as file:
        for insight in business_insights:
            file.write(insight + '\n')

    return "Done"

def export_data_quality_report(data_quality_report, path):
    data_quality_report.to_csv(path, index=False)
    return "Done"









