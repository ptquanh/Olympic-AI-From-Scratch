#!/usr/bin/env python3
"""
Format all Jupyter notebooks and Python scripts in the curriculum using black.
Usage: python tools/format_notebooks.py
"""

import subprocess
import sys
from pathlib import Path

def main():
    root_dir = Path(__file__).resolve().parent.parent
    modules_dir = root_dir / "modules"
    
    if not modules_dir.exists():
        print(f"Error: {modules_dir} not found.")
        sys.exit(1)
        
    print(f"Running black formatter on {modules_dir}...")
    print("This will format both .py files and .ipynb notebooks.\n")
    try:
        # Sử dụng black thông qua python module
        result = subprocess.run(
            [sys.executable, "-m", "black", str(modules_dir)],
            cwd=str(root_dir)
        )
        if result.returncode != 0:
            print("\nFormatting failed or encountered issues.")
            sys.exit(result.returncode)
        else:
            print("\nFormatting completed successfully!")
    except Exception as e:
        print(f"Failed to run black: {e}")
        print("Vui lòng đảm bảo đã cài đặt black hỗ trợ jupyter:")
        print("pip install -r envs/requirements-dev.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
