# Import pandas module for data manipulation
import pandas as pd
import os

# Define dimensions to be used in parallel coordinates plot
dims = ['Percentage of aerial duel won', 'Ball Recoveries', 'Dribbles Tackled', 'Interceptions',
        'Minutes per game', 'Passes completed']

# Get the current working directory
current_dir = os.getcwd()

# Specify the relative path to the data file
data_path = os.path.join(current_dir, "df.csv")

# Load data from CSV file
df = pd.read_csv(data_path)

# Convert the 'Contract Expiration Date' column to datetime format
df['Contract Expiration Date'] = pd.to_datetime(df['Contract Expiration Date'])

# Create a new column 'Contract Expiration Year' extracted from the 'Contract Expiration Date' column
df['Contract Expiration Year'] = df['Contract Expiration Date'].dt.year

df['Market Value'] = df['Market Value'].str.replace(',', '')
df['Market Value'] = pd.to_numeric(df['Market Value'])
