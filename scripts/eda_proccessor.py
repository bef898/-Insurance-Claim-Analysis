import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class EDA:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the EDA class with a DataFrame.
        
        Parameters:
        data (pd.DataFrame): The input DataFrame for analysis.
        """
        self.data = data

    # Data Summarization
    def data_summarization(self):
        """
        Summarizes the data by providing descriptive statistics for numerical columns 
        and data type review for all columns.
        """
        print("Descriptive Statistics:\n")
        print(self.data.describe())
        print("\nData Types:\n")
        print(self.data.dtypes)

    # Data Quality Assessment
    def check_missing_values(self):
        """
        Prints a summary of missing values in the DataFrame.
        """
        missing_summary = self.data.isnull().sum()
        print("\nMissing Values Summary:")
        print(missing_summary[missing_summary > 0])

    # Univariate Analysis
    def plot_histograms(self, numerical_columns: list):
        """
        Plots histograms for specified numerical columns.

        Parameters:
        numerical_columns (list): List of numerical columns to plot histograms for.
        """
        for column in numerical_columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(self.data[column], kde=True, bins=20)
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()

    def plot_bar_charts(self, categorical_columns: list):
        """
        Plots bar charts for specified categorical columns.

        Parameters:
        categorical_columns (list): List of categorical columns to plot bar charts for.
        """
        for column in categorical_columns:
            plt.figure(figsize=(10, 8))
            self.data[column].value_counts().plot(kind='bar')
            plt.title(f'Bar Chart of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.show()

    # Bivariate or Multivariate Analysis
    def plot_correlation_matrix(self):
        """
        Plots a heatmap showing the correlation matrix of numerical columns in the DataFrame.
        """
        plt.figure(figsize=(10, 8))
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()

    def scatter_plot(self, x_column: str, y_column: str, hue_column: str = None):
        """
        Plots a scatter plot between two specified columns.

        Parameters:
        x_column (str): The column for the x-axis.
        y_column (str): The column for the y-axis.
        hue_column (str): Optional column to color points by category.
        """
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.data[x_column], y=self.data[y_column], hue=self.data[hue_column] if hue_column else None)
        plt.title(f'Scatter Plot: {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()

    # Data Comparison (Trends Over Geography)
    def plot_trend_over_geography(self, groupby_column: str, target_column: str):
        """
        Plots a comparison of the target column based on geographical or categorical grouping.

        Parameters:
        groupby_column (str): The column to group by (e.g., geography).
        target_column (str): The target numerical column to compare.
        """
        grouped_data = self.data.groupby(groupby_column)[target_column].mean().sort_values()
        grouped_data.plot(kind='bar', figsize=(10, 6), title=f'{target_column} by {groupby_column}')
        plt.xlabel(groupby_column)
        plt.ylabel(target_column)
        plt.show()

    # Outlier Detection
    def plot_boxplots(self, numerical_columns: list):
        """
        Plots boxplots for specified numerical columns to detect outliers.

        Parameters:
        numerical_columns (list): List of numerical columns to plot boxplots for.
        """
        for column in numerical_columns:
            plt.figure(figsize=(8, 5))
            sns.boxplot(data=self.data[column])
            plt.title(f'Boxplot of {column}')
            plt.xlabel(column)
            plt.show()

    # Creative Visualizations
    def create_visualizations(self):
        """
        Produces three creative and insightful plots based on the EDA.
        """
        # Example Visualization 1: Distribution of TotalPremium
        if 'TotalPremium' in self.data.columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(self.data['TotalPremium'], kde=True, bins=30, color='purple')
            plt.title('Distribution of Total Premium')
            plt.xlabel('Total Premium')
            plt.ylabel('Frequency')
            plt.show()

        # Example Visualization 2: Monthly trends of TotalClaims if 'Month' column exists
        if 'Month' in self.data.columns and 'TotalClaims' in self.data.columns:
            monthly_trends = self.data.groupby('Month')['TotalClaims'].mean()
            monthly_trends.plot(kind='line', marker='o', figsize=(10, 6), color='green')
            plt.title('Average Total Claims Per Month')
            plt.xlabel('Month')
            plt.ylabel('Average Total Claims')
            plt.grid()
            plt.show()

        # Example Visualization 3: Correlation heatmap
        self.plot_correlation_matrix()
