from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

memory = {
    'name': None,
    'feeling': None
}

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

def get_bot_response(user_input):
    if memory['name'] is None:
        memory['name'] = user_input
        return f"Nice to meet you, {memory['name']}! How are you feeling today?"

    if memory['feeling'] is None:
        sentiment = analyze_sentiment(user_input)
        memory['feeling'] = sentiment
        if sentiment == "positive":
            return "I'm glad to hear that! What's making you feel good today?"
        elif sentiment == "negative":
            return "I'm sorry to hear that. Do you want to talk about what's bothering you?"
        else:
            return "I see. Do you want to share more about your day?"

    if memory['feeling'] == "positive":
        return "That's wonderful! Anything else exciting happening?"
    elif memory['feeling'] == "negative":
        return "I'm here to listen. It's okay to share your thoughts."
    else:
        return "Tell me more! I'm here to listen."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    response_text = get_bot_response(user_input)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
