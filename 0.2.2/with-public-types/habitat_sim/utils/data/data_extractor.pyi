from _typeshed import Incomplete
from habitat_sim.agent.agent import AgentConfiguration as AgentConfiguration, AgentState as AgentState
from habitat_sim.utils.data.data_structures import ExtractorLRUCache as ExtractorLRUCache
from habitat_sim.utils.data.pose_extractor import PoseExtractor as PoseExtractor, TopdownView as TopdownView
from typing import Callable, List

def make_pose_extractor(name: str) -> Callable[..., PoseExtractor]: ...

class ImageExtractor:
    scene_filepaths: Incomplete
    cur_fp: Incomplete
    labels: Incomplete
    img_size: Incomplete
    cfg: Incomplete
    sim: Incomplete
    meters_per_pixel: Incomplete
    tdv_fp_ref_triples: Incomplete
    pose_extractor: Incomplete
    poses: Incomplete
    mode: str
    mode_to_data: Incomplete
    instance_id_to_name: Incomplete
    out_name_to_sensor_name: Incomplete
    output: Incomplete
    use_caching: Incomplete
    cache: Incomplete
    def __init__(self, scene_filepath: str | List[str], labels: List[float] = None, img_size: tuple = (512, 512), output: List[str] = None, pose_extractor_name: str = 'closest_point_extractor', sim: Incomplete | None = None, shuffle: bool = True, split: tuple = (70, 30), use_caching: bool = True, meters_per_pixel: float = 0.1) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
    def close(self) -> None: ...
    def set_mode(self, mode: str) -> None: ...
    def get_semantic_class_names(self) -> List[str]: ...
