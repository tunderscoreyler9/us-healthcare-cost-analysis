import pandas as pd
import numpy as np

# def load_kff_data(filepath):
#     """Load and perform initial cleaning of KFF healthcare data"""
#     df = pd.read_csv(filepath)
#     df = df.replace('N/A', np.nan)
#     return df

# def load_cms_data(filepath):
#     """Load and perform initial cleaning of CMS healthcare data"""
#     df = pd.read_csv(filepath)
#     df = df.replace('N/A', np.nan)
#     return df
# src/data_loader.py

def load_and_clean_data(file_path, skip_rows=2, row_limit=None):
    """
    Load and clean healthcare spending data.

    Parameters:
    - file_path (str): Path to the CSV file.
    - skip_rows (int): Number of rows to skip at the top.
    - row_limit (int): Maximum number of rows to read.

    Returns:
    - pd.DataFrame: Cleaned dataframe with healthcare spending data.
    """
    df = pd.read_csv(file_path, 
                     skiprows=skip_rows, 
                     thousands=',', 
                     nrows=row_limit)
    df['Health Spending per Capita'] = (df['Health Spending per Capita']
                                        .str.replace('$', '', regex=False)
                                        .str.replace(',', '', regex=False)
                                        .astype(float))
    return df
