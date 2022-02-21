class Participants:
    """A collection of minerals.

    The responsibility of the Participants class is to keep track of a collection of minerals. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _minerals (dict): A dictionary of minerals { key: group_name, value: a list of minerals }
    """
        
    def __init__(self):
        """Constructs a new mineral."""
        self._minerals = {}
    
    def add_minerals(self, group, mineral):
        """Adds a mineral to the given group.
        
        Args:
            group (string): The name of the group.
            mineral (mineral): The mineral to add.
        """
        if not group in self._minerals.keys():
            self._minerals[group] = []
            
        if not mineral in self._minerals[group]:
            self._minerals[group].append(mineral)

    def get_minerals(self, group):
        """Gets the minerals in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The minerals in the group.
        """
        total = []
        if group in self._minerals.keys():
            total = self._minerals[group].copy()
        return total
    
    def get_all_minerals(self):
        """Gets all the minerals in participants.
        
        Returns:
            List: All the minerals in participants.
        """
        total = []
        for group in self._minerals:
            total.extend(self._minerals[group])
        return total

    def get_first_mineral(self, group):
        """Gets the first mineral in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first mineral in the group.
        """
        total = None
        if group in self._minerals.keys():
            total = self._minerals[group][0]
        return total

    def remove_actor(self, group, mineral):
        """Removes a mineral from the given group.
        
        Args:
            group (string): The name of the group.
            mineral (mineral): The mineral to remove.
        """
        if group in self._minerals:
            self._minerals[group].remove(mineral)
