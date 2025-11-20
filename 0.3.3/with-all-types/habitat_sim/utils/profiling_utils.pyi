from _typeshed import Incomplete
from contextlib import ContextDecorator
from habitat_sim.logging import logger as logger

_env_var: Incomplete
_enable_profiling: Incomplete

class _ProfilingHelper:
    step_count: int
    capture_start_step: int
    capture_end_step: int
    range_depth: int

_helper: Incomplete

def configure(capture_start_step: int = -1, num_steps_to_capture: int = -1) -> None: ...
def on_start_step() -> None: ...
def range_push(msg: str) -> None: ...
def range_pop() -> None: ...

class RangeContext(ContextDecorator):
    _msg: Incomplete
    def __init__(self, msg: str) -> None: ...
    def __enter__(self) -> RangeContext: ...
    def __exit__(self, *exc) -> None: ...
