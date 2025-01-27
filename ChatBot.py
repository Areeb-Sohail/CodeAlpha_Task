import random

#Chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey, how can I help you today?", "Greetings!"],
    "hi": ["Hi there!", "Hello!", "Hey", "Greetings!"],
    "name":"I don\'t have a name assigned yet you can call me whatever you like",
    "assalamualaikum":["Wa alaikum assalam , Akhi how are you?"],
    "i am fine":["Good to hear that","Happy to have you in good health"],
    "not fine":["Why are you here go take a rest","Sorry to hear that , take care"],
    "i am good":["Good to hear that","Happy to have you in good health"],
    "not good":["Why are you here go take a rest","Sorry to hear that , take care"],
    "good morning": ["Good evening! How can I assist you?", "Good morning! What can I do for you today?"],
    "good evening": ["Good evening! How can I assist you?", "Good evening! What can I do for you today?"],
    "good night": ["Good night! Have a great rest!", "Good night! Take care!"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "bye": ["Goodbye!", "Bye! Hope to talk again soon!", "Take care!"],
    "cook":["I wish I could cook but I am just a chatbot here to chitchat","I can only wish to cook"],
    "how are you": ["I'm doing well, thank you! How about you?", "I'm great, thanks for asking! How are you doing?"],
    "name": ["I'm your friendly chatbot! How can I help you today?", "You can call me your assistant!"],
    "how old are you": ["I don't have an age, but I'm here to help you anytime!", "I'm ageless, but always ready to assist!"],
    "thank you": ["You're welcome!", "Anytime!", "Glad to help!"],
    "thanks": ["You're welcome!", "No problem at all!", "Anytime!"],
    "purpose": ["I can answer questions, assist with tasks, and more!", "I can help with a variety of tasks—what would you like assistance with?"],
    "work": ["I analyze your input and try to provide the best possible response!", "I use algorithms to understand your questions and give helpful answers."],
    "not_understood": ["Sorry, I didn't quite catch that. Can you rephrase?", "I'm not sure I understand, could you try again?"],
    "sorry": ["Sorry about that, let me try to help you better!", "I apologize, let me fix that for you."],
    "weather":["Today is a very pleasent weather","Amazing weather we have today with blue skies and fresh air"],
    "invalid_command": ["I'm sorry, that command isn't recognized. Can you try something else?", "Hmm, that doesn't seem to be a valid command. Could you try again?"],
    "fallback": ["I'm not sure how to respond to that, but I'm here to help with other things!", "Hmm, that's a bit tricky. Can you tell me more?"],
    "help": ["How can I assist you today?", "What can I do for you?", "Feel free to ask me anything!"]
}

#Function to process user input
def process_input(input_text):
    input_text = input_text.lower()
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return random.choice(responses["not_understood"])

#Main chatbot loop
while True:
    user_input = input('User: ')
    response = process_input(user_input)
    print('Chatbot:', response)
