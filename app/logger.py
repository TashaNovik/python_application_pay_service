
import logging
import structlog
from logging.config import dictConfig
from typing import TYPE_CHECKING, cast
from app.config import settings


if TYPE_CHECKING:
    from structlog.typing import EventDict, Processor, WrappedLogger


def configure_logger(
        enable_json_logs: bool = False,
        enable_sql_logs: bool = False,
        level: int | str = logging.INFO
) -> None:
    processors: list[Processor] = [
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.contextvars.merge_contextvars,
        structlog.processors.format_exc_info
        #structlog.stdlib.
    ]

    structlog.configure(
        processors=processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter],

    )

base_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": structlog.stdlib.ProcessorFormatter,
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
     },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        }
    }
}

dictConfig(base_config)
#
#     #DEBUG =10
#     #INFO =20
#     #WARNING =30
#     #ERROR =40
#     #CRITICAL =50

