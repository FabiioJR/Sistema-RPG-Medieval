import abc

class Criatura(abc.ABC):
    def __init__(self, nome, pontos_vida, ataque, defesa):
        self._nome = nome

        if pontos_vida < 400:
            self._pontos_vida = 400 
        elif pontos_vida > 1000:
            self._pontos_vida = 1000
        else:
            self._pontos_vida = pontos_vida

        if ataque < 50:
            self._ataque = 50 
        elif ataque > 200:
            self._ataque = 200 
        else:
            self._ataque = ataque 

        if defesa < 10:
            self._defesa = 10 
        elif defesa > 200:
            self._defesa = 200 
        else:
            self._defesa = defesa

    @abc.abstractmethod
    def atacar(self):
        pass

    @abc.abstractmethod
    def defender(self,dano):
        pass
    
    def sofre_dano(self, dano):
        dano_final = dano - self._defesa
        if dano_final < 0:
            dano_final = 0
        self._pontos_vida -= dano_final

    
    @property
    def pontos_vida(self):
        return self._pontos_vida
