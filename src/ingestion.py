import pandas as pd 

def load_data(path):
    try:
        df=pd.read_csv(path)
        return df
    except FileNotFoundError :
        raise FileNotFoundError(f"This Path is Wrong : {path}")



def get_data_overview(df):
    RowsCount = df.shape[0]
    ColumnCount = df.shape[1]
    ColumnNames = df.columns
    DataTypes = df.dtypes
    MemoryUsage = df.memory_usage(deep=True)    
    
    return {
    'RowCount': RowsCount,
    'ColumnCount': ColumnCount,
    'ColumnNames': ColumnNames,
    'DataTypes': DataTypes,
    'MemoryUsage': MemoryUsage
}



def  check_missing_values(df):
    return df.isnull().sum()



def check_duplicates(df):
    return df.duplicated().sum()







   



