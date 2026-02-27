import logging
from typing import Union

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def log_message(text: str, level: Union[str, int] = 'INFO') -> None:
    if isinstance(level, str):
        level = level.upper()
        level = getattr(logging, level, logging.INFO)
    logging.log(level, text)


def setup_logging(level: Union[str, int] = 'DEBUG') -> None:
    logging.basicConfig(
        handlers=[InterceptHandler()],
        level=logging.getLevelName(level)
    )

    aiogram_logger = logging.getLogger('aiogram')
    aiogram_logger.setLevel(logging.ERROR)
