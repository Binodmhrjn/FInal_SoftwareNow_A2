# ## Option 1 - BOTH OPTIONS ARE OK

# import pandas as pd
# import glob
# import os

# # Specifying  folder path containing the CSV files
# csv_folder = '/Users/binodmaharjan/Downloads/Assignment 2 actual csvs/CSVS'  

# # Using glob to find all CSV files in the folder
# csv_files = glob.glob(os.path.join(csv_folder, '*.csv'))

# # Defining the path to save the combined text file
# output_file_path = '/Users/binodmaharjan/Downloads/Assignment 2 actual csvs/output text2/combined_text.txt'  # Replace with the output file path

# # List to hold all the extracted text
# all_text = []

# # Loop through each CSV and extract the text
# for file_path in csv_files:
#     # Read the CSV file
#     df = pd.read_csv(file_path)
    
#     # Find the column that contains 'text' in the name (case-insensitive)
#     text_column = [col for col in df.columns if 'text' in col.lower()]
    
#     if text_column:
#         # Extract the text from the found column and append it to the list
#         all_text.append(" ".join(df[text_column[0]].astype(str)))

# # Combine all the text into a single string
# combined_text = "\n".join(all_text)

# # Write the combined text to a .txt file (ensure file name is present)
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     output_file.write(combined_text)

# print(f"Text has been successfully written to {output_file_path}")

# Option 2
import pandas as pd

# List of CSV file paths
csv_files = [
    './CSVS/CSV1.csv',  # CSV1 with 'SHORT TEXT' column
    './CSVS/CSV2.csv',  # CSV2 with 'text' column
    './CSVS/CSV2.csv',  # CSV3 with 'text' column
    './CSVS/CSV2.csv'   # CSV4 with 'text' column
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

