from dataclasses import dataclass   

@dataclass
class Item:
    id: int
    title: str
    status: str
    load: None
    load_2: None
    load_3: float
    reference: str
    notes: str
    quantity_planned: float
    quantity_delivered: float 
    