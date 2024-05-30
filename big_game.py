##########################################################################
# FIRSTNAME LASTNAME
# Period: PERIOD NUMBER
# Game Title: GAME TITLE HERE
##########################################################################
#Imports
import os
from ecs_game import engine
from ecs_game.engine import GameElement
from pgzero.keyboard import keyboard

os.environ['SDL_VIDEO_CENTERED'] = '1'
# Initialize screen and positions
engine.set_fps(60)
WIDTH = 640
HEIGHT = 480
screen = engine.initialize_screen(WIDTH, HEIGHT)
player_starting_pos = (WIDTH/2, HEIGHT/2)
target_starting_pos = (0, 0)
danger_starting_pos = (0, 0)

# Game title: Write the title of your game here & change color if desired
TITLE = "Game Title"
COLOR = (255, 255, 255)

# Graphics Definitions
player = GameElement("https://drive.usercontent.google.com/download?id=1dBDYHqLPuDsP7kIgnFUKX12gwAHWr2-p", player_starting_pos)
target = GameElement('https://drive.usercontent.google.com/download?id=1HK5jfTkYizeXblERcAo_2O8YCokX4hjD', target_starting_pos)
danger = GameElement('https://drive.usercontent.google.com/download?id=1t71we32KMq-syrGqA7AB8Np2S0E1BEOH', danger_starting_pos)
mystery = GameElement('https://drive.usercontent.google.com/download?id=1MwVJ8plJJmkn3TWNsGQApRCnqxxL2GyI', player.pos)
background = engine.load_background("https://drive.usercontent.google.com/download?id=106y3sFitp8TiDrdOdOh4dMpRX2Pe2_Iv")

player.scale(1.2)
player.flip_horizontal()
danger.scale(1.5)
danger.flip_horizontal()

##########################################################################
# 1. Danger and Target movement section
##########################################################################

# update_danger function
def update_danger(x, y):
    return [x, y]

#update_target function
def update_target(x, y):
    return [x, y]

##########################################################################
# 2. Safe on-screen section
##########################################################################

#is_safe_left function
def is_safe_left(x):
    return True

#is_safe_right function
def is_safe_right(x):
    return True

#is_safe-up_function
def is_safe_up(y):
    return True

#is_safe_down function
def is_safe_down(y):
    return True

#is_onscreen function
def is_onscreen(x, y):
    return True

##########################################################################
# 3. Player movement section
##########################################################################

# update_player function
def update_player(x, y):
    return [x, y]

##########################################################################
# 4. Collision detection section
##########################################################################

# line_length function
def line_length(a, b):
    return a

# distance function
def distance(cx, cy, dx, dy):
    return cx

# is_collision function
def is_collision(cx, cy, dx, dy):
    return False

##########################################################################
# 4. Mystery section
##########################################################################

#update_mystery function
def update_mystery(x, y):
    return [x, y]

##########################################################################
# PROVIDED CODE
# DO NOT CHANGE THIS CODE UNLESS YOU UNDERSTAND WHAT YOU ARE CHANGING
##########################################################################
score = 100
mysteries = []
mysteries_lag = 0
danger_lag = 0
target_lag = 0
player_alive = True

def draw():
    engine.render_game(player_alive, screen, background, player,
                target, danger, mysteries, TITLE, score, COLOR,
                WIDTH, HEIGHT)

def update():
    global score
    global mysteries_lag
    global danger_lag
    global target_lag
    global player_alive

    cycle = engine.update_cycle(player, danger, target, mystery, mysteries, is_onscreen, update_player, update_target,
             update_danger, update_mystery, is_collision, score, WIDTH, HEIGHT, keyboard, mysteries_lag, danger_lag,
                     target_lag, player_alive, player_starting_pos, target_starting_pos, danger_starting_pos)

    score = cycle[0]
    mysteries_lag = cycle[1]
    danger_lag = cycle[2]
    target_lag = cycle[3]
    player_alive = cycle[4]

engine.run_game()