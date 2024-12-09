import pandas as pd
import numpy as np

# # def load_kff_data(filepath):
# #     """Load and perform initial cleaning of KFF healthcare data"""
# #     df = pd.read_csv(filepath)
# #     df = df.replace('N/A', np.nan)
# #     return df

# # def load_cms_data(filepath):
# #     """Load and perform initial cleaning of CMS healthcare data"""
# #     df = pd.read_csv(filepath)
# #     df = df.replace('N/A', np.nan)
# #     return df
# # src/data_loader.py

# def load_and_clean_data(file_path, skip_rows=2, row_limit=None):
#     """
#     Load and clean healthcare spending data.

#     Parameters:
#     - file_path (str): Path to the CSV file.
#     - skip_rows (int): Number of rows to skip at the top.
#     - row_limit (int): Maximum number of rows to read.

#     Returns:
#     - pd.DataFrame: Cleaned dataframe with healthcare spending data.
#     """
#     df = pd.read_csv(file_path, 
#                      skiprows=skip_rows, 
#                      thousands=',', 
#                      nrows=row_limit)
#     df['Health Spending per Capita'] = (df['Health Spending per Capita']
#                                         .str.replace('$', '', regex=False)
#                                         .str.replace(',', '', regex=False)
#                                         .astype(float))
#     return df

regions = {
    'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island',
                 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania'],
    'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota',
                'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas'],
    'South': ['Delaware', 'Maryland', 'District of Columbia', 'Virginia', 'West Virginia',
              'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Kentucky',
              'Tennessee', 'Alabama', 'Mississippi', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas'],
    'West': ['Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah',
             'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii']
}

def load_and_prepare_data():
    """
    Load and prepare the healthcare spending data for analysis.

    Returns:
    tuple: (complete_df, state_data, us_average)
    """
    file_path = '../data/raw/kff_healthcare_spending_per_capita_2020.csv'
    df = pd.read_csv(file_path, skiprows=2, thousands=',', nrows=52)
    df['Health Spending per Capita'] = (df['Health Spending per Capita']
                                        .str.replace('$', '', regex=False)
                                        .str.replace(',', '', regex=False)
                                        .astype(float))

    # Separate state data from US average
    state_data = df[df['Location'] != 'United States'].copy()
    us_average = df[df['Location'] == 'United States']['Health Spending per Capita'].values[0]

    state_data['Region'] = state_data['Location'].apply(
        lambda x: next((region for region, states in regions.items() if x in states), 'Other')
    )

    return df, state_data, us_average