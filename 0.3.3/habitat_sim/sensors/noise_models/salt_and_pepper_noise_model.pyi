from habitat_sim.registry import registry as registry
from habitat_sim.sensor import SensorType as SensorType
from habitat_sim.sensors.noise_models.sensor_noise_model import SensorNoiseModel as SensorNoiseModel
from numpy import ndarray

class SaltAndPepperNoiseModelCPUImpl:
    s_vs_p: float
    amount: float
    def simulate(self, image: ndarray) -> ndarray: ...

class SaltAndPepperNoiseModel(SensorNoiseModel):
    s_vs_p: float
    amount: float
    def __attrs_post_init__(self) -> None: ...
    @staticmethod
    def is_valid_sensor_type(sensor_type: SensorType) -> bool: ...
    def simulate(self, image): ...
    def apply(self, image): ...
