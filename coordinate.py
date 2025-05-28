from directions import Directions
class Coordinate:    
    def __init__(self) -> None:
        self.index = 0
        self.x = 0
        self.y = 0
    def __repr__(self) -> str:
        return f"[{self.index}, [{self.x}, {self.y}]]"
   
    def right(self, directions:Directions):
        return directions.x.add_to(self.x, self.y)
    
    def left(self, directions:Directions):
        return directions.x.subtract_from(self.x, self.y)
    
    def up(self, directions:Directions):
        return directions.y.subtract_from(self.x, self.y)
    
    def down(self, directions:Directions):
        return directions.y.add_to(self.x, self.y)
    
    def step_right(self, directions:Directions):
        self.index += 1
        self.x, self.y = self.right(directions)
    
    def step_left(self, directions:Directions):
        self.index -= 1
        self.x, self.y = self.left(directions)
    
    def step_right_down(self, directions:Directions):
        self.x, self.y = self.right(directions)
        self.x, self.y = self.down(directions)

    
      


        
    
