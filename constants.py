# Constans for paths
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Path Executable
EXEC_PATH = BASE_DIR/"executables"
CHROME_DRIVER = EXEC_PATH/"chromedriver"