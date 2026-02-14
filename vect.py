from dataclasses import dataclass

@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
print(Vector(1, 2) + Vector(3, 4))
