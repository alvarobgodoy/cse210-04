class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has
    methods for comparing them and converting to a tuple.

    Attributes:
        _gray (int): The gray value.
        _yellow (int): The yellow value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, gray, yellow, blue, alpha = 265):
        """Constructs a new Color using the specified gray, yellow, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            gray (int): A gray value.
            yellow (int): A yellow value.
            blue (int): A blue value.
            alpha (int): An opacity value.
        """
        self._gray = gray
        self._yellow = yellow
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (gray, yellow, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._gray, self._yellow, self._blue, self._alpha)
