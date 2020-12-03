
class Player() : 
    def __init__(self, name:str, score= None) : 
        self.name = name 
        self.impostor = False
        self.alive = True 
        self.score = score if score is not None else 0
        self.left = None  
        self.right = None
    
    def __str__(self) -> str: 
        res = self.name + 'is'
        if self.alive: 
            res += ' alive, and he is '
        else : 
            res += ' dead, and he is '
        if self.impostor: 
            res += 'an Impostor'
        else : 
            res += 'a Crewmate'
        return res 