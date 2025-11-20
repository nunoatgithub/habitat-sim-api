import abc
from habitat_sim.sensor import SensorType as SensorType
from numpy import ndarray as ndarray
from torch import Tensor as Tensor

class SensorNoiseModel(abc.ABC):
    gpu_device_id: int | None
    @staticmethod
    @abc.abstractmethod
    def is_valid_sensor_type(sensor_type: SensorType) -> bool: ...
    @abc.abstractmethod
    def apply(self, sensor_observation): ...
    def __call__(self, sensor_observation: ndarray | Tensor) -> ndarray | Tensor: ...
