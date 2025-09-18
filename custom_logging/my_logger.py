import logging
import os 
from datetime import datetime


LOG_DIR = os.path.join(os.getcwd(),"logs")

os.makedirs(LOG_DIR,exist_ok=True)



#create unique log file names
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE)


# Logging configuration
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



logger = logging.getLogger("my_agentic_app")