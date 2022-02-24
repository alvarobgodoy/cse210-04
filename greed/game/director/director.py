class Director:
    '''The one who directs the game 
    
    It gives the directions about what, which and when something has to act in the right moment

    Attributes:
        _movement (Movement): An instance of Movement.
        _graphics (Graphics): An instance of Graphics.
        _waterfall (Waterfall): An instance of Waterfall.
    
    '''
    def __init__(self, movement, graphics, waterfall):
        '''Constructs a new Director using the specified movement and graphic services
        
        Args:
            movement (Movement): An instance of Movement.
            graphics (Graphics): An instance of Graphics.
            waterfall (Waterfall): An instance of Waterfall.
        '''
        self._points = 0
        self._waterfall = waterfall
        self._graphics = graphics
        self._movement = movement


    def start_game(self, participants):
        """Starts the main game loop.

        Args:
            participants (Participants): All the participants.
        """
        self._graphics.open_window()
        while self._graphics.is_window_open():
            self._get_inputs(participants)                    
            self._do_updates(participants)                
            self._do_outputs(participants)
        self._graphics.close_window()


    def _get_inputs(self, participants):
        """Gets directional input from the keyboard and applies it to the excavator.
        
        Args:
            participants (Participants): All the participants.
        """
        excavator = participants.get_first_participant('excavators')
        velocity = self._movement.get_direction()
        excavator.set_velocity(velocity)


    def _do_updates(self, participants):
        """Updates the excavator's position and resolves any collisions with entities.
        
        Args:
            participants (Participants): All the participants.
        """       
        generated_minerals = self._waterfall.generate_line()
        participants.add_minerals(generated_minerals)
        banner = participants.get_first_participant('banners')
        excavator = participants.get_first_participant('excavators')
        minerals = participants.get_participants('minerals')

        max_x = self._graphics.get_width()
        max_y = self._graphics.get_height()

        for mineral in minerals:
            if excavator.get_position().equals(mineral.get_position()):
                mineral_points = mineral.get_points()
                self._points += mineral_points
                participants.remove_participant('minerals', mineral)
        banner.set_text(f'Score: {self._points}')

        self._waterfall.move_down(participants, max_x, max_y)
        excavator.move_next(max_x, max_y)

        self._waterfall.remove_last_line(participants)

    def _do_outputs(self, participants):
        """Draws the entities on the screen.
        
        Args:
            participants (Participants): All the participants.
        """     
        self._graphics.clear_buffer()
        entities = participants.get_all_participants()
        self._graphics.draw_participants(entities)
        self._graphics.flush_buffer()