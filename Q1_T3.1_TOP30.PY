
import re
from collections import Counter
import csv

# Define the path to your .txt file
txt_file_path = './Combined_text.txt'

# Define the path to save the CSV file
csv_output_path = './top_30_words.csv'

# Read the content of the text file
with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Clean and preprocess the text
# Convert to lowercase, remove punctuation and special characters, and split by spaces
# Only keep words with 2 or more letters (and exclude numbers)
words = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())

# Count the occurrences of each word
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Display the top 30 words with their counts (optional)
for word, count in top_30_words:
    print(f"{word}: {count}")

# Save the top 30 words and their counts to a CSV file
with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['Word', 'Count'])
    # Write the top 30 words and their counts
    writer.writerows(top_30_words)

print(f"Top 30 words have been successfully written to {csv_output_path}")
