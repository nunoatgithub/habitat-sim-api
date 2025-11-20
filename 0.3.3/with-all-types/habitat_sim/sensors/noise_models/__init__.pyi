from _typeshed import Incomplete
from habitat_sim.registry import registry as registry
from habitat_sim.sensors.noise_models.gaussian_noise_model import GaussianNoiseModel as GaussianNoiseModel
from habitat_sim.sensors.noise_models.no_noise_model import NoSensorNoiseModel as NoSensorNoiseModel
from habitat_sim.sensors.noise_models.poisson_noise_model import PoissonNoiseModel as PoissonNoiseModel
from habitat_sim.sensors.noise_models.redwood_depth_noise_model import RedwoodDepthNoiseModel as RedwoodDepthNoiseModel
from habitat_sim.sensors.noise_models.salt_and_pepper_noise_model import SaltAndPepperNoiseModel as SaltAndPepperNoiseModel
from habitat_sim.sensors.noise_models.sensor_noise_model import SensorNoiseModel as SensorNoiseModel
from habitat_sim.sensors.noise_models.speckle_noise_model import SpeckleNoiseModel as SpeckleNoiseModel
from typing import Any, Dict

def make_sensor_noise_model(name: str, kwargs: Dict[str, Any]) -> SensorNoiseModel: ...

__all__: Incomplete
