# Constants for paths
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Path Executable
EXEC_PATH = BASE_DIR/"executables"


# Path Drivers: Firefox
FIREFOX_DRIVER_DIR_LINUX = EXEC_PATH/"linux"
FIREFOX_DRIVER_DIR_WINDOWS = EXEC_PATH/"windows"

FIREFOX_DRIVER_LINUX = FIREFOX_DRIVER_DIR_LINUX/"geckodriver"
FIREFOX_DRIVER_WINDOWS = FIREFOX_DRIVER_DIR_WINDOWS/"geckodriver.exe"
