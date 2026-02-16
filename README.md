### 1. Create uv environment
```
uv venv ~/env/image_proc
```

### 2. Activate uv environment

```
source ~/env/image_proc/bin/activate
```

### 3. Install packages
```
uv pip install Pillow tqdm
```

### 3. How to run
```
python3 image_to_pdf_final.py
```
- past the absolute path containing the pictures in the prompt. For example:
```
Enter image folder path: <absolute_path_to_picture_folder>
```