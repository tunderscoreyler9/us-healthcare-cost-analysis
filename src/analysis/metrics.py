import pandas as pd
import numpy as np
from scipy import stats

def calculate_metrics(state_data, us_average):
    """
    Calculate comprehensive regional metrics including statistical tests
    and add a row for the national overview.
    
    Parameters:
    - state_data (pd.DataFrame): DataFrame with state-level healthcare spending data.
    - us_average (float): The U.S. national average for healthcare spending per capita.
    
    Returns:
    - pd.DataFrame: DataFrame with regional and national metrics.
    """
    regional_metrics = {}

    for region in state_data['Region'].unique():
        region_data = state_data[state_data['Region'] == region]['Health Spending per Capita']

        # Basic statistics for the region
        metrics = {
            'mean': region_data.mean(),
            'median': region_data.median(),
            'std': region_data.std(),
            'cv': region_data.std() / region_data.mean(),  # Coefficient of variation
            'skew': stats.skew(region_data),
            'kurtosis': stats.kurtosis(region_data),
            'n_states': len(region_data),
            'pct_above_us_avg': (region_data > us_average).mean() * 100
        }

        # One-sample t-test against U.S. average
        t_stat, p_val = stats.ttest_1samp(region_data, us_average)
        metrics['t_stat'] = t_stat
        metrics['p_value'] = p_val

        # Store metrics for the region
        regional_metrics[region] = metrics

    # Add a row for the national overview
    national_metrics = {
        'mean': state_data['Health Spending per Capita'].mean(),
        'median': state_data['Health Spending per Capita'].median(),
        'std': state_data['Health Spending per Capita'].std(),
        'cv': state_data['Health Spending per Capita'].std() / state_data['Health Spending per Capita'].mean(),
        'skew': stats.skew(state_data['Health Spending per Capita']),
        'kurtosis': stats.kurtosis(state_data['Health Spending per Capita']),
        'n_states': len(state_data),
        'pct_above_us_avg': (state_data['Health Spending per Capita'] > us_average).mean() * 100,
        't_stat': None,  # Not applicable for the national average
        'p_value': None  # Not applicable for the national average
    }

    # Add national metrics to the DataFrame
    regional_metrics['National'] = national_metrics

    return pd.DataFrame(regional_metrics).T