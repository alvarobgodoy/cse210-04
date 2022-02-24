class Participants:
    """A collection of minerals.

    The responsibility of the Participants class is to keep track of a collection of minerals. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _participants (dict): A dictionary of participants { key: group_name, value: a list of participants}
    """
        
    def __init__(self):
        """Constructs a new mineral."""
        self._participants = {'minerals': []}
    
    def add_minerals(self, minerals):
        """Adds a list of minerals to the 'minerals' group in _participants.
        
        Args:
            group (string): The name of the group.
            mineral (mineral): The mineral to add.
        """
        for mineral in minerals:
            if not mineral in self._participants['minerals']:
                self._participants['minerals'].append(mineral)

    def add_participant(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._participants.keys():
            self._participants[group] = []
            
        if not actor in self._participants[group]:
            self._participants[group].append(actor)

    def get_participants(self, group):
        """Gets the participants in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The participants in the group.
        """
        total = []
        if group in self._participants.keys():
            total = self._participants[group].copy()
        return total
    
    def get_all_participants(self):
        """Gets all the participants in participants.
        
        Returns:
            List: All the participants in participants.
        """
        results = []
        for group in self._participants:
            results.extend(self._participants[group])
        return results

    def get_first_participant(self, group):
        """Gets the first participant in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first participant in the group.
        """
        total = None
        if group in self._participants.keys():
            total = self._participants[group][0]
        return total

    def remove_participant(self, group, mineral):
        """Removes a participant from the given group.
        
        Args:
            group (string): The name of the group.
            participant (participant): The participant to remove.
        """
        if group in self._participants:
            self._participants[group].remove(mineral)
