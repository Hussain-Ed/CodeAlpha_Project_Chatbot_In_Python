import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files
nltk.download('punkt')

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, how can I help you?", "Hey there! How can I assist you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me Chatbot!",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem at all.",]
    ],
    [
        r"I am (.*) (good|well|okay|ok|happy)",
        ["Nice to hear that! How can I assist you today?",]
    ],
    [
        r"(.*) (help|assist) (.*)",
        ["Sure, I am here to help you. What do you need assistance with?",]
    ],
    [
        r"quit",
        ["Bye for now. Take care!", "Goodbye! It was nice talking to you."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you please rephrase?",]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to extract named entities using spaCy
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to initiate conversation
def start_chat():
    print("Hi, I'm a chatbot. How can I help you today?")
    print("Type 'quit' to exit the chat.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day.")
            break
        # Extract entities using spaCy
        entities = extract_entities(user_input)
        if entities:
            print("I noticed you mentioned the following entities:")
            for ent in entities:
                print(f" - {ent[0]} ({ent[1]})")
        response = chatbot.respond(user_input)
        print(response)

# Start the chat
if __name__ == "__main__":
    start_chat()
