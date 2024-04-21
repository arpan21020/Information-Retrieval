import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import difflib

# Load CSV file into DataFrame
df = pd.read_csv('government_schemes.csv')

# Extract policy names from DataFrame
policy_names = df['Policy name'].tolist()

# Get user input (replace this with your actual user input method)
user_input = input("Enter user's input related to policy: ")

# Preprocess user input
user_input = user_input.lower()  # Convert to lowercase
user_input = ''.join(c for c in user_input if c.isalnum() or c.isspace())  # Remove punctuation

# Tokenize user input into words
user_words = user_input.split()

# Find the closest matching policy name using fuzzy matching
closest_match = difflib.get_close_matches(user_input, policy_names, n=1, cutoff=0.1)

if closest_match:
    extracted_policy_name = closest_match[0]
    print(f"Extracted Policy Name: {extracted_policy_name}")
else:
    print(closest_match[0])
    print("No matching policy name found.")
