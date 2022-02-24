class Location:
    '''This class is the represents the distance of the origin (0, 0)
    
    The responsibility of Location is to save and provide 
    information about the position of the element that holds this class. 
    
    Attributes:
        _x (interger): The horizontal distance of the origin
        _y (interger): The vertical distance of the origin
    '''
    def __init__(self, x, y):
        ''' Constructs the new location with the given x and y values

        Args:
            x (int): the given x value
            y (int): the given y value
        '''
        self._x = x
        self._y = y

    def add(self, other):
        '''Gets a new location that is the sum of this 
        and the given one
        
        Args:
            other (Location): The location to add.
        
        Returns:
            Location: A new location that is the sum.
            
        '''
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Location(x, y)



    def equals(self, other):
        '''Whether or not yhid Location is equal to the given one.
        
        Args: 
            other (Location): the Location to compare

        Returns:
            boolean: True if both x and y are equal; false if otherwise.

        '''
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        '''Gets the horizontal distance.
        
        Returns:
            interger: The horizontal distance
        '''
        return self._x

    def get_y(self):
        '''Gets the vertical distance.
        
        Returns:
            interger: The vertical distance'''
        return self._y

    def scale(self, factor):
        '''Scales the location by the provided factor.
        
        Args:
            factor (int): The amount to scale.
            
        Returns: 
            Location: A new Location that is called'''
        return Location(self._x * factor, self._y * factor)
 



    