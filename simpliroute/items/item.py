from dataclasses import dataclass   

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
    quantity_delivered: float = 0

    @classmethod
    def to_dict(self, items):
        item_list = []
        for item in self:
            item_dict = {
                'title':item.title,
                'load':item.load,
                'reference':item.reference,
                'quantity_planned':item.quantity_planned,
                'status':item.status,
                'load_2':item.load_2,
                'load_3':item.load_3,
                'notes':item.notes,
                'quantity_delivered':item.quantity_delivered
            }
            item_list.append(item_dict)
        return item_list