from dataclasses import asdict, dataclass, field
from typing import List

from simpliroute.abstract.abstract_dataclass import  AbstractSimplirouteV1Dataclass
from simpliroute.config.config import ConfigV1   
import requests
from dataclasses_json import dataclass_json, config
from simpliroute.items.item import Item

@dataclass_json
@dataclass
class Visit(AbstractSimplirouteV1Dataclass):
    id: int
    order: None
    tracking_id: str
    status: str
    title: str
    address: str
    latitude: str
    longitude: str
    load: float
    load_2: float
    load_3: float
    window_start: None
    window_end: None
    window_start_2: None
    window_end_2: None
    duration: str
    contact_name: str
    contact_phone: str
    contact_email: None
    reference: str
    notes: str
    skills_required: list
    skills_optional: list
    tags: list
    planned_date: str
    programmed_date: None
    route: None
    estimated_time_arrival: None
    estimated_time_departure: None
    checkin_time: None
    checkout_time: None
    checkout_latitude: None
    checkout_longitude: None
    checkout_comment: str
    checkout_observation: None
    signature: None
    pictures: list
    created: str
    modified: str
    eta_predicted: str
    eta_current: str
    priority: bool
    has_alert: bool
    priority_level: None
    extra_field_values: None
    geocode_alert: None
    visit_type: None
    current_eta: None
    fleet: None
    # Should change later to a Property object
    # properties: any
    
    on_its_way: None
    title:str 
    items:List[Item] = field(default_factory=list) 
    endpoint:str = field(default='routes/visits', metadata=config(exclude=lambda x: True))
    
    def create(self):
        """Podes usar este para convertirlo a json, habria que ver si algun campo no jode."""
        response = requests.post(self.endpoint_url, json=self.to_json(), headers=self.config.headers)
        ... 
    
    @classmethod
    def update(cls, config:ConfigV1, visit_id:str, update_data:dict):
        update_url = config.get_endpoint(f"{cls.endpoint}/{visit_id}")
        ...

    @classmethod
    def delete(cls, config:ConfigV1, visit_id:str):
        delete_url = config.get_endpoint(f"{cls.endpoint}/{visit_id}")
        ...
    
    @classmethod
    def get(cls, config:ConfigV1, visit_id:str) -> 'Visit':
        """ Te dejo como ejemplo este. 
        Usamos un archivo config, que le vamos a pasar a los object, con ese sacamos token, headers y endpoint. Este endpoint ya genera la visita perfectamente.
        """
        response = requests.get(config.get_endpoint(f"{cls.endpoint}/{visit_id}"), headers=config.headers)        
        return cls.from_dict({"config":config, **response.json()})
    

    
        