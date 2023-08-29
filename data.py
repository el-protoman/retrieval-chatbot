import pandas as pd

# Read the CSV file
df = pd.read_csv('./philosophy_data.csv')

# Get the unique authors, schools, and titles
unique_authors = df['author'].unique()
unique_schools = df['school'].unique()
unique_titles = df['title'].unique()

# Count the number of unique authors, schools, and titles
num_authors = len(unique_authors)
num_schools = len(unique_schools)
num_titles = len(unique_titles)

print("Unique authors:", unique_authors)
print("Number of unique authors:", num_authors)
print("Unique schools:", unique_schools)
print("Number of unique schools:", num_schools)
print("Unique titles:", unique_titles)
print("Number of unique titles:", num_titles)
