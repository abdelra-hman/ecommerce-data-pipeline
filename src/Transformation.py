
from src.ingestion import load_data
import pandas as pd 
import numpy as np 

df = load_data('../Data/raw/online_retail_II.csv')

def create_revenue_column(df):
    df['Revenue'] = df['Quantity']*df['Price']
    return df



def extract_date_features(df):
    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    df['Day'] = df['InvoiceDate'].dt.day
    df['Hour'] = df['InvoiceDate'].dt.hour
    return df


def create_transaction_type(df):
    df['TransactionType'] = np.where(
        df['Quantity'] > 0,
        'Sale',
        'Return'
    )

    return df


def prepare_sales_data(df):
    df = create_revenue_column(df)
    df = extract_date_features(df)
    df = create_transaction_type(df)
    return df
