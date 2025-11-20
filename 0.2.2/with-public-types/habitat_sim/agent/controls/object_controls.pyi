from habitat_sim import bindings as hsim
from habitat_sim.agent.controls.controls import ActuationSpec as ActuationSpec
from habitat_sim.registry import registry as registry
from typing import Callable

EPS: float

class ObjectControls:
    move_filter_fn: Callable[[_3d_point, _3d_point], _3d_point]
    @staticmethod
    def is_body_action(action_name: str): ...
    def action(self, obj: hsim.SceneNode, action_name: str, actuation_spec: ActuationSpec, apply_filter: bool = True) -> bool: ...
    def __call__(self, obj: hsim.SceneNode, action_name: str, actuation_spec: ActuationSpec, apply_filter: bool = True): ...
