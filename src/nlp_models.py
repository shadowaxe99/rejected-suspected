```python
from transformers import BertModel, BertTokenizer, RobertaModel, RobertaTokenizer
import torch

class NLPModel:
    def __init__(self, model_type='bert'):
        self.model_type = model_type
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        if self.model_type == 'bert':
            self.model = BertModel.from_pretrained('bert-base-uncased')
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        elif self.model_type == 'roberta':
            self.model = RobertaModel.from_pretrained('roberta-base')
            self.tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
        else:
            raise ValueError("Invalid model type. Choose 'bert' or 'roberta'.")

    def encode_text(self, text):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        return encoded_input

    def get_embeddings(self, text):
        encoded_input = self.encode_text(text)
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        return model_output.last_hidden_state

nlp_model = NLPModel()
```
