import os
import sys
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def check_directories():
    required_dirs = [
        './philharmonia',
        './philharmonia/train',
        './philharmonia/test'
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
            try:
                os.makedirs(dir_path)
                print(f"Created directory: {dir_path}")
            except Exception as e:
                print(f"Error creating directory {dir_path}: {str(e)}")
    
    return len(missing_dirs) == 0

def main():
    print("Checking environment setup...")
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check ffmpeg
    if check_ffmpeg():
        print("? ffmpeg is installed")
    else:
        print("? ffmpeg is not installed. Please install ffmpeg:")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt-get install ffmpeg")
        print("  Windows: download from https://ffmpeg.org/download.html")
    
    # Check directories
    if check_directories():
        print("? Required directories exist")
    else:
        print("! Some directories were created")
    
    print("\nEnvironment check complete.")

if __name__ == "__main__":
    main()
