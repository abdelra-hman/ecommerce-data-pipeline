
def create_customer_summary(df):
    customer_summary = (
        df.groupby('Customer ID')
        .agg({
            'Revenue': 'sum',
            'Quantity': 'sum'
        })
        .reset_index()
    )

    return customer_summary



def create_product_summary(df):
    Productr_summary = (
        df.groupby('StockCode')
        .agg({
            'Revenue': 'sum',
            'Quantity': 'sum'
        })
        .reset_index()
    )

    return Productr_summary


def create_Country_summary(df):
    Country_summary = (
        df.groupby('Country')
        .agg({
            'Revenue': 'sum',
            'Quantity': 'sum'
        })
        .reset_index()
    )

    return Country_summary





def create_monthly_summary(df):
    monthly_summary = (
        df.groupby(['Year','Month'])
        .agg({
            'Revenue': 'sum',
            'Quantity': 'sum'
        })
        .reset_index()
    )

    return monthly_summary



def get_top_customers(df):
    sorted_df = df.sort_values('Revenue', ascending=False)
    return sorted_df.head(10)



def get_top_countries(df):
    sorted_df = df.sort_values('Revenue', ascending=False)
    return sorted_df.head(10)

def get_top_products(df):
    sorted_df = df.sort_values('Revenue', ascending=False)
    return sorted_df.head(10)












