# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup and commands

```bash
# Create and activate environment (uv)
uv venv ~/env/image_proc
source ~/env/image_proc/bin/activate

# Install dependencies
uv pip install Pillow tqdm

# Run the script
python3 image_to_pdf_final.py
```

The script prompts interactively for `Enter image folder path:` — pass the absolute path to a folder of images.

There are no tests, linter, or build step configured in this repository.

## Architecture

This is a single-script utility (`image_to_pdf_final.py`) with no package structure. The flow, all within `main()`:

1. Prompt for an input folder path.
2. Collect `.jpg`/`.jpeg`/`.png`/`.webp` files from that folder (non-recursive), sorted with a natural-sort key (`natural_sort_key`) so numeric filename segments sort numerically rather than lexicographically.
3. Convert each image to RGB JPEG (quality 95), writing sequentially numbered output (`0001.jpg`, `0002.jpg`, ...) into a sibling `<folder>_normalized_jpg/` directory.
4. Merge the converted JPGs into a single `merged_output.pdf` saved in the original input folder, using Pillow's multi-image PDF save (`save_all=True, append_images=...`).

`temp/` contains sample `.webp` input images used for manual testing of the conversion flow — not part of the library/package surface.
