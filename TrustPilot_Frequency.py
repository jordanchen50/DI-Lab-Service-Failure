import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from collections import Counter

import matplotlib.pyplot as plt

# Load CVS file, select a column and turn every row of that column into list.
def load_file(path, col):
    file_path = path
    file_df = pd.read_csv(file_path, usecols=[col])
    list_data = file_df[col].to_list()
    return list_data

# Tokenize all the words in the selected column.
def tokenize_csv_column(create_list):
    list_after_tokenize = []
    for i in range(len(create_list)):
        word = word_tokenize(create_list[i])
        # join list
        list_after_tokenize += word
    return list_after_tokenize


frequency_dict = {}
# Main:
def vis(path, gram):
    master_file = load_file('/Users/jordanchen/Python/cleaned_airbnb_out.csv', 'Cleaned Data')
    blob = ' '.join(master_file)

    csv_into_list = load_file(path, gram)  # Run load_file function
    # csv_tokenized_list = tokenize_csv_column(csv_into_list)  # Run tokenize function


    # frequency_dict = dict(Counter(csv_into_list))  # Using counter function to count how many times the words appear in the list

    for element in csv_into_list:
        frequency_dict[element] = blob.count(element)


    # sort by frequency high to low and return sort dict:
    sort_high_to_low_dict = dict(sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True))
    df_high_to_low = pd.DataFrame(list(sort_high_to_low_dict.items()),columns = ['Key Word','Frequency'])

    short_df = df_high_to_low.head(50)

    short_df.plot.bar(x = 'Key Word', y = 'Frequency', rot = 70)
    plt.show(block=True)

# vis('/Users/jordanchen/Python/bigramed_airbnb_df_out.csv', 'Bigramed Data')
vis('/Users/jordanchen/Python/trigramed_airbnb_df_out.csv', 'Trigramed Data')

