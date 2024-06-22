import os
import pandas as pd
import textstat
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the root directory and the subdirectories with the corresponding human readability levels
root_dir = "Texts-SeparatedByReadingLevel"
directories = {
    "Int-Txt": "Intermediate",
    "Ele-Txt": "Elementary",
    "Adv-Txt": "Advanced"
}

# List to store the readability scores
readability_data = []

# Function to get readability scores for a given text
def get_readability_scores(text):
    try:
        scores = {
            "Flesch Reading Ease": textstat.flesch_reading_ease(text),
            "SMOG Index": textstat.smog_index(text),
            "Flesch-Kincaid Grade": textstat.flesch_kincaid_grade(text),
            "Coleman-Liau Index": textstat.coleman_liau_index(text),
            "Automated Readability Index": textstat.automated_readability_index(text),
            "Dale-Chall Readability Score": textstat.dale_chall_readability_score(text),
            "Difficult Words": textstat.difficult_words(text),
            "Linsear Write Formula": textstat.linsear_write_formula(text),
            "Gunning Fog Index": textstat.gunning_fog(text),
            "Text Standard": textstat.text_standard(text)
        }
    except Exception as e:
        logging.error(f"Error calculating readability scores: {e}")
        scores = {
            "Flesch Reading Ease": None,
            "SMOG Index": None,
            "Flesch-Kincaid Grade": None,
            "Coleman-Liau Index": None,
            "Automated Readability Index": None,
            "Dale-Chall Readability Score": None,
            "Difficult Words": None,
            "Linsear Write Formula": None,
            "Gunning Fog Index": None,
            "Text Standard": None
        }
    return scores

# Iterate through the directories
for dir_name, readability_level in directories.items():
    dir_path = os.path.join(root_dir, dir_name)
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(dir_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    scores = get_readability_scores(text)
                    scores["Filename"] = filename
                    scores["Human Evaluation"] = readability_level
                    readability_data.append(scores)
                    logging.info(f"Processed file: {filename} in {readability_level} level")
            except Exception as e:
                logging.error(f"Error reading file {filename}: {e}")

# Create a DataFrame from the collected data
df = pd.DataFrame(readability_data)

# Export the DataFrame to an Excel file
output_file = "readability_assessments.xlsx"
df.to_excel(output_file, index=False)

logging.info(f"Readability assessments exported to {output_file}")
