from pathlib import Path
from PIL import Image
from tqdm import tqdm
import re

def natural_sort_key(s: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

def main():
    folder_input = input("Enter image folder path: ").strip()
    in_dir = Path(folder_input).expanduser().resolve()

    if not in_dir.exists() or not in_dir.is_dir():
        print(f"❌ Invalid folder: {in_dir}")
        return

    # Create normalized JPG folder
    out_dir = in_dir / f"{in_dir.name}_normalized_jpg"
    out_dir.mkdir(exist_ok=True)

    supported_ext = {".jpg", ".jpeg", ".png", ".webp"}

    # Collect and sort files naturally
    image_files = sorted(
        [p for p in in_dir.iterdir() if p.is_file() and p.suffix.lower() in supported_ext],
        key=lambda p: natural_sort_key(p.name)
    )

    if not image_files:
        print("⚠️ No supported images found.")
        return

    jpg_paths = []

    print(f"\n📸 Converting images to JPG in: {out_dir}\n")
    for i, img_path in enumerate(tqdm(image_files, desc="Processing"), start=1):
        new_name = f"{i:04d}.jpg"
        out_path = out_dir / new_name

        try:
            with Image.open(img_path) as img:
                img = img.convert("RGB")
                img.save(out_path, "JPEG", quality=95)

            jpg_paths.append(out_path)

        except Exception as e:
            print(f"\n❌ Failed: {img_path.name} → {e}")

    if not jpg_paths:
        print("⚠️ No images converted. PDF not created.")
        return

    # Save PDF in original folder
    pdf_path = in_dir / "merged_output.pdf"

    print(f"\n📄 Creating PDF: {pdf_path}\n")

    with Image.open(jpg_paths[0]) as first_img:
        rest_imgs = [Image.open(p) for p in jpg_paths[1:]]
        first_img.save(pdf_path, save_all=True, append_images=rest_imgs)
        for img in rest_imgs:
            img.close()

    print("✅ Done!")
    print(f"📁 JPG folder: {out_dir}")
    print(f"📄 PDF saved at: {pdf_path}")

if __name__ == "__main__":
    main()
