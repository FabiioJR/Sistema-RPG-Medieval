from criatura import Criatura

class Guerreiro(Criatura):
    def __init__(self, nome, pontos_vida, ataque, defesa, arma):
        super().__init__(nome, pontos_vida, ataque, defesa)
        self._arma = arma
    
    
    def atacar(self):
        return self._ataque + self._ataque * self._arma * 0.3
    
    def defender(self):
        self._defesa += 25
        if self._defesa > 300:
            self._defesa = 300
