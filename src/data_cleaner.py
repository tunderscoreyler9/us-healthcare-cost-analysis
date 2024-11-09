def clean_state_names(df, state_column='State'):
    """Standardize state names across datasets"""
    # Add state name standardization logic
    return df

def clean_currency_columns(df, currency_columns):
    """Clean currency columns by removing $ and , and converting to float"""
    for col in currency_columns:
        df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
    return df
