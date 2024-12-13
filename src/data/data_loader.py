import pandas as pd
import numpy as np

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

def load_and_prepare_data(file_path):
    """
    Load and prepare the healthcare spending data for analysis.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - tuple: (complete_df, state_data, us_average)
    """
    raw_df = pd.read_csv(file_path, skiprows=2, thousands=',', nrows=52)
    df = pd.read_csv(file_path, skiprows=2, thousands=',', nrows=52)
    df['Health Spending per Capita'] = (df['Health Spending per Capita']
                                        .str.replace('$', '', regex=False)
                                        .str.replace(',', '', regex=False)
                                        .astype(float))

    # Separate state data from US average
    state_data = df[df['Location'] != 'United States'].copy()
    us_average = df[df['Location'] == 'United States']['Health Spending per Capita'].values[0]

    # Add region mapping
    state_data['Region'] = state_data['Location'].apply(
        lambda x: next((region for region, states in regions.items() if x in states), 'Other')
    )

    
    print(us_average)
    print(type(us_average))
    return df, state_data, us_average, raw_df