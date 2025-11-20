import numpy as np
from _typeshed import Incomplete
from attr import Attribute
from habitat_sim import bindings as hsim
from habitat_sim.agent.controls.controls import ActuationSpec as ActuationSpec, SceneNodeControl as SceneNodeControl
from habitat_sim.registry import registry as registry
from numpy import ndarray
from typing import Any, List, Sequence, Tuple

class _TruncatedMultivariateGaussian:
    mean: np.ndarray
    cov: np.ndarray
    def __init__(self, mean: Sequence, cov: Sequence) -> None: ...
    def sample(self, truncation: List[Tuple[Any | None, Any | None] | None] | None = None) -> ndarray: ...

class MotionNoiseModel:
    linear: _TruncatedMultivariateGaussian
    rotation: _TruncatedMultivariateGaussian

class ControllerNoiseModel:
    linear_motion: MotionNoiseModel
    rotational_motion: MotionNoiseModel

class RobotNoiseModel:
    ILQR: ControllerNoiseModel
    Proportional: ControllerNoiseModel
    Movebase: ControllerNoiseModel
    def __getitem__(self, key: str) -> ControllerNoiseModel: ...

pyrobot_noise_models: Incomplete

class PyRobotNoisyActuationSpec(ActuationSpec):
    robot: str
    def check_robot(self, attribute: Attribute, value: str) -> None: ...
    controller: str
    def check_controller(self, attribute: Attribute, value: str) -> None: ...
    noise_multiplier: float

class PyrobotNoisyMoveBackward(SceneNodeControl):
    def __call__(self, scene_node: hsim.SceneNode, actuation_spec: ActuationSpec) -> None: ...

class PyrobotNoisyMoveForward(SceneNodeControl):
    def __call__(self, scene_node: hsim.SceneNode, actuation_spec: ActuationSpec) -> None: ...

class PyrobotNoisyTurnLeft(SceneNodeControl):
    def __call__(self, scene_node: hsim.SceneNode, actuation_spec: ActuationSpec) -> None: ...

class PyrobotNoisyTurnRight(SceneNodeControl):
    def __call__(self, scene_node: hsim.SceneNode, actuation_spec: ActuationSpec) -> None: ...
