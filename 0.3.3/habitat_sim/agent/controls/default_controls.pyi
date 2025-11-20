from habitat_sim.agent.controls.controls import ActuationSpec as ActuationSpec, SceneNodeControl as SceneNodeControl
from habitat_sim.geo import FRONT as FRONT
from habitat_sim.registry import registry as registry
from habitat_sim.scene import SceneNode as SceneNode

class MoveBackward(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class MoveForward(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class MoveRight(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class MoveLeft(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class MoveUp(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class MoveDown(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class LookLeft(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class LookRight(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class LookUp(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class LookDown(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class RotateSensorClockwise(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...

class RotateSensorAntiClockwise(SceneNodeControl):
    def __call__(self, scene_node: SceneNode, actuation_spec: ActuationSpec) -> None: ...
