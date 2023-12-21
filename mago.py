from criatura import Criatura

class Mago(Criatura):
    def __init__(self, nome, pontos_vida, ataque, defesa, magia):
        super().__init__(nome, pontos_vida, ataque, defesa)
        self._magia = magia

    def atacar(self):
        return self._ataque + self._ataque * self._magia * 0.5
    
    def defender(self):
        self._defesa += 25
        if self._defesa > 250:
            self._defesa = 250
