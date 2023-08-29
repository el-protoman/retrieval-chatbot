from random import choice
import csv

# Read data from CSV file
data = []
with open('./philosophy_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            "school": row["school"],
            "sentence_str": row["sentence_str"],
            "tokenized_txt": row["tokenized_txt"]  # Add this line
        })

def get_philos_response(menu_item):
    # Modify this function to return the same response for the same input
    hash_value = hash(menu_item) % len(data)
    response_data = data[hash_value]
    response = "According to {}, {}".format(response_data["school"], response_data["sentence_str"])
    return response



# Example usage
sample_item = "Meaning of Life"
print(get_philos_response(sample_item))
blank_spot = "philosopher"  # Add your chosen blank_spot value here
