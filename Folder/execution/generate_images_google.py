import os
import json
import urllib.request
import urllib.error
import base64

# Configuration
KEY_FILE = ".env"
PROMPTS_FILE = ".tmp/prompts.json"
OUTPUT_DIR = ".tmp/images"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict"

def get_api_key():
    if not os.path.exists(KEY_FILE):
        print("Error: .env file not found")
        return None
    
    with open(KEY_FILE, 'r') as f:
        for line in f:
            if line.strip().startswith("GOOGLE_API_KEY="):
                return line.strip().split("=", 1)[1]
    return None

def generate_image(api_key, context, index):
    prompt_text = f"Dark horror illustration, atmospheric. {context['title']}. {context['prompt_content']}"
    
    payload = {
        "instances": [
            {
                "prompt": prompt_text
            }
        ],
        "parameters": {
            "sampleCount": 1
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    url = f"{API_URL}?key={api_key}"
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            
            # The structure depends on the API version, but typically:
            # { "predictions": [ { "bytesBase64Encoded": "..." } ] }
            
            if "predictions" in result:
                b64_img = result["predictions"][0]["bytesBase64Encoded"]
                
                # Ensure output dir exists
                if not os.path.exists(OUTPUT_DIR):
                    os.makedirs(OUTPUT_DIR)
                    
                filename = f"story_{index}_google.png"
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                with open(filepath, "wb") as f:
                    f.write(base64.b64decode(b64_img))
                    
                print(f"Generated: {filepath}")
                return True
            else:
                print(f"Unexpected response format for story {index}: {result}")
                return False

    except urllib.error.HTTPError as e:
        print(f"HTTP Error for story {index}: {e.code} {e.reason}")
        print(e.read().decode())
        return False
    except Exception as e:
        print(f"Error generating story {index}: {e}")
        return False

def main():
    api_key = get_api_key()
    if not api_key:
        print("Could not find GOOGLE_API_KEY in .env")
        return

    if not os.path.exists(PROMPTS_FILE):
        print(f"Prompts file not found: {PROMPTS_FILE}")
        return

    with open(PROMPTS_FILE, 'r') as f:
        prompts = json.load(f)

    success_count = 0
    for i, p in enumerate(prompts):
        # 1-indexed naming
        if generate_image(api_key, p, i+1):
            success_count += 1
            
    print(f"Finished. Generated {success_count}/{len(prompts)} images.")

if __name__ == "__main__":
    main()
