from collections import Counter
from responses import data, get_philos_response  # Import the data and the response function
from user_functions import preprocess, pos_tag, extract_nouns, compare_overlap, compute_similarity
import spacy
# word2vec = spacy.load('en')
nlp = spacy.load("en_core_web_md")

exit_commands = ("quit", "goodbye", "exit", "no")

class PhilosophyChatBot:
  
  #define .make_exit() below:
  def make_exit(self,user_message):
    for exit_command in exit_commands:
      if exit_command in user_message:
        print("Okay, thanks have a great day!")
        return True    
  #define .chat() below:
  def chat(self):
    user_message = input("Hey, how's life? What do you want to know about philosophy?")
    while not self.make_exit(user_message):
      user_message = self.respond(user_message)
  #define .find_intent_match() below:
  def find_intent_match(self,responses,user_message):
    bow = preprocess(user_message)
    bow_user_message = Counter(bow)
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(doc,bow_user_message) for doc in processed_responses]
    response_index = similarity_list.index(max(similarity_list))
    return responses[response_index]
 
  #define .find_entities() below:
  def find_entities(self,user_message):
    result = preprocess(user_message)
    tagged_user_message = pos_tag(result)
    message_nouns = extract_nouns(tagged_user_message)
    tokens=nlp(" ".join(message_nouns))
    category=nlp(blank_spot)
    word2vec_result=compute_similarity(tokens,category)
    word2vec_result.sort(key=lambda x: x[2])
    if len(word2vec_result) < 1:
      return blank_spot
    else:
      return word2vec_result[-1][0]
 
# Define .respond() below:
  def respond(self, user_message):
    entity = self.find_entities(user_message)
        
    # Find the most relevant response from the data
    best_response = self.find_intent_match(data, user_message)
        
    response = get_philos_response(entity)  # Generate response based on corpus
    print(response)
    input_message = input("Any other questions?")
    return input_message

# Initialize PhilosophyChatBot instance below:
philosophy_bot = PhilosophyChatBot()
# Call .chat() method below:
philosophy_bot.chat()


