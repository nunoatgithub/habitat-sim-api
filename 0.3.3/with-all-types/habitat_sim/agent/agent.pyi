import magnum as mn
import numpy as np
import quaternion as qt
from .controls import ActuationSpec as ActuationSpec, ObjectControls as ObjectControls
from _typeshed import Incomplete
from habitat_sim import bindings as hsim
from habitat_sim._ext.habitat_sim_bindings import SceneNode as SceneNode
from habitat_sim.sensors.sensor_suite import SensorSuite as SensorSuite
from habitat_sim.utils.common import quat_from_coeffs as quat_from_coeffs, quat_from_magnum as quat_from_magnum, quat_rotate_vector as quat_rotate_vector, quat_to_magnum as quat_to_magnum
from habitat_sim.utils.validators import NoAttrValidationContext as NoAttrValidationContext, all_is_finite as all_is_finite, is_unit_length as is_unit_length, value_is_validated as value_is_validated
from typing import Any, Dict, List

__all__: Incomplete

class ActionSpec:
    name: str
    actuation: ActuationSpec | None

def _default_action_space() -> Dict[str, ActionSpec]: ...
def _triple_zero() -> np.ndarray: ...
def _default_quaternion() -> qt.quaternion: ...

class SixDOFPose:
    position: np.ndarray
    rotation: qt.quaternion | List

class AgentState:
    position: np.ndarray
    rotation: qt.quaternion | List | np.ndarray
    sensor_states: Dict[str, SixDOFPose]

class AgentConfiguration:
    height: float
    radius: float
    sensor_specifications: List[hsim.SensorSpec]
    action_space: Dict[Any, ActionSpec]
    body_type: str

class Agent:
    agent_config: AgentConfiguration
    _sensors: SensorSuite
    controls: ObjectControls
    body: mn.scenegraph.AbstractFeature3D
    initial_state: Incomplete
    def __init__(self, scene_node: hsim.SceneNode, agent_config: AgentConfiguration | None = None, _sensors: SensorSuite | None = None, controls: ObjectControls | None = None) -> None: ...
    def reconfigure(self, agent_config: AgentConfiguration, reconfigure_sensors: bool = True) -> None: ...
    def _add_sensor(self, spec: hsim.SensorSpec, modify_agent_config: bool = True) -> None: ...
    def act(self, action_id: Any) -> bool: ...
    def get_state(self) -> AgentState: ...
    def set_state(self, state: AgentState, reset_sensors: bool = True, infer_sensor_states: bool = True, is_initial: bool = False) -> None: ...
    @property
    def scene_node(self) -> SceneNode: ...
    @property
    def state(self): ...
    @state.setter
    def state(self, new_state: AgentState): ...
    def close(self) -> None: ...
