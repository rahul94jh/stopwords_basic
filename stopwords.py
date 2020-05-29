import helpers as hp

# Download text of 'Alice in Wonderland' ebook from https://www.gutenberg.org/
# Get list of words from the url
url = "https://www.gutenberg.org/files/11/11-0.txt"
alice = hp.get_words_from_url(url)

# Let's plot the frequency of the words in the downloaded text
df = hp.get_word_frequency_df(alice, 15)
# show the word frequency count plot
# We can see that most of the words with high frequency are stop words
hp.plot_word_frequency(df.labels, df.counts)


""" Removing stopwords from plian texts
    NLTK library provides the list of stop words like is the can e.t.c for many languages, let's see 
    how we can use the stop words defined for English language in nltk corpus to remove the stop words
    from plain english texts. """

# Removing stop words from a sample text
sample_text = "the great aim of education is not knowledge but action"
# create list of words
sample_words = sample_text.split()
# filter the list and remove the stopwords
filtered = list(filter(hp.filter_stopwords, sample_words))
# The sentence now doesn't contain any stopwords
print(" ".join(filtered))


""" Now let's remove stopwords from the alice corpus we have """

# Filter out the stopwords from alice corpus
alice_filtered = list(filter(hp.filter_stopwords, alice))


# Let's plot the frequency of the words in the filtered alice corpus
df = hp.get_word_frequency_df(alice_filtered, 10)

# we have removed most of the stop words but still we can see few issues
# in the alice corpus which needs further cleaning
hp.plot_word_frequency(df.labels, df.counts)
