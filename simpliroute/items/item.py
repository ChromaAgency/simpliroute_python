from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from simpliroute.config.config import ConfigV1
import requests
@dataclass_json
@dataclass
class Item:
    id: int
    title: str
    load: float
    reference: str
    quantity_planned: float
    
    status: str = "pending"
    load_2: float = 0
    load_3: float = 0
    notes: str = ""
    quantity_delivered: float = field(default=None, metadata=config(exclude=lambda x: not x))

    @classmethod    
    def update_items(cls, config:ConfigV1, visit_id:str, update_data:dict):
        update_url = config.get_endpoint(f"{cls.endpoint}/{visit_id}/items")
        response = requests.put(update_url,json=update_data, headers=config.headers)
        return response