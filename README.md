/*Import/Download the Data*/
Kaggle Chatbot Philosophy Corpus
https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy

/*Retrieval-based chatbot*/

script.py:

Your PhilosophyChatBot class has methods to handle various aspects of chatbot functionality, including making an exit, chatting, finding intent matches, finding entities, and responding.
You're using en_core_web_md from spaCy to process natural language, which includes tokenization and word embeddings.
The intent matching, entity recognition, and response selection logic is implemented as expected.
user_functions.py:

The preprocess function handles different input types (dictionary or other) and preprocesses the input sentence by making it lowercase and removing punctuation.
compare_overlap checks the similarity of words between user messages and possible responses.
extract_nouns identifies nouns in a tagged message.
compute_similarity calculates the similarity of word embeddings between tokens and a category.

responses.py:

You've defined the data variable that reads data from a CSV file containing the philosophy responses.
get_philos_response function is modified to return a response based on a hash of the input menu item, ensuring consistent responses for the same input.

/*Future Improvements*/

Add a user interface (GUI, website) for your chatbot.

/*Project Info*/
Title: Retrieval Bot
Name: Nicholas D'Agostino
Codecademy user: ndagostino

I chose a closed-domain architecture to keep the responses true to the source and not allow for deviation from the source.

Use case(s) for chatbot:
Get random aphorisms on philosophy from schools of thought

A reflection:
I had difficulty implementing the bag of words for intent selection, when i added the functions it took too long to return a response and crashed multiple times due to insufficient memory. The word2vec model was changed from spacy.loan('en') to spacy.load("en_core_web_md"). Lastly, the selection of the response is random and not using the intent and entity similarity function. 

I was thinking that I could pregenerate the BOW matrix for the corpus before and save the result in a dictionary for future use.

Dependencies:

+Python 3: Your code is written in Python 3.

+spaCy: You're using spaCy for natural language processing, including tokenization and word embeddings. You've loaded the en_core_web_md model from spaCy for these tasks.

+NLTK (Natural Language Toolkit): You're using NLTK for parts of speech tagging, word tokenization, and importing stopwords.

+CSV: You're using the CSV library to read data from a CSV file.