# Google Image Generation Directive

**Goal**: Generate images using Google's Imagen model via API Key.

**Tool**: `execution/generate_images_google.py`

**Inputs**:
- `GOOGLE_API_KEY` in `.env`
- `.tmp/prompts.json`

**Process**:
1.  Run `python execution/generate_images_google.py`.
2.  Script saves images to `.tmp/images/story_{i}_google.png`.

**Output**: 10 PNG images.
