import habitat_sim
from _typeshed import Incomplete
from typing import Any

class SemanticDisplay:
    sim: Incomplete
    semantic_region_debug_draw_choices: Incomplete
    semantic_region_debug_draw_state: int
    debug_semantic_colors: Incomplete
    def __init__(self, sim: habitat_sim.simulator.Simulator) -> None: ...
    def cycle_semantic_region_draw(self): ...
    def draw_region_debug(self, debug_line_render: Any) -> None: ...
