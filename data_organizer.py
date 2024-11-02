import os
import shutil
import random
from pathlib import Path

def setup_directories():
    # Create train and test directories
    Path("./philharmonia/train").mkdir(parents=True, exist_ok=True)
    Path("./philharmonia/test").mkdir(parents=True, exist_ok=True)

def split_data(source_dir, train_ratio=0.8):
    for instrument in os.listdir(source_dir):
        if os.path.isdir(os.path.join(source_dir, instrument)):
            files = os.listdir(os.path.join(source_dir, instrument))
            random.shuffle(files)
            
            split_idx = int(len(files) * train_ratio)
            train_files = files[:split_idx]
            test_files = files[split_idx:]
            
            # Create instrument directories in train and test
            Path(f"./philharmonia/train/{instrument}").mkdir(exist_ok=True)
            Path(f"./philharmonia/test/{instrument}").mkdir(exist_ok=True)
            
            # Copy files to train
            for f in train_files:
                src = os.path.join(source_dir, instrument, f)
                dst = f"./philharmonia/train/{instrument}/{f}"
                shutil.copy2(src, dst)
            
            # Copy files to test
            for f in test_files:
                src = os.path.join(source_dir, instrument, f)
                dst = f"./philharmonia/test/{instrument}/{f}"
                shutil.copy2(src, dst)

def main():
    setup_directories()
    split_data("./philharmonia/original")

if __name__ == "__main__":
    main()
