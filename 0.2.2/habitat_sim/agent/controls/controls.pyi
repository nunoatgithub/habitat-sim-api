import abc
from habitat_sim import bindings as hsim

class ActuationSpec:
    amount: float
    constraint: float | None

class SceneNodeControl(abc.ABC):
    body_action: bool
    @abc.abstractmethod
    def __call__(self, scene_node: hsim.SceneNode, acutation_spec: ActuationSpec) -> None: ...
