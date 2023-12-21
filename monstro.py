from criatura import Criatura

class Monstro(Criatura):
    def __init__(self, nome, pontos_vida, ataque, defesa, nivel):
        super().__init__(nome, pontos_vida, ataque, defesa)
        self._nivel = nivel

    def atacar(self):
        return self._ataque + self._ataque * self._nivel * 0.1
    
    def defender(self):
        self._defesa += 25 
        if self._defesa > 350:
            self._defesa = 350
