import torch
from habitat_sim.registry import registry as registry
from habitat_sim.sensor import SensorType as SensorType
from habitat_sim.sensors.noise_models.sensor_noise_model import SensorNoiseModel as SensorNoiseModel
from numpy import ndarray as ndarray

class NoSensorNoiseModel(SensorNoiseModel):
    @staticmethod
    def is_valid_sensor_type(sensor_type: SensorType) -> bool: ...
    def apply(self, x: ndarray | torch.Tensor) -> ndarray | torch.Tensor: ...
