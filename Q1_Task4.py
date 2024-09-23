from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

def extract_entities_biobert(text):
    # Load the BioBERT model and tokenizer
    model_name = "dmis-lab/biobert-base-cased-v1.1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Create an NER pipeline
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)
    
    # Apply the pipeline to the text
    entities = ner_pipeline(text)
    
    diseases = []
    drugs = []

    # Filter and collect entities related to diseases and drugs
    for entity in entities:
        if 'disease' in entity['entity'].lower():
            diseases.append(entity['word'])
        elif 'drug' in entity['entity'].lower():
            drugs.append(entity['word'])
    
    return diseases, drugs

# Define the path to your input text file
text_file = './Combined_text.txt'

# Read the text from the file
with open(text_file, 'r', encoding='utf-8', errors='ignore') as file:
    text = file.read()

# Use BioBERT to extract diseases and drugs
diseases_biobert, drugs_biobert = extract_entities_biobert(text)

# Print the results
print(f"Diseases (BioBERT): {diseases_biobert}")
print(f"Drugs (BioBERT): {drugs_biobert}")
