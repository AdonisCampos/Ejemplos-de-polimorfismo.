from Jugador1 import Jugador1
from Jugador1 import player2
class Jugador2(Jugador1):
    def Jugar ():
        return '{} Juega la FIFA 2023'.format(player2.nombreJugador)
jugador1 = Jugador1
jugador2 = Jugador2
print (jugador1.Jugar())
print (jugador2.Jugar())
