from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

def extract_entities_biobert(text):
    # Load the BioBERT model and tokenizer
    model_name = "dmis-lab/biobert-base-cased-v1.1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Create an NER pipeline with proper configuration
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    # Set maximum length for BioBERT
    max_length = 512

    # Split text into chunks to avoid truncation errors
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]

    diseases = []
    drugs = []

    # Process each chunk separately
    for chunk in chunks:
        # Apply the pipeline to the chunk
        entities = ner_pipeline(chunk)

        # Filter and collect entities related to diseases and drugs
        for entity in entities:
            # Debug: Print all entities to understand the structure
            print(f"Entity: {entity}")

            # Check if the entity is a disease or drug based on entity group
            entity_group = entity['entity_group'].lower()
            if 'disease' in entity_group:
                diseases.append(entity['word'])
            elif 'drug' in entity_group:
                drugs.append(entity['word'])

    # Deduplicate and return results
    return list(set(diseases)), list(set(drugs))

# Define the path to your input text file
text_file = './Combined_text.txt'  # Ensure this path is correct

# Read the text from the file
with open(text_file, 'r', encoding='utf-8', errors='ignore') as file:
    text = file.read()

# Use BioBERT to extract diseases and drugs
diseases_biobert, drugs_biobert = extract_entities_biobert(text)

# Print the results
print(f"Diseases (BioBERT): {diseases_biobert}")
print(f"Drugs (BioBERT): {drugs_biobert}")


