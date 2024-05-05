import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def process_text(input_text):
    tokens = word_tokenize(input_text)
    return tokens
user_input = "What's the weather like today?"
tokens = process_text(user_input)
print(tokens)


from nltk import FreqDist
from nltk.corpus import stopwords
nltk.download('stopwords')
def recognize_intent(tokens):
    # Remove stopwords and non-alphabetic tokens
    filtered_tokens = [word for word in tokens if word.isalpha() and word.lower() not in stopwords.words('english')]

    # Calculate frequency distribution of tokens
    freq_dist = FreqDist(filtered_tokens)

    # Identify the most common token as the intent
    intent = freq_dist.max()

    return intent
intent = recognize_intent(tokens)
print("User intent:", intent)




def generate_response(intent):
    responses = {
        "weather": "The weather today is sunny with a high of 25°C.",
        "greeting": "Hello! How can I assist you today?",
        "farewell": "Goodbye! Have a great day!"
    }

    response = responses.get(intent, "I'm sorry, I didn't understand that.")
    return response
response = generate_response(intent)
print("Virtual assistant:", response)
