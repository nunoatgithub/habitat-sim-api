from habitat_sim.registry import registry as registry
from habitat_sim.sensor import SensorType as SensorType
from habitat_sim.sensors.noise_models.sensor_noise_model import SensorNoiseModel as SensorNoiseModel
from numpy import ndarray

class SpeckleNoiseModelCPUImpl:
    intensity_constant: float
    mean: int
    sigma: int
    def simulate(self, image: ndarray) -> ndarray: ...

class SpeckleNoiseModel(SensorNoiseModel):
    intensity_constant: float
    mean: int
    sigma: int
    def __attrs_post_init__(self) -> None: ...
    @staticmethod
    def is_valid_sensor_type(sensor_type: SensorType) -> bool: ...
    def simulate(self, image: ndarray) -> ndarray: ...
    def apply(self, image: ndarray) -> ndarray: ...
