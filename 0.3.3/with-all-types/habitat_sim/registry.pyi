from _typeshed import Incomplete
from typing import DefaultDict, Type

__all__: Incomplete

def _camel_to_snake(name): ...

class _Registry:
    _mapping: DefaultDict[str, dict]
    @classmethod
    def register_move_fn(cls, controller: Type | None = None, *, name: str | None = None, body_action: bool | None = None): ...
    @classmethod
    def register_noise_model(cls, noise_model: Type | None = None, *, name: str | None = None): ...
    @classmethod
    def _get_impl(cls, _type, name: str): ...
    @classmethod
    def get_move_fn(cls, name: str): ...
    @classmethod
    def get_noise_model(cls, name: str): ...

registry: Incomplete
