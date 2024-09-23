from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text_file, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")

    # Read the text file with error handling for encoding issues
    with open(text_file, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
        print("File content preview:\n", text[:500])  # Print first 500 characters to ensure the file is read correctly

    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    print("First 50 tokens:", tokens[:50])  # Print the first 50 tokens to check tokenization

    # Count the occurrences of each token
    token_counts = Counter(tokens)
    print("Token counts:", token_counts)  # Print token counts

    # Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)
    print("Top tokens:", top_tokens)  # Print top tokens

    return top_tokens

# Example usage:
text_file = './Combined_text.txt'

top_30_tokens = count_unique_tokens(text_file, top_n=30)

for token, count in top_30_tokens:
    print(f"Token: {token}, Count: {count}")
