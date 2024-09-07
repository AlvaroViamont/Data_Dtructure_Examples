from agents.part import Part

class Product:
    def __init__(self, parts:list=None, time:int=0) -> None:
        self.parts = parts
        self.time = time
        self.weight = None
        self.size = None
    
    def add_part(self, part:Part):
        self.parts.append(part)
    
    def get_weight(self) -> float:
        if self.parts:
            self.weight = 0
            for part in self.parts:
                self.weight = self.weight + part.weight
        return self.weight
    
    def get_size(self) -> list:
        if self.parts:
            self.size = [0, 0, 0]
            for part in self.parts:
                self._compare_size(part)
        return self.size
    
    def _compare_size(self, part:Part) -> None:
        for i in range(3):
            if self.size[i] < part.size[i]:
                self.size.pop(i)
                self.size.insert(i, part.size[i])
    
    def get_time(self) -> int:
        return self.time
    
    def get_part_list(self) -> list:
        if self.parts:
            return self.parts
        return None
    
    def search_part(self, part:Part):
        if self.parts:
            for local_part in self.parts:
                if local_part.part_type == part.part_type:
                    return local_part
        return None