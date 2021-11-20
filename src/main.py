from math import sin
from time import sleep

from pygame import Surface, Color, SRCALPHA, draw

from src.game import Game
from src.launcher import Launcher


game, launcher = Game(), Launcher()
center_x = int(game.config.width / 2)
center_y = int(game.config.height / 2)
dot_color = Color('white')


def draw_coordinate_plane():
    game.screen.fill((0, 0, 0))
    x_axis = Surface((game.config.width, 3))
    y_axis = Surface((3, game.config.height))
    x_axis.fill((50, 50, 50))
    y_axis.fill((50, 50, 50))
    game.screen.blit(x_axis, (0, game.config.height / 2))
    game.screen.blit(y_axis, (game.config.width / 2, 0))


def draw_dot(x, y):
    game.context['plane'].set_at((x, y), dot_color)


def track_time():
    try:
        game.context['tick'] += 1
        if game.context['tick'] == game.config.width:
            game.activate_kill_switch()
    except KeyError:
        game.context['tick'] = 0


def add_drawing_plane():
    surface = Surface(game.config.window_size, SRCALPHA)
    game.context['plane'] = surface
    game.context['previous_positive_point'] = (center_x , center_y)
    game.context['previous_negative_point'] = (center_x , center_y)


def squared(x: int) -> int:
    return int(1/(game.config.width / 2) * x * x)


def linear(x: int) -> int:
    return x


def sinwave(x: int) -> int:
    return int(100*sin((1/10)*x))


def draw_parabola():
    if game.context['tick'] <= game.config.width / 2:
        # positive side
        x = game.context['tick'] + center_x
        y = 0 - linear(game.context['tick']) + center_y
        print(f'Point: ({x}, {y})')
        draw.line(
            game.context['plane'],
            Color('green'),
            game.context['previous_positive_point'],
            (x, y)        
        )
        draw_dot(x, y)
        game.context['previous_positive_point'] = (x, y)
        
        #negative side
        x = center_x - game.context['tick']
        y = 0 - linear(x - center_x) + center_y
        draw.line(
            game.context['plane'],
            Color('red'),
            game.context['previous_negative_point'],
            (x, y)        
        )
        draw_dot(x, y)
        game.context['previous_negative_point'] = (x, y)
        
        # put it on the screen!
        game.screen.blit(game.context['plane'], (0, 0))


def wait_a_few_seconds():
    sleep(5)


# game.add_task('launch', launcher.open)
game.add_task('start', draw_coordinate_plane)
game.add_task('start', add_drawing_plane)
game.add_task('loop', track_time)
game.add_task('loop', draw_parabola)
game.add_task('close', wait_a_few_seconds)
game.prime_engine()
game.start_loop()
