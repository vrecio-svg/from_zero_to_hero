import nltk

sample_text = "Me encanta comer crema de cacahuete"

from nltk.tokenize import word_tokenize

tokens = word_tokenize(sample_text)

print("Tokens: ", tokens)