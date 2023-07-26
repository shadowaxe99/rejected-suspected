```python
import requests
from nlp_models import nlp_model
from TextData import TextData

class ContentModerationPlatform:
    def __init__(self, api_key):
        self.api_key = api_key

    def moderate_content(self, text_data: TextData):
        sarcasm_detected = self.detect_sarcasm(text_data)
        if sarcasm_detected:
            print("Sarcasm detected in content. Please review.")
        else:
            print("No sarcasm detected in content.")

    def detect_sarcasm(self, text_data: TextData):
        headers = {'Authorization': 'Bearer ' + self.api_key}
        response = requests.post('http://localhost:5000/detect_sarcasm', headers=headers, data=text_data)
        if response.status_code == 200:
            return response.json()['sarcasm_detected']
        else:
            print("Error in sarcasm detection API call.")
            return False

if __name__ == "__main__":
    content_moderation_platform = ContentModerationPlatform(api_key)
    text_data = TextData("This is a sample text for sarcasm detection.")
    content_moderation_platform.moderate_content(text_data)
```