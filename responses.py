from random import choice
# Sample data as a corpus
import csv

# Read data from CSV file
data = []
with open('./philosophy_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({"school": row["school"], "sentence_str": row["sentence_str"]})

def get_philos_response(menu_item):
    response_data = choice(data)
    response = "According to {}, {}".format(response_data["school"], response_data["sentence_str"])
    return response

# Example usage
sample_item = "Meaning of Philosophy"
print(get_philos_response(sample_item))
