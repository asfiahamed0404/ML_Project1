import logging         #to write log messages
import os                           #to handle file paths and directories
from datetime import datetime         #to get the current date and time for log file naming

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path to logs directory, eg-C:\Users\Asfi\project
logs_dir = os.path.join(os.getcwd(), "logs")

# Create logs directory if it doesn't exist,A folder named logs is inside your project folder
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file,  eg- "C:\Users\Asfi\project\logs\02_14_2026_18_35_20.log"
log_file_path = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,               # Path to the log file where messages will be saved
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  
                                          # Format of each log line:
                                          # %(asctime)s → timestamp
                                          # %(lineno)d → line number in code
                                          # %(name)s → logger name (usually 'root' by default)
                                          # %(levelname)s → log level (INFO, ERROR, etc.)
                                          # %(message)s → the actual log message
    level=logging.INFO                    # Minimum severity level to log (INFO and above)
)

if __name__ == "__main__":
    logging.info("Logging has started.")