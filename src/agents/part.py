

class Part:
    def __init__(self, part_type:str= None, weight:float=None, size:list=None) -> None:
        self.part_type = part_type
        self.weight = weight
        self.size = size
    
    def get_weight(self) -> float:
        return self.weight
    
    def get_size(self) -> list:
        return self.size
    
    def __str__(self) -> str:
        return self.part_type