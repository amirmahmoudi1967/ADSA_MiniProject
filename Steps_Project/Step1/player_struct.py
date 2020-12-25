
class Player() : 
    def __init__(self, name:str, score= None) : 
        self.name = name 
        self.impostor = False
        self.alive = True 
        self.score = score if score is not None else 0
        self.left = None  
        self.right = None
    