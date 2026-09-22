
from src.ingestion import load_data
import pandas as pd 


df = load_data('../Data/raw/online_retail_II.csv')


def remove_duplicates(df):
    df = df[~df.duplicated()]
    return df


def handle_missing_values(df):
    description_map = (
        df.groupby("StockCode")["Description"]
        .agg(lambda x: x.dropna().iloc[0] if x.dropna().nunique() == 1 else None)
    )

    df["Description"] = df["Description"].fillna(
        df["StockCode"].map(description_map)
    )

    return df

def clean_invalid_quantities(df):
    Q1 = df['Quantity'].quantile(0.25)
    Q3 = df['Quantity'].quantile(0.75)
    IQR= Q3-Q1 
    LowerBound= Q1-1.5*IQR
    UpperBound= Q3+1.5*IQR
    mask = (df['Quantity'] >= LowerBound) & (df['Quantity'] <= UpperBound)
    df = df[mask]  
    return df


def clean_invalid_prices(df):
    df = df[df['Price'] > 0]
    return df 

def convert_data_types(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Customer ID'] =df['Customer ID'] .astype('Int64')
    df['Quantity'] =df['Quantity'] .astype('Int64')
    df['Price'] =df['Price'] .astype('float')
    return 

def clean_text_columns(df):
    df['Description'] = df['Description'].str.strip()
    df['StockCode'] = df['StockCode'].str.strip()
    df['Country'] = df['Country'].str.strip()
    return df


def clean_data(df):
    df=remove_duplicates(df)
    df=handle_missing_values(df)
    df=clean_invalid_quantities(df)
    df=clean_invalid_prices(df)
    df=convert_data_types(df)
    df=clean_text_columns(df)
    return df







