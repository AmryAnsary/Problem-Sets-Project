import pandas as pd
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load AHTN data for 2017 and 2022 (Data in CSV format)
ahtn_2017 = pd.read_csv(r'C:\Users\user\Downloads\AHTN_2017.csv', encoding='ISO-8859-1')
ahtn_2022 = pd.read_csv(r'C:\Users\user\Downloads\AHTN_2022.csv', encoding='ISO-8859-1')

# Function to calculate Levenshtein Distance
def levenshtein_similarity(s1, s2):
    # Ensure both inputs are strings and handle None or NaN values
    s1 = str(s1) if s1 is not None else ""
    s2 = str(s2) if s2 is not None else ""
    return SequenceMatcher(None, s1, s2).ratio()

# Function to find top 3 closest matches using Levenshtein and Cosine Similarity
def find_closest_ahtn_2017(ahtn_2022_code, ahtn_2022_desc, top_n=3):
    results = []
    for _, row in ahtn_2017.iterrows():
        ahtn_2017_code = str(row['Code']) if row['Code'] is not None else ""  # CSV column name
        ahtn_2017_desc = str(row['Description']) if row['Description'] is not None else ""  # CSV column name

        # Calculate Levenshtein similarity
        lev_similarity = levenshtein_similarity(ahtn_2022_code, ahtn_2017_code)

        # Calculate Cosine similarity based on descriptions
        vectorizer = TfidfVectorizer().fit_transform([ahtn_2022_desc, ahtn_2017_desc])
        cos_similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

        # Average the two similarity measures
        avg_similarity = (lev_similarity + cos_similarity) / 2
        results.append((ahtn_2017_code, ahtn_2017_desc, avg_similarity))
    
    # Sort results by similarity and return top N
    results.sort(key=lambda x: x[2], reverse=True)
    return results[:top_n]

# Example Usage
ahtn_2022_code = "85.02"  # Example AHTN 2022 code
ahtn_2022_desc = "Electric Generating Sets And Rotary Converters."

closest_matches = find_closest_ahtn_2017(ahtn_2022_code, ahtn_2022_desc)
for match in closest_matches:
    print(f"2017 Code: {match[0]}, Description: {match[1]}, Similarity: {match[2]}")