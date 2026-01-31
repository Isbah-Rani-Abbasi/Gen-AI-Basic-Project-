import os
import urllib.request
import urllib.error
import json

KEY_FILE = ".env"
url = "https://generativelanguage.googleapis.com/v1beta/models?key={}"

def get_api_key():
    if not os.path.exists(KEY_FILE):
        return None
    with open(KEY_FILE, 'r') as f:
        for line in f:
            if line.strip().startswith("GOOGLE_API_KEY="):
                return line.strip().split("=", 1)[1]
    return None

def verify():
    key = get_api_key()
    if not key:
        print("No API Key found.")
        return

    print(f"Testing API Key: {key[:5]}...{key[-5:]}")
    
    target_url = url.format(key)
    
    try:
        with urllib.request.urlopen(target_url) as response:
            data = json.loads(response.read().decode())
            print("Success! API Key is valid.")
            print("\nAvailable Models:")
            
            imagen_found = False
            for model in data.get('models', []):
                name = model.get('name', 'unknown')
                methods = model.get('supportedGenerationMethods', [])
                print(f"- {name} ({', '.join(methods)})")
                
                if 'generateImages' in methods or 'imagen' in name.lower():
                    imagen_found = True
                    print(f"  *** IMAGE MODEL FOUND: {name} ***")
            
            if not imagen_found:
                print("\nWARNING: No model named 'imagen' or supporting 'generateImages' was found.")
                print("This key likely only has access to text/multimodal models (Gemini).")
                
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} {e.reason}")
        print(e.read().decode())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify()
