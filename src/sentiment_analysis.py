```python
from nlp_models import nlp_model
from textblob import TextBlob

def analyze_sentiment(text_data):
    """
    Function to analyze the sentiment of the text.
    It uses the TextBlob library to get the polarity of the text.
    The polarity is a float within the range [-1.0, 1.0] where -1 means negative sentiment and 1 means a positive sentiment.
    """
    # Use the NLP model to tokenize the text
    tokenized_text = nlp_model.tokenize(text_data)

    # Analyze the sentiment of each token
    sentiment_scores = [TextBlob(token).sentiment.polarity for token in tokenized_text]

    # Calculate the average sentiment score
    average_sentiment = sum(sentiment_scores) / len(sentiment_scores)

    return average_sentiment
```