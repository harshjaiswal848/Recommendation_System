import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import os

# Set plot style for better visuals
plt.style.use('seaborn-v0_8')

# 1. Data Loading
def load_data(file_path):
    """Load dataset and return DataFrame."""
    try:
        df = pd.read_csv(file_path, encoding='latin1', sep=',', on_bad_lines='skip')  # Specify delimiter and skip bad lines
        print(f"Dataset loaded successfully with shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File 'movielens_ratings.csv' not found. Ensure it is in the project root.")
        return None
    except pd.errors.ParserError:
        print("Error: Failed to parse CSV. Check file format or delimiters.")
        return None
    except PermissionError:
        print("Error: Permission denied for 'movielens_ratings.csv'. Ensure the file is not open elsewhere and you have read permissions.")
        return None

# 2. Data Cleaning
def clean_data(df):
    """Handle missing values, remove duplicates, and handle outliers."""
    # Check for missing values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    # Drop rows with missing critical columns (e.g., userId, movieId, rating)
    critical_columns = ['userId', 'movieId', 'rating']
    df = df.dropna(subset=critical_columns)
    
    # Detect and filter outliers in ratings (expected range: 1–5)
    outliers = df[~df['rating'].between(1, 5)]
    print(f"Outliers in rating (outside 1–5): {len(outliers)} rows")
    df = df[df['rating'].between(1, 5)]  # Filter outliers
    
    # Fill missing non-critical columns with appropriate values (e.g., mean for numerical)
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].mean())  # Use direct assignment instead of inplace=True
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    print(f"Shape after cleaning: {df.shape}")
    return df

# 3. Feature Selection
def select_features(df):
    """Select relevant features for recommendation system."""
    # Select core features: userId, movieId, rating
    selected_columns = ['userId', 'movieId', 'rating']
    
    # Include additional features if available (e.g., timestamp)
    if 'timestamp' in df.columns:
        selected_columns.append('timestamp')
    
    df_selected = df[selected_columns]
    print("\nSelected features:", df_selected.columns.tolist())
    return df_selected

# 4. Data Transformation
def transform_data(df):
    """Transform data (e.g., normalize ratings, convert timestamps)."""
    # Normalize ratings
    scaler = StandardScaler()
    df['rating_normalized'] = scaler.fit_transform(df[['rating']])
    
    # Convert timestamp to datetime if available
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    print("\nData after transformation:")
    print(df.head())
    return df

# 5. Exploratory Data Analysis
def perform_eda(df, output_dir='plots'):
    """Perform EDA and save visualizations."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Distribution of ratings
    plt.figure(figsize=(8, 6))
    sns.histplot(df['rating'], bins=20, kde=True)
    plt.title('Distribution of Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'rating_distribution.png'))
    plt.close()
    
    # Number of ratings per user
    user_ratings = df.groupby('userId').size()
    plt.figure(figsize=(8, 6))
    sns.histplot(user_ratings, bins=30, kde=True)
    plt.title('Number of Ratings per User')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'ratings_per_user.png'))
    plt.close()
    
    # Number of ratings per movie
    movie_ratings = df.groupby('movieId').size()
    plt.figure(figsize=(8, 6))
    sns.histplot(movie_ratings, bins=30, kde=True)
    plt.title('Number of Ratings per Movie')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'ratings_per_movie.png'))
    plt.close()
    
    print(f"EDA plots saved in {output_dir}/")

# Main function to run the pipeline
def main():
    # File path to dataset (relative to project root)
    file_path = 'movielens_ratings.csv'  # Ensure this file is in the project root
    
    # Load data
    df = load_data(file_path)
    if df is None:
        return
    
    # Clean data
    df = clean_data(df)
    
    # Select features
    df = select_features(df)
    
    # Transform data
    df = transform_data(df)
    
    # Perform EDA
    perform_eda(df)

if __name__ == "__main__":
    main()