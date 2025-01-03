import logging
import traceback
import sys

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),  # Logs to a file named 'debug.log'
        logging.StreamHandler(sys.stdout)  # Also outputs logs to the console
    ]
)

# Function to log errors with traceback
def log_error(exception):
    logging.error("An error occurred: %s", str(exception))
    logging.error("Traceback:\n%s", traceback.format_exc())

try:
    
    result = 10 / 0  
except Exception as e:
    log_error(e)

#  Logging various points in the code
logging.info("Starting face preprocessing step...")
# Your face preprocessing code
logging.info("Face preprocessing completed successfully.")

logging.info("Starting voice manipulation...")
# Your voice manipulation code
logging.info("Voice manipulation completed successfully.")
