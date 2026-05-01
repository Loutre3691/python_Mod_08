import sys
import os
import site


virtual_env = os.environ.get('VIRTUAL_ENV')
venv_name = os.path.basename(virtual_env) if virtual_env else "None detected"

if sys.prefix != sys.base_prefix:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting"
          " the global system.\n")

    print(f"Package installation path: {site.getsitepackages()[0]}")

else:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}\n")

    print("""WARNING: You're in the global environment!)
The machines can see everything you install.\n
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows\n
Then run this program again.""")
