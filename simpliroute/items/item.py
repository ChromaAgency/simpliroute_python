from dataclasses import dataclass   

@dataclass
class Item:
    id: int
    title: str
    load: float
    reference: str
    quantity_planned: float
    
    status: str = ""
    load_2: float = 0
    load_3: float = 0
    notes: str = ""
    quantity_delivered: float = 0