import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import os
import html
import re

# Configuration
RSS_URL = "https://www.reddit.com/r/shortscarystories/new/.rss"
OUTPUT_DIR = ".tmp"
TARGET_COUNT = 10
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def clean_html(raw_html):
    """Remove HTML tags to get plain text."""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return html.unescape(cleantext).strip()

def scrape_stories():
    print(f"Fetching RSS feed from {RSS_URL}...")
    try:
        req = urllib.request.Request(RSS_URL, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            content = response.read()
    except Exception as e:
        print(f"Error fetching RSS: {e}")
        return

    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return

    # Namespaces
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    entries = root.findall('atom:entry', ns)
    if not entries:
        # Try standard RSS 2.0 'item'
        entries = root.findall('.//item')

    print(f"Found {len(entries)} entries in feed.")

    count = 0
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for i, entry in enumerate(entries):
        if count >= TARGET_COUNT:
            break

        # Extract title
        title_elem = entry.find('atom:title', ns)
        if title_elem is None: title_elem = entry.find('title')
        title = title_elem.text if title_elem is not None else "No Title"

        # Extract content
        content_elem = entry.find('atom:content', ns)
        if content_elem is None: content_elem = entry.find('description')
        raw_content = content_elem.text if content_elem is not None else ""
        
        content = clean_html(raw_content)

        # skip if empty or just a link 
        if len(content) < 50: 
            print(f"Skipping entry {i}: Content too short.")
            continue

        filename = os.path.join(OUTPUT_DIR, f"story_{count+1}.txt")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n\n")
            f.write(content)
        
        print(f"Saved: {filename}")
        count += 1

    if count < TARGET_COUNT:
        print(f"Warning: Only scraped {count} stories. Feed might not have enough text-based posts.")
    else:
        print(f"Successfully scraped {count} horror stories.")

if __name__ == "__main__":
    scrape_stories()
