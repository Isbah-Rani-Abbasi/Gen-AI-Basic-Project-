import os
import urllib.request
import json

KEY_FILE = ".env"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def get_api_key():
    if not os.path.exists(KEY_FILE):
        return None
    with open(KEY_FILE, 'r') as f:
        for line in f:
            if line.strip().startswith("GOOGLE_API_KEY="):
                return line.strip().split("=", 1)[1]
    return None

def test_text_gen():
    key = get_api_key()
    if not key:
        print("No key found")
        return

    url = f"{API_URL}?key={key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "Write a one-sentence horror story."}]
        }]
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print("Success! Text generation works.")
            print("Response snippet:", result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No text'))
    except Exception as e:
        print(f"Error testing text generation: {e}")

if __name__ == "__main__":
    test_text_gen()
