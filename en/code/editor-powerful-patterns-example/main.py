from p5 import *
from random import randint


def setup():
    # Put code to run once here
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Put code to run every frame here
    no_stroke()
    fill(255, 0, 255, frame_count) 
    rect(5*frame_count, 50, 120, 100)
    fill(0, 0, 255,100)
    ellipse(randint(-100, 400), randint(-100, 400), 50, 50) 
    fill(125, 0, 255, frame_count) 
    rect(250, 5*frame_count, 100, 100)
    fill(255, 255, 0, frame_count) 
    rect(400-5*frame_count,250 , 100, 100)

# Keep this to run your code
run(frame_rate=5)

print('🟪 󠁢Look at these shapes! 🔵')