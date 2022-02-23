# well... this is the class named director

from game.services.waterfall import Waterfall

class Director:
    '''The one who directs the game 
    
    It gives the directions about what, which and when something has to act in the right moment

    Attributes:
        _keyboard_service
        _video_service
    
    '''
    def __init__(self, keyboard_service, video_service):
        '''Constructs a new Director using the specified movement and graphic services
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService
            video_service (VideoService): An instance of VideoService           
        '''
        self._points = 0
        self._waterfall = Waterfall()

        self._video_service = video_service
        self._keyboard_service = keyboard_service


    def start_game(self, participants):
        '''Starts the the game using the given participants. Runs 
        the main game loop
        
        Args:
            participants (Participants): the group of all the participants
        '''
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self.get_inputs(participants)                    
            self.do_updates(participants)                
            self.do_outputs(participants)
        self._video_service.close_window()


    def get_inputs(self, participants):
        '''Gets the directions from the inputs of the user 
        from the keyboard
        
        Args:
            participants (Participants): the group of all the participants'''
        excavator = participants.get_first_participant('excavator')
        velocity = self._keyboard_service.get_direction()
        excavator.set_velocity(velocity)


    def do_updates(self, participants):
        '''Updates the participant positions and resolves any collitions 
        between the excavator and the minerals
        
        Args:
            participants (Participants): the group of all the participants'''        
        banner = participants.get_participants('banner')
        excavator = participants.get_first_participant('excavator')
        minerals = participants.get_participants('minerals')

        banner.set_text('')
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        excavator.move_next(self._max_x)


        self._waterfall.generate_line()
        self._waterfall.move_down(participants, max_x, max_y)
        self._waterfall.remove_last_line(participants)

        for mineral in minerals:
            if excavator.get_position().equals(mineral.get_position()):
                mineral_points = mineral.get_points()
                self._points += mineral_points
                participants.remove_actor(mineral, 'minerals')
        banner.set_text(f'Score: {self._points}')
            



    def do_outputs(self, participants):
        '''Draws the participants on the screen 
        
        Args:
            participants (Participants): the group of all the participants'''     

        self._video_service.clear_buffer()
        entities = participants.get_all_minerals()
        self._video_service(entities)
        self._video_service.flush_buffer()






