import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Load a sample text
sample_text = "this this is a project project of AI of Data Science."

# Process the text using spaCy
doc = nlp(sample_text)

# Remove stop words and perform lemmatization
lemmas = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]

# Compute the frequency distribution of lemmas
lemma_freq = Counter(lemmas)

# Print the top 10 most common lemmas
for lemma, freq in lemma_freq.most_common(10):
    print(lemma, freq)
