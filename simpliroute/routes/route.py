from dataclasses import dataclass, field

from simpliroute.abstract.abstract_dataclass import  AbstractSimplirouteV1Dataclass   
from dataclasses_json import dataclass_json, config

@dataclass_json
@dataclass
class Route(AbstractSimplirouteV1Dataclass):
    endpoint:str = field(default='routes', metadata=config(exclude=lambda x: True))
    ... 
    