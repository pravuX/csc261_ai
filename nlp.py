import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")

example_string = "This is a sample paragraph. Now, this is the second sentence. This is so fun!"


sentences = sent_tokenize(example_string)
print("\nSentence Tokenization\n", sentences)

words = word_tokenize(example_string)
print("\nWord Tokenization\n", words)

stop_words = set(stopwords.words("english"))

filtered_list = [
    word for word in words if word.casefold() not in stop_words]
print("\nStop Word filtering\n", filtered_list)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nWord Stemming\n", stemmed_words)

pos_tagged_words = nltk.pos_tag(words)
print("\nPOS Tagging\n", pos_tagged_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("\nWord Lemmatizing\n", lemmatized_words)
print("Unique Bhattarai, 28136/078, Lab No.22")

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(pos_tagged_words)
tree.draw()
