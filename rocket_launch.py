#Imports
import os
from ecs_game import launch_engine

WIDTH = 300
HEIGHT = 480

# Graphics Definitions
rocket = launch_engine.GameElement("https://drive.usercontent.google.com/download?id=1mm6oe14OLho5jfe2cgUVDv4A63bla_Fs", (WIDTH / 2 - 15, HEIGHT - 10))
rocket.scale(1.5)
background = launch_engine.load_background("https://drive.usercontent.google.com/download?id=106y3sFitp8TiDrdOdOh4dMpRX2Pe2_Iv")

def rocket_height(time):
    return 0

##########################################################################
# PROVIDED CODE
# DO NOT CHANGE THIS CODE UNLESS YOU UNDERSTAND WHAT YOU ARE CHANGING
##########################################################################
os.environ['SDL_VIDEO_CENTERED'] = '1'
launch_engine.set_fps(30)
screen = launch_engine.initialize_screen(WIDTH, HEIGHT)
elapsed = 0
def draw():
    launch_engine.render_game(screen, background, rocket, elapsed, WIDTH, HEIGHT, rocket_height)
def update():
    global elapsed
    elapsed = launch_engine.update_cycle(rocket, rocket_height, elapsed, HEIGHT)
launch_engine.run_game()