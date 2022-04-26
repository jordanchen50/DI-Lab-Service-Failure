import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time, os
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

start_time = time.time()

stopWords = set(stopwords.words("english"))
stopWords.add("uber")
stopWords.add("airbnb")

def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize(rawString):
    uniform_string = re.sub('[^A-Za-z0-9]+', ' ', rawString).lower()

    updatedStringToken = word_tokenize(uniform_string)
    filteredSW = [w for w in updatedStringToken if not w in stopWords]

    pos_tagged = nltk.pos_tag(filteredSW)
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []

    for word, tag in wordnet_tagged:
        if tag is None:
            lemmatized_sentence.append(word)
        else:
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))

    return ' '.join(lemmatized_sentence)

# airbnb_df = pd.read_csv('/Users/jordanchen/Python/airbnb_out.csv', usecols=['Review'])
# uber_df = pd.read_csv('/Users/jordanchen/Python/uber_out.csv', usecols=['Review'])

train_df = pd.read_csv('/Users/jordanchen/Python/TRAIN_DATA.csv', usecols=['TRAIN'])
train_list = train_df.values.tolist()
# airbnb_review_list = airbnb_df.values.tolist()
# uber_review_list = uber_df.values.tolist()


# cleaned_airbnb_data = []
# cleaned_uber_data = []

cleaned_train_data = []

for review in train_list:
    temp = lemmatize(str(review))
    cleaned_train_data.append(temp)

# for review in uber_review_list:
#     cleaned_uber_data.append(lemmatize(str(review)))

# cleaned_airbnb_df = pd.DataFrame(list(zip(cleaned_airbnb_data,)),columns=['Cleaned Data'])
# os.makedirs('/Users/jordanchen/Python', exist_ok=True)
# cleaned_airbnb_df.to_csv('/Users/jordanchen/Python/cleaned_airbnb_out.csv')

# cleaned_uber_df = pd.DataFrame(list(zip(cleaned_uber_data,)),columns=['Cleaned Data'])
# os.makedirs('/Users/jordanchen/Python', exist_ok=True)
# cleaned_uber_df.to_csv('/Users/jordanchen/Python/cleaned_uber_data_out.csv')

cleaned_train_df = pd.DataFrame(list(zip(cleaned_train_data,)), columns=['Cleaned Train'])
os.makedirs('/Users/jordanchen/Python', exist_ok=True)
cleaned_train_df.to_csv('/Users/jordanchen/Python/cleaned_train_data_out.csv')
# print("--- %s seconds ---" % (time.time() - start_time))



# bi gram tri gram testing
# airbnb_review_list 
# uber_review_list 
# test = ["Hi My Hi My name is Jordan", "this is the 2 test"]

# from nltk import bigrams, trigrams
# all_bigrams = []
# all_trigrams = []

# for element in cleaned_airbnb_data:
#     unigrams = word_tokenize(element)
    
#     temp_bigrams = bigrams(unigrams)
#     temp_bigrams_list = list(temp_bigrams)

#     for words in temp_bigrams_list:
#         temp_word = ' '.join(words)
        
#         if temp_word not in all_bigrams: 
#             all_bigrams.append(temp_word)

#     temp_trigrams = trigrams(unigrams)
#     temp_trigrams_list = list(temp_trigrams)

#     for words in temp_trigrams_list:
#         temp_word = ' '.join(words)

#         if temp_word not in all_trigrams:
#             all_trigrams.append(temp_word)


# bigramed_airbnb_df = pd.DataFrame(list(zip(all_bigrams,)),columns=['Bigramed Data'])
# os.makedirs('/Users/jordanchen/Python', exist_ok=True)
# bigramed_airbnb_df.to_csv('/Users/jordanchen/Python/bigramed_airbnb_df_out.csv')

# trigramed_uber_df = pd.DataFrame(list(zip(all_trigrams,)),columns=['Trigramed Data'])
# os.makedirs('/Users/jordanchen/Python', exist_ok=True)
# trigramed_uber_df.to_csv('/Users/jordanchen/Python/trigramed_airbnb_df_out.csv')