# 👻 Automated Horror Story Visualizer

> **An end-to-end Generative AI pipeline that turns text narratives into custom cover art automatically.**

## 📖 About The Project
This project automates the creative workflow of visualizing storytelling. It scrapes raw text from horror story communities, analyzes the narrative using Large Language Models (LLMs), and generates atmospheric cover images using Text-to-Image models.

I built this to explore the intersection of **Web Scraping**, **Prompt Engineering**, and **Generative AI** in a cohesive Python pipeline.

## ⚙️ How It Works (The Pipeline)
The system operates in three distinct stages:

1.  **Data Extraction (`scrape_rss.py`):** Fetches horror stories from online community threads.
2.  **Narrative Analysis (`prepare_prompts.py`):** An LLM reads the story, extracts key visual elements (setting, characters, atmosphere), and constructs a detailed art prompt.
3.  **Image Synthesis (`generate_images_google.py`):** The prompt is fed into a Generative AI model to render the final cover art.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **GenAI:** Google Gemini (LLM & Vision) / Stable Diffusion (depending on config)
* **Web Scraping:** BeautifulSoup4 / Selenium
* **Data Handling:** Pandas, JSON

## 📂 Project Structure
```text
gen-ai-basicproject/
├── data/
│   ├── stories.json       # Raw scraped text
│   └── prompts.json       # Generated art prompts
├── images/                # Final output images
├── scrape_rss.py          # Scraper script
├── prepare_prompts.py     # LLM analysis script
├── generate_images.py     # Image generation script
└── README.md
