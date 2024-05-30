#Imports
import os
from ecs_game import flight_engine

WIDTH = 640
HEIGHT = 480

# Graphics Definitions
rocket = flight_engine.GameElement("https://drive.usercontent.google.com/download?id=1mm6oe14OLho5jfe2cgUVDv4A63bla_Fs", (WIDTH / 2, HEIGHT / 2))
background = flight_engine.load_background("https://drive.usercontent.google.com/download?id=106y3sFitp8TiDrdOdOh4dMpRX2Pe2_Iv")

def is_safe_left(x):
    return True
def is_safe_right(x):
    return True
def is_safe_up(y):
    return True
def is_safe_down(y):
    return True

def is_onscreen(x, y):
    return True

##########################################################################
# PROVIDED CODE
# DO NOT CHANGE THIS CODE UNLESS YOU UNDERSTAND WHAT YOU ARE CHANGING
##########################################################################
os.environ['SDL_VIDEO_CENTERED'] = '1'
flight_engine.set_fps(30)
screen = flight_engine.initialize_screen(WIDTH, HEIGHT)
def draw():
    flight_engine.render_game(screen, background, rocket, WIDTH)
def update():
    flight_engine.update_cycle(rocket, is_onscreen)
flight_engine.run_game()