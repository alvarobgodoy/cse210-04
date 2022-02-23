# mineral(entity): hereda de la clase actor, atributo: puntos (negativos o positivos). Metodos: get_points y set_points.


from entity import entity


class mineral(entity):

    def __init__(self):

        self._is_rock=False

        self._is_mineral= False 
    


    def indentificador(self):
        self.gema= super.get_gema()
        self.roca=super.get_rock()

        if select == self.gema:
            self._is_mineral==True
        else:
            self._is_rock=True
            self._is_mineral=False     

