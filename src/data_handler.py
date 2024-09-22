import pandas as pd

def load_data(file_path):
    """Load the dataset."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def check_missing_values(data):
    """Check for missing values in the dataset."""
    missing_data = data.isnull().sum()
    print(f"Missing values:\n{missing_data}")
    return missing_data
def null_percentage(data):
        """Returns a Series with the percentage of null values per column."""
        null_counts = data.isnull().sum()
        total_rows = len(data)
        null_percentage = (null_counts / total_rows) * 100
        return null_percentage
def handle_null_values(data):
        """Impute null values based on percentage of missing data."""
        total_rows = len(data)
        for col in data.columns:
            null_percentage = (data[col].isnull().sum() / total_rows) * 100
            
            if null_percentage > 0 and null_percentage <= 30:
                # Option 1: Impute with mean/median for numeric, mode for categorical
                if pd.api.types.is_numeric_dtype(data[col]):
                    data[col].fillna(data[col].mean(), inplace=True)  # Mean for numeric
                else:
                    data[col].fillna(data[col].mode()[0], inplace=True)  # Mode for categorical
            elif 30 < null_percentage <= 90:
                # Option 1: Impute with median for numeric, mode for categorical
                if pd.api.types.is_numeric_dtype(data[col]):
                    data[col].fillna(data[col].median(), inplace=True)  # Median for numeric
                else:
                    data[col].fillna(data[col].mode()[0], inplace=True)  # Mode for categorical
            elif null_percentage > 90:
                # Option 1: Drop the column if too many nulls
                data.drop(columns=[col], inplace=True)
    
def check_data_types(df):
    """Check the data types of columns."""
    print(f"Data Types:\n{df.dtypes}")
    return df.dtypes
import pandas as pd

def identify_column_types(df):
    """
    Function to identify numerical and categorical columns in a DataFrame.
    
    Args:
    df: pandas DataFrame
    
    Returns:
    numerical_columns: List of numerical column names
    categorical_columns: List of categorical column names
    """
    # Select numerical columns
    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    # Select categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    print(f"Numerical Columns: {numerical_columns}")
    print(f"Categorical Columns: {categorical_columns}")
    
    return numerical_columns, categorical_columns

