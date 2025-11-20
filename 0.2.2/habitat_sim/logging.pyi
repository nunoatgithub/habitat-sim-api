import logging
from _typeshed import Incomplete
from habitat_sim._ext.habitat_sim_bindings.core import LoggingContext as LoggingContext
from logging import LogRecord

DEBUG: Incomplete
INFO: Incomplete
WARNING: Incomplete
WARN: Incomplete
ERROR: Incomplete
FATAL: Incomplete
logger: Incomplete
handler: Incomplete

def format_message(record: LogRecord) -> str: ...

class HabitatSimFormatter(logging.Formatter):
    def format(self, record: LogRecord) -> str: ...
