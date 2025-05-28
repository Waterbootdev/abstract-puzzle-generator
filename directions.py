from normal_vector import NormalVector
class Directions:
    def __init__(self) -> None:
        
        self.x = NormalVector(x=1)
        self.y = NormalVector(y=1)
        self.__rotation = 0
        
    def __repr__(self) -> str:
        return f'[{self.x},{self.y}]'
    
    def rotate_cw(self):
        self.x.rotate_cw()
        self.y.rotate_cw()
        self.decrement_rotation()

    def rotate_ccw(self):
        self.y.rotate_ccw()
        self.x.rotate_ccw()
        self.increment_rotation()

    def increment_rotation(self):
        if self.__rotation == 3:
            self.__rotation = 0
        else:
            self.__rotation += 1
    def decrement_rotation(self):
        if self.__rotation == 0:
            self.__rotation = 3
        else:
            self.__rotation -= 1

    def is_unrotated(self):
        return self.__rotation == 0
         
    def get_rotation(self):
        return self.__rotation