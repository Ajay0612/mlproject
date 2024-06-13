import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # file name created will be in this format (text file)
logs_path = os.path.join(os.getcwd(),"logs") # Giving path to the logs ( to create log folder)
os.makedirs(logs_path, exist_ok=True) # making directories , exist ok true to create more and more even if there are already present

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # making the log file path

'''
Giving the file configuration for the files. 
'''

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, #incase of info only i can print the particular message
)

