import pandas as pd

# Load the CSV file into a pandas DataFrame
data = pd.read_csv('philosophy_data.csv')

# Preprocess the data
data['sentence_lowered'] = data['sentence_lowered'].apply(preprocess)  # Preprocess function from user_functions.py

# Now, you have a DataFrame 'data' with preprocessed sentences and other information
