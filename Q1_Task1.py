
import pandas as pd

# List of CSV file paths
csv_files = [
    './CSV1.csv',  # CSV1 with 'SHORT TEXT' column
    './CSV2.csv',  # CSV2 with 'text' column
    './CSV2.csv',  # CSV3 with 'text' column
    './CSV2.csv'   # CSV4 with 'text' column
]

# Define the path to save the combined text file
output_file_path = './Combined_text.txt'

# List to hold all the extracted text
all_text = []

# Loop through each CSV and extract the text
for file_path in csv_files:
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Find the column that contains 'text' in the name (case-insensitive)
    text_column = [col for col in df.columns if 'text' in col.lower()]
    
    if text_column:
        # Extract the text from the found column and append it to the list
        all_text.append(" ".join(df[text_column[0]].astype(str)))

# Combine all the text into a single string
combined_text = "\n".join(all_text)

# Write the combined text to a .txt file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combined_text)

print(f"Text successfully written to {output_file_path}")

