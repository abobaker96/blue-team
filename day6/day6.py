import psutil
import time
from logger import logger

THRESHOLD = 3
SECOND = 10
vals = []


while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    logger.info(f"processor consumption now: {cpu_percent}%")
    if cpu_percent > THRESHOLD:
        logger.warning("processor consumption higt:alert!")
    time.sleep(SECOND)