# Scrape Horror Stories Directive

**Goal**: Scrape 10 unique horror stories from r/shortscarystories (or similar) into the `.tmp/` directory.

**Tool**: `execution/scrape_rss.py`

**Inputs**:
- Subreddit RSS URL (default: `https://www.reddit.com/r/shortscarystories/new/.rss`)
- Number of stories: 10

**Process**:
1.  Run the python script.
2.  Script fetches the RSS feed.
3.  Script parses XML to find `<entry>` or `<item>` tags.
4.  Extracts title and content mapping.
5.  Saves files as `.tmp/story_1.txt` ... `.tmp/story_10.txt`.
6.  **Verification**: The script creates a report or prints output confirming 10 non-empty files.

**Edge Cases**:
- **Empty content**: Some RSS items might be links-only. Skip them.
- **Not enough items**: Fetch more or fail gracefully (user can rerun).
- **Network error**: Retry or report failure.
