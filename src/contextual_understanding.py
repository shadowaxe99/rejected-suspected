```python
import spacy
from nlp_models import nlp_model

def contextual_understanding(text_data):
    """
    Function to analyze the context of the text for sarcasm detection.
    """
    doc = nlp_model(text_data)
    context = {}

    # Extract entities and their context
    for ent in doc.ents:
        context[ent.text] = ent.root.head.text

    return context

def detect_sarcasm_context(text_data, context):
    """
    Function to detect sarcasm based on the context of the text.
    """
    sarcasm_detected = False

    # Check for common sarcasm indicators in context
    for entity, root in context.items():
        if root.lower() in ['but', 'though', 'actually']:
            sarcasm_detected = True
            break

    return sarcasm_detected
```