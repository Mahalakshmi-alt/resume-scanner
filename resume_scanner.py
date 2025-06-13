import requests
import json

# Replace with your actual endpoint and key
endpoint = "https://resume-scanner-ai.cognitiveservices.azure.com/"
key = "6JGBJfz0aekHLxlmdlgrYYtEzBEY1VGrveCkciwsZwK27CB6YxvlJQQJ99BFACYeBjFXJ3w3AAAaACOGuKZE"
sentiment_url = endpoint + "language/:analyze-text?api-version=2023-04-01"

# === Step 1: Read from resume.txt ===
with open("resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

# === Step 2: Prepare request ===
headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

body = {
    "kind": "SentimentAnalysis",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": resume_text
            }
        ]
    }
}

# === Step 3: Send request ===
response = requests.post(sentiment_url, headers=headers, json=body)
result = response.json()

# === Step 4: Print result clearly ===
try:
    sentiment = result['results']['documents'][0]['sentiment']
    scores = result['results']['documents'][0]['confidenceScores']
    print("\n🔍 Resume Sentiment Analysis Result:")
    print(f"Sentiment: {sentiment.capitalize()}")
    print("Confidence Scores:")
    print(f"  - Positive: {scores['positive']}")
    print(f"  - Neutral : {scores['neutral']}")
    print(f"  - Negative: {scores['negative']}")
except Exception as e:
    print("❌ Error in response:")
    print(json.dumps(result, indent=2))