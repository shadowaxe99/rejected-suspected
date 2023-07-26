```python
import requests
from nlp_models import nlp_model
from sentiment_analysis import analyze_sentiment

class SocialMediaManager:
    def __init__(self, api_key):
        self.api_key = api_key

    def monitor_social_media(self, text_data):
        sarcasm_detected = self.detect_sarcasm(text_data)
        sentiment = self.analyze_sentiment(text_data)
        return sarcasm_detected, sentiment

    def detect_sarcasm(self, text_data):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post('http://localhost:5000/detect_sarcasm', headers=headers, json=text_data)
        if response.status_code == 200:
            return response.json()['sarcasm_detected']
        else:
            raise Exception('Sarcasm detection failed.')

    def analyze_sentiment(self, text_data):
        sentiment = analyze_sentiment(nlp_model, text_data)
        return sentiment

    def handle_feedback(self, feedback_data):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post('http://localhost:5000/handle_feedback', headers=headers, json=feedback_data)
        if response.status_code == 200:
            return response.json()['feedback_received']
        else:
            raise Exception('Feedback handling failed.')
```