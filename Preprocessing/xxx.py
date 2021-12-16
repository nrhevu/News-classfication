from os import remove
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))

def clean_header(text):
    text = re.sub(r'(From:\s+[^\n]+\n)', '', text)
    text = re.sub(r'(Subject:[^\n]+\n)', '', text)
    text = re.sub(r'(([\sA-Za-z0-9\-]+)?[A|a]rchive-name:[^\n]+\n)', '', text)
    text = re.sub(r'(Last-modified:[^\n]+\n)', '', text)
    text = re.sub(r'(Version:[^\n]+\n)', '', text)
    return text

def clean_text(text):
    # remove header
    text = clean_header(text)
    # lower text
    text = text.lower()
    # remove text in square brackets
    text = re.sub('\[.*?\]', ' ', text)
    # remove link
    text = re.sub('https?://\S+|www\.\S+', ' ', text)
    # remove email
    text = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)',' ', text)
    # remove HTML tag
    text = re.sub('<.*?>+', ' ', text)
    # remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    # remove special characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # remove empty line
    text = re.sub('\n', ' ', text)
    # remove words containing numbers.
    text = re.sub('\w*\d\w*', ' ', text)
    # remove extra whitespaces
    text = re.sub(' +', ' ', text)
    # remove single character
    text = ' '.join([word for word in text.split() if len(word) > 1])
    return text.strip()

def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    words_of_sentences = [word for word in word_tokens if not word.lower() in stopwords]
    print(words_of_sentences)
    return words_of_sentences


def combine_text(list_of_text):
    combined_text = ' '.join(list_of_text)
    return combined_text

def preprocess(text):
    txt = clean_text(text)
    txt = remove_stopwords(txt)
    txt = combine_text(txt)
    return txt

#demo
#txt = 'This is a sample sentence, showing off the stop words filtration.'
#print(preprocess(txt))
