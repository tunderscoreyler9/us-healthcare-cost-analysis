import matplotlib.pyplot as plt
import seaborn as sns

def plot_state_comparison(df, metric, title, figsize=(15, 6)):
    """Create bar plot comparing states for a given metric"""
    plt.figure(figsize=figsize)
    sns.barplot(data=df.sort_values(metric, ascending=False),
                x='State', 
                y=metric)
    plt.xticks(rotation=45, ha='right')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df, columns, title):
    """Create correlation matrix heatmap"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[columns].corr(), annot=True, cmap='coolwarm')
    plt.title(title)
    plt.tight_layout()
    plt.show()
