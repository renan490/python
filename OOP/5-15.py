import math

class Vector2:
    
    def __init__(self, x=0, y=0):        
        self.x = x
        self.y = y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
        
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
        
    def from_points(P1, P2):
        print("1")        
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )
    
    def get_magnitude(self):
        print("2")
        return math.sqrt( self.x**2 + self.y**2 )
        
    def normalize(self):
        print("3")
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
        
    def __add__(self, rhs):
        print("4")         
        return Vector2(self.x + rhs.x, self.y + rhs.y)
        
    def __sub__(self, rhs):
        print("5")
        return Vector2(self.x - rhs.x, self.y - rhs.y)
        
    def __neg__(self):
        return Vector2(-self.x, -self.y)
        
    def __mul__(self, scalar):
        print("6")
        return Vector2(self.x * scalar, self.y * scalar)
        
    def __truediv__(self, scalar):
        print("7")
        return Vector2(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        print("8")
        return self._v[index]

    def __setitem__(self, index, value):
        print("9")
        print("Aqui!")
        self._v[index] = 1.0 * value

            
if __name__ == "__main__":     
    A = (10.0, 20.0)
    B = (30.0, 35.0)
    AB = Vector2.from_points(A, B)
    step = AB * .1
    #position = Vector2(A) não funciona, pois A é uma tupla.
    position = Vector2(*A)
    for n in range(10):
        position += step
        print(position)
