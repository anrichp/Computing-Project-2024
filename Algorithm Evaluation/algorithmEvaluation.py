import os
import pandas as pd
import textstat
import logging
import seaborn as sns
import matplotlib.pyplot as plt

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
            "Linsear Write Formula": textstat.linsear_write_formula(text),
            "Gunning Fog Index": textstat.gunning_fog(text)
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
            "Linsear Write Formula": None,
            "Gunning Fog Index": None
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

# Convert human evaluations to numeric scores
df['Human Evaluation Numeric'] = df['Human Evaluation'].map({
    'Elementary': 1,
    'Intermediate': 2,
    'Advanced': 3
})

# Calculate Pearson correlation
numeric_columns = [
    "Flesch Reading Ease",
    "SMOG Index",
    "Flesch-Kincaid Grade",
    "Coleman-Liau Index",
    "Automated Readability Index",
    "Dale-Chall Readability Score",
    "Linsear Write Formula",
    "Gunning Fog Index",
    "Human Evaluation Numeric"
]
correlation_matrix = df[numeric_columns].corr(method='pearson')

# Print the correlation matrix
print(correlation_matrix)

# If you want to specifically see the correlation of readability scores with human evaluations
print(correlation_matrix['Human Evaluation Numeric'])

# Export the DataFrame and correlation matrix to an Excel file
with pd.ExcelWriter("readability_assessments_with_correlation.xlsx") as writer:
    df.to_excel(writer, sheet_name='Readability Scores', index=False)
    correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

logging.info(f"Readability assessments and correlation matrix exported to readability_assessments_with_correlation.xlsx")

# Visualize the Pearson correlation matrix using seaborn
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Pearson Correlation Matrix of Readability Scores')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

# Save the heatmap to a file
heatmap_fig = heatmap.get_figure()
heatmap_fig.savefig("pearson_correlation_heatmap.png")

logging.info("Pearson correlation heatmap saved to pearson_correlation_heatmap.png")
plt.show()
