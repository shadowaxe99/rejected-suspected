```python
from src.nlp_models import nlp_model
from src.contextual_understanding import ContextualUnderstanding
from src.sentiment_analysis import analyze_sentiment
from src.ambiguity_detection import AmbiguityDetection
from src.user_feedback import handle_feedback
from src.api_integration import integrate_api

class SarcasmDetector:
    def __init__(self):
        self.nlp_model = nlp_model
        self.contextual_understanding = ContextualUnderstanding()
        self.ambiguity_detection = AmbiguityDetection()
        self.api_key = None

    def detect_sarcasm(self, text_data):
        sarcasm_detected = self.nlp_model.predict(text_data)
        if sarcasm_detected:
            context = self.contextual_understanding.get_context(text_data)
            sarcasm_detected = self.ambiguity_detection.check_ambiguity(sarcasm_detected, context)
            sentiment = analyze_sentiment(text_data)
            return {"sarcasm": sarcasm_detected, "sentiment": sentiment}
        else:
            return {"sarcasm": sarcasm_detected}

    def receive_feedback(self, feedback_data):
        handle_feedback(feedback_data)

    def integrate_api(self, api_key):
        self.api_key = api_key
        integrate_api(api_key)

if __name__ == "__main__":
    sarcasm_detector = SarcasmDetector()
    text_data = input("Enter text to analyze: ")
    print(sarcasm_detector.detect_sarcasm(text_data))
```
