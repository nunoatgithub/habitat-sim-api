from habitat_sim import bindings as hsim
from typing import Dict

class SensorSuite(Dict[str, hsim.Sensor]):
    def add(self, sensor: hsim.Sensor) -> None: ...
