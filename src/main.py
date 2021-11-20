from game import Game
from launcher import Launcher


game, launcher = Game(), Launcher()

game.add_task('start', launcher.open)

game.prime_engine()
game.start_loop()
