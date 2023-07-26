```python
import requests
from typing import Dict

api_key = "YOUR_API_KEY"

def integrate_api(text: str) -> Dict:
    """
    Function to integrate the sarcasm detector API.
    """
    url = "https://api.sarcasm_detector.com/detect"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API request failed"}

def get_sarcasm_score(text: str) -> float:
    """
    Function to get the sarcasm score from the API response.
    """
    response = integrate_api(text)
    if "error" not in response:
        return response["sarcasm_score"]
    else:
        return None
```