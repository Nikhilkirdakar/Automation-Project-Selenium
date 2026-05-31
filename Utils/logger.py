from loguru import logger
import os

os.makedirs('Logs', exist_ok=True)
logger.add(
    "Logs/execution.log",
    rotation="5 MB"
)
