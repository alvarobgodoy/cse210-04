import random
from game.participants.mineral import Mineral
from game.common.location import Location
from game.common.color import Color

class Waterfall:
    '''The reponsability of the Waterfall class is to have the functionality that makes all the objects fall like a waterfall.

    Attributes:
        _columns (int): The number of columns.
        _rows (int): The number of rows.
        _cell_size (int): The size of each cell.
        _font_size (int): Font size.
        _gem_color (Color): A color object for the gems.
        _rock_color (Color): A color object for the rocks.
    '''
    def __init__(self, columns, rows, cell_size, font_size):
        """Constructs a new Waterfall.
        
        Args:
            columns (int): Current number of columns.
            rows (int): Current number of rows.
            cell_size (int): Current size of each cell.
            font_size (int): Current font size.
        """
        self._columns = columns
        self._rows = rows
        self._cell_size = cell_size
        self._font_size = font_size
        self._gem_color = Color(0, 255, 0)
        self._rock_color = Color(163, 163, 194)

    
    def generate_line(self):
        '''Generates an return a list of mineral objects and puts them at the top of the screen, with an random x coordinate. It could return an empty list.

        Returns:
            minerals (list): a list of mineral objects, it could contain 0 to 6 objects.
        '''
        # n is the number of objects that will be created
        n = random.randint(0, 6)
        icons = ['*', 'o']

        # create an empty list to store the objects
        minerals = []

        if n != 0:
            for _ in range(n):
                # Determine the type (rock or gem)
                chosen_icon = random.choice(icons)

                # Randomly select the x location
                x = random.randint(1, self._columns - 1)
                position = Location(x, 1)
                position = position.scale(self._cell_size)

                # Creation and configuration of the mineral
                mineral = Mineral()
                mineral.set_text(chosen_icon)
                mineral.set_font_size(self._font_size)
                if mineral.get_text() == '*':
                    mineral.set_points(100)
                    mineral.set_color(self._gem_color)
                elif mineral.get_text() == 'o':
                    mineral.set_points(-100)
                    mineral.set_color(self._rock_color)
                mineral.set_position(position)

                # Add the mineral to the group
                minerals.append(mineral)
        
        return minerals
                

    def remove_last_line(self, participants):
        '''Chekcs every mineral, if it's in the last row then it gets destroyed.

        Args:
            participants (Participants): the used instance of the Participants class.
        '''
        # get all the participants from the minerals category
        for mineral in participants.get_actors('minerals'):
            # get its y position
            position = mineral.get_position()
            y = position.get_y()
            # if the y position is in the last row then it gets removed
            if y == self._rows:
                participants.remove_actor('minerals', mineral)


    def move_down(self, participants, max_x, max_y):
        '''Moves every mineral 1 cell down in the y axis.

        Args:
            participants (Participants): the used instance of the Participants class.
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        '''
        # get all the participants from the minerals category
        for mineral in participants.get_actors('minerals'):
            # get its position
            position = mineral.get_position()
            x = position.get_x()
            y = position.get_y()
            # set its velocity to +1 in the y axis
            velocity = Location(x, y + 1)
            mineral.set_velocity(velocity)
            # moves the mineral
            mineral.move_next(max_x, max_y)