import shutil
from pathlib import Path

def copy_prefixed_train_data(source_dir: Path, target_dir: Path, prefix: str) -> int:
    """ Copy images which starts with a prefix"""
    copied_images = 0
    
    if not source_dir.exists():
        print("Source path not found")
        return copied_images
    if not target_dir.exists():
        print("Target dir not found")
        return copied_images
        
    for img in source_dir.iterdir:
        if not img.is_file():
            continue
        if not img.name.startswith(prefix):
            continue
        
        shutil.copy2(source_dir, target_dir)
        copied_images += 1
        
    print(f"Number of copied images: {copied_images}")
    return copied_images