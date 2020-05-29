import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from nltk import FreqDist
from nltk.corpus import stopwords
import nltk

# this needs to be run if nltk corpora is not already avilable
# nltk.download("stopwords")


def get_words_from_url(url: str) -> list:
    data = requests.get(url)
    # get the text and convert the text to lower case
    text = data.text.lower()
    # get a list of words from the downloaded text
    words = text.split()
    return words


def get_word_frequency_df(words, top_n=10) -> pd.DataFrame:
    word_freq = FreqDist(words)
    labels = [element[0] for element in word_freq.most_common(top_n)]
    counts = [element[1] for element in word_freq.most_common(top_n)]
    df = pd.DataFrame(list(zip(labels, counts)), columns=["labels", "counts"])
    return df


def plot_word_frequency(x: str, y: str):
    _ = sns.barplot(x, y)
    plt.show()


def filter_stopwords(word: str) -> bool:
    return False if word in stopwords.words("english") else True
