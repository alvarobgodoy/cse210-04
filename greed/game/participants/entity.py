from game.common.color import Color
from game.common.location import Location


class Entity:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of entity is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Location): The screen coordinates.
        _velocity (Location): The speed and direction.
    """

    def __init__(self):
        """Constructs a new entity."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Location(0, 0)
        self._velocity = Location(0, 0)

    def get_color(self):
        """Gets the entity's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The entity's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the entity's font size.
        
        Returns:
            Location: The entity's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the entity's position in 2d space.
        
        Returns:
            Location: The entity's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the entity's textual representation.
        
        Returns:
            string: The entity's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the entity's speed and direction.
        
        Returns:
            Location: The entity's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the entity to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Location(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Location): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Location): The given velocity.
        """
        self._velocity = velocity