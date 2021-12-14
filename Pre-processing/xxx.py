import re
import string

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

start_time = time()
df['cleaned_text'] = df['text'].apply(clean_text)
print("Time to process data: " + str(time() - start_time) + 's')

df['cleaned_text'].head()

df['number_of_cleaned_words'] = df['cleaned_text'].apply(lambda x:len(str(x).split()))
df.head()

df['number_of_cleaned_words'].describe()

# number of rows with text length = 0
no_text = df[df['number_of_cleaned_words']==0]
print(len(no_text))

# drop these rows
df.drop(no_text.index,inplace=True)

df['tokens'] = df['cleaned_text'].apply(lambda x: x.split())
df.head()

# stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
print(ENGLISH_STOP_WORDS)

len(ENGLISH_STOP_WORDS)

# removing stopwords
stop_words = ENGLISH_STOP_WORDS

def remove_stopwords(text):
    words = [word for word in text if word not in stop_words]
    return words 
df['stopwords_remove_tokens'] = df['tokens'].apply(lambda x : remove_stopwords(x))
df.head()

from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

def lem_word(x):
    return [lem.lemmatize(w, pos="v") for w in x]

df['lemmatized_text'] = df['stopwords_remove_tokens'].apply(lem_word)
df.head()

def combine_text(list_of_text):
    combined_text = ' '.join(list_of_text)
    return combined_text

df['final_text'] = df['lemmatized_text'].apply(lambda x : combine_text(x))
df.head()

df['final_number_of_words'] = df['final_text'].apply(lambda x:len(str(x).split()))
df.head()

df['final_number_of_words'].describe()

# number of rows with text length = 0
no_text = df[df['final_number_of_words'] == 0]
print(len(no_text))

# drop these rows
df.drop(no_text.index,inplace=True)

plt.style.use('ggplot')
plt.figure(figsize=(12,6))
sns.distplot(df['final_number_of_words'], kde = False,color="red", bins=200)
plt.title("Frequency distribution of number of words for each text extracted", size=20)

df.to_csv(data_root_path + "data.csv", index=False)