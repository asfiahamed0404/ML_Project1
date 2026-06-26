import logging
import os
import sys
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(LOG_DIR, LOG_FILE)

LOG_FORMAT = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

# Console stream that won't crash on Windows cp1252 when emojis are emitted
_utf8_stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1, closefd=False) if hasattr(sys.stdout, "fileno") else sys.stdout

logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file_path, encoding="utf-8"),
        logging.StreamHandler(_utf8_stdout),
    ],
)


if __name__ == "__main__":
    logging.info("Logging has started.")