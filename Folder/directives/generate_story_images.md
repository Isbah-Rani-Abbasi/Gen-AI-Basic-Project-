# Generate Story Images Directive

**Goal**: Generate a unique horror illustration for each story in `.tmp/`.

**Tool**: `execution/prepare_prompts.py` and Agent's `generate_image` tool.

**Process**:
1.  Run `execution/prepare_prompts.py` to extract titles/excerpts.
2.  Agent reads the output (JSON).
3.  For each story:
    -   Construct a prompt: `Horror illustration, dark style. {Title}. {Excerpt}`.
    -   Call `generate_image` tool with `ImageName=story_{i}`.
4.  **Verification**: Check that images exist in `.tmp/` or artifacts directory.

**Output**: 10 Image files.
