
class Tile:
    def __init__(sekf)

class Area:
    """Mapping out an area with a horizontal and vertical value."""
    def __init__(self, h, v, area_type=None):
        self.h = h
        self.v = v
        self.area_type = area_type
        
        self.create_area()
        
    def create_area(self):
        self.grid = [[
            (x, y)
            for x in range(self.h)]
                for y in range(self.v)        
        ]

        
for n in Area(10,10).grid:
    print n
