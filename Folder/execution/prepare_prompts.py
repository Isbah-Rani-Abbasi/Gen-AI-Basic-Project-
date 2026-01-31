import os
import glob
import json

OUTPUT_DIR = ".tmp"

def get_stories():
    files = glob.glob(os.path.join(OUTPUT_DIR, "story_*.txt"))
    stories = []
    
    # Sort files by number in filename (story_1.txt, story_2.txt...)
    files.sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))

    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        title = "Untitled"
        content = ""
        
        if lines:
            if lines[0].startswith("Title:"):
                title = lines[0].replace("Title:", "").strip()
                content = "".join(lines[2:]).strip() # Skip title and newline
            else:
                content = "".join(lines).strip()
        
        # Create a short prompt excerpt
        excerpt = content[:150].replace('\n', ' ') + "..."
        
        stories.append({
            "filename": os.path.basename(fpath),
            "title": title,
            "prompt_content": excerpt
        })
        
    # Save to file
    output_path = os.path.join(OUTPUT_DIR, "prompts.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(stories, f, indent=2)
    print(f"Prompts saved to {output_path}")

if __name__ == "__main__":
    get_stories()
