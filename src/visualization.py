import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column):
    """Plot a histogram for a given column."""
    df[column].hist(bins=30)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_bar(df, column):
    """Plot a bar chart for a given categorical column."""
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_correlation_matrix(df):
    """Plot a correlation matrix for the dataframe."""
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
