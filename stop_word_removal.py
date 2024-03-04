import os
def stop_words_extracting(stopwords_file_path):  # Replace with the actual path to your stop words file  # Replace with the actual path to your stop words file

  with open(stopwords_file_path, 'r', encoding='utf-8', errors='replace') as stopwords_file:
      stop_words = set(stopwords_file.read().split())
  return stop_words


def list_files_in_folder(folder_path):
    files_list = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            files_list.append(file_path)
    return files_list

# Example usage:
files_in_folder = [r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_Auditor.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_Currencies.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_DatesandNumbers.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_Generic.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_GenericLong.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_Geographic.txt",
                   r"C:\Users\DELL\PycharmProjects\dataminner\StopWords\StopWords_Names.txt"]


def remove_stop_words(file_path, stop_words):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text (you might want to customize this based on your specific requirements)
    words = text.split()

    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the remaining words to reconstruct the text
    processed_text = ' '.join(filtered_words)

    # Create a new folder if it doesn't exist
    output_folder = r'C:\Users\DELL\PycharmProjects\dataminner\clean_txt'  # Replace with the desired path for the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the processed text to a new file in the output folder
    output_file_path = os.path.join(output_folder, os.path.basename(file_path))
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(processed_text)



all_stop_words = []
for file_path in files_in_folder:
  response = stop_words_extracting(file_path)
  all_stop_words.append(response)

combined_set = set().union(*all_stop_words)
# Example usage:
stop_words_set = combined_set  # Replace with your set of stop words
folder_path = r"C:\Users\DELL\PycharmProjects\dataminner\text_output_file"  # Replace with the actual path to your folder
all_file_paths = list_files_in_folder(folder_path)
# Replace with the actual path to your text file
for file_ in all_file_paths:

    remove_stop_words(file_, stop_words_set)
