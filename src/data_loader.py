import pandas as pd
import numpy as np

def load_kff_data(filepath):
    """Load and perform initial cleaning of KFF healthcare data"""
    df = pd.read_csv(filepath)
    df = df.replace('N/A', np.nan)
    return df

def load_cms_data(filepath):
    """Load and perform initial cleaning of CMS healthcare data"""
    df = pd.read_csv(filepath)
    df = df.replace('N/A', np.nan)
    return df
