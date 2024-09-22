import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def summary_statistics(df):
    """Generate descriptive statistics of numerical columns."""
    print("Descriptive Statistics:\n")
    stats = df.describe()
    print(stats)
    return stats

def univariate_analysis(df, numerical_columns, categorical_columns):
    """Perform univariate analysis on numerical and categorical columns."""
    print("Univariate Analysis: Numerical Columns")
    for col in numerical_columns:
        df[col].hist(bins=30)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()

    print("Univariate Analysis: Categorical Columns")
    for col in categorical_columns:
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.show()

def bivariate_analysis(df, target_col):
    """Explore relationships between numerical features and the target variable."""
    print(f"Bivariate Analysis: Relationship with {target_col}")
    sns.pairplot(df, x_vars=df.columns, y_vars=[target_col])
    plt.show()

def correlation_matrix(df):
    """Generate and plot a correlation matrix."""
    print("Correlation Matrix:\n")
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    return corr
