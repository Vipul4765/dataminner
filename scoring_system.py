# main.py
from positive_negative import dict_pos_neg
import pandas as pd
import nltk
import os
import re

# Download stopwords data
nltk.download('punkt')

positive_dict = dict_pos_neg['Positive_Words']
negative_dict = dict_pos_neg['Negative_Words']

# Assuming stop_words_set is a predefined set of stop words
stop_words_set = set(nltk.corpus.stopwords.words('english'))

# Define a regex pattern for personal pronouns
personal_pronouns_pattern = re.compile(r'\b(?:I|we|my|ours|us)\b', flags=re.IGNORECASE)

def list_files_in_folder(folder_path):
    files_list = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            files_list.append(file_path)
    return files_list

def file_open_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the data from the file
        data_read = file.read()
    return data_read

def calculate_derived_variables(text):
    # Tokenize the text using nltk
    tokens = nltk.word_tokenize(text)

    # Clean text by removing stop words and punctuation
    cleaned_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words_set]

    # Initialize scores and variables
    positive_score = 0
    negative_score = 0
    total_words = len(cleaned_tokens)
    total_sentences = nltk.sent_tokenize(text)
    total_sentences_count = len(total_sentences)
    total_complex_words_count = 0
    total_syllables_count = 0
    personal_pronouns_count = 0

    # Calculate Positive and Negative Scores
    for token in cleaned_tokens:
        if token in positive_dict:
            positive_score += 1
        elif token in negative_dict:
            negative_score += 1

        # Calculate syllables count for each word
        syllables = sum([1 for char in token if char.lower() in 'aeiou'])
        total_syllables_count += max(1, syllables)  # Handle words with no vowels

        # Count complex words
        if syllables > 2:
            total_complex_words_count += 1

        # Count personal pronouns
        if personal_pronouns_pattern.match(token):
            personal_pronouns_count += 1

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

    # Calculate Subjectivity Score
    subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)

    # Calculate Readability Scores
    average_sentence_length = total_words / total_sentences_count
    percentage_complex_words = total_complex_words_count / total_words
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    average_words_per_sentence = total_words / total_sentences_count

    # Calculate Average Word Length
    average_word_length = sum(len(word) for word in cleaned_tokens) / total_words

    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Average Sentence Length': average_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Average Number of Words Per Sentence': average_words_per_sentence,
        'Complex Word Count': total_complex_words_count,
        'Word Count': total_words,
        'Syllable Per Word': total_syllables_count / total_words,
        'Personal Pronouns': personal_pronouns_count,
        'Average Word Length': average_word_length,
    }


# ...

result_df = pd.DataFrame(columns=['Positive Score', 'Negative Score', 'Polarity Score', 'Subjectivity Score',
                                  'Average Sentence Length', 'Percentage of Complex Words', 'Fog Index',
                                  'Average Number of Words Per Sentence', 'Complex Word Count', 'Word Count',
                                  'Syllable Per Word', 'Personal Pronouns', 'Average Word Length'])

data = list_files_in_folder(r'C:\Users\DELL\PycharmProjects\dataminner\clean_txt')

for file_open_dta in data:
    res = file_open_data(file_open_dta)
    result = calculate_derived_variables(res)

    # Convert result to DataFrame and append
    result_df = pd.concat([result_df, pd.DataFrame(result, index=[0])], ignore_index=True)

# Save the DataFrame to a CSV file
result_df.to_csv('result.csv', index=False)

