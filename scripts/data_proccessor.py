import pandas as pd

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the DataProcessor with a DataFrame.
        
        Parameters:
        data (pd.DataFrame): The input DataFrame to be processed.
        """
        self.data = data
    def missing_data_summary(self) -> pd.DataFrame:
        """
        Returns a summary of columns with missing data, including count and percentage of missing values.

        Returns:
            pd.DataFrame: A DataFrame with columns 'Missing Count' and 'Percentage (%)' for columns with missing values.
        """
        # Total missing values per column
        missing_data = self.data.isnull().sum()
        
        # Filter only columns with missing values greater than 0
        missing_data = missing_data[missing_data > 0]
        
        # Calculate the percentage of missing data
        missing_percentage = (missing_data / len(self.data)) * 100
        
        # Combine the counts and percentages into a DataFrame
        missing_df = pd.DataFrame({
            'Missing Count': missing_data, 
            'Percentage (%)': missing_percentage
        })
        
        # Sort by percentage of missing data
        missing_df = missing_df.sort_values(by='Percentage (%)', ascending=False)
        
        return missing_df

    def handle_missing_data(self, strategy: str = 'mean', columns: list = None) -> None:
        """
        Handles missing data based on a specified strategy for specified columns,
        categorizing columns as numerical or non-numerical and handling accordingly.

        Parameters:
        strategy (str): The strategy to handle missing data - 'mean', 'median', 'mode', or 'drop'.
        columns (list): List of columns to apply the strategy on. If None, applies to all columns.
        """
        if columns is None:
            columns = self.data.columns

        # Identify columns with missing values
        missing_columns = [col for col in columns if self.data[col].isnull().sum() > 0]

        # Separate columns into numerical and non-numerical types
        numerical_cols = [col for col in missing_columns if self.data[col].dtype in ['int64', 'float64']]
        non_numerical_cols = [col for col in missing_columns if self.data[col].dtype not in ['int64', 'float64']]

        # Handle missing data for numerical columns
        for column in numerical_cols:
            if strategy == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
            elif strategy == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif strategy == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            elif strategy == 'drop':
                self.data.dropna(subset=[column], inplace=True)
            else:
                raise ValueError(f"Unsupported strategy '{strategy}' for numerical column '{column}'.")

        # Handle missing data for non-numerical columns
        for column in non_numerical_cols:
            if strategy == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            elif strategy == 'drop':
                self.data.dropna(subset=[column], inplace=True)
            else:
                print(f"Warning: Strategy '{strategy}' is not applicable for non-numerical column '{column}'. Defaulting to 'mode'.")
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)

       
    def get_processed_data(self) -> pd.DataFrame:
        """
        Returns the processed DataFrame.
        
        Returns:
        pd.DataFrame: Processed DataFrame.
        """
        return self.data
