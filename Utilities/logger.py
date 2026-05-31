from loguru import logger

logger.add(
    "Logs/execution.log",
    rotation="5 MB"
)