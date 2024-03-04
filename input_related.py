import pandas as pd

# Read the CSV file
frame = pd.read_csv('input.csv')

# Display the first few rows of the DataFrame
url_ist = list(frame['URL'])
url_id = list(frame['URL_ID'])
print(url_id[0])