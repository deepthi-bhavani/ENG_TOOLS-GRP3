
import sys
import platform
import os

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Operating system:", platform.system())
print("Current working directory:", os.getcwd())
print("Virtual environment:", os.environ.get("VIRTUAL_ENV", "Not detected"))
