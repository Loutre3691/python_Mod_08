import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix}")
        print(f"Environment Path: {os.environ.get('VIRTUAL_ENV')}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting"
              " the global system.\n")
        print(f"Package installation path: {site.getsitepackages()}")

    else:
        print("MATRIX STATUS: You're still plugged in")
