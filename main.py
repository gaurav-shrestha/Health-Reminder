from pygame import mixer
from datetime import datetime
from time import time

def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("actions.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

init_water=time()
init_eyes=time()
init_exrcse=time()
water_music=30*60
eyes_music=60*60
exrcse_music=120*60

while True:
    if time() - init_water > water_music:
        print("TIME TO DRINK WATER!! Write 'drank' to stop.")
        music("./musics/water.mp3","drank")
        init_water=time()
        log("Drank water at ")

    if time() - init_eyes > eyes_music:
        print("TIME TO DO REST!! Write 'ok' to stop.")
        music("./musics/eyes.mp3","ok")
        init_eyes=time()
        log("Eyes rest done at ")

    if time() - init_exrcse > exrcse_music:
        print("TIME TO DO EXERCISE!! Write 'ok' to stop.")
        music("./musics/exercise.mp3","ok")
        init_exrcse=time()
        log("Exercise done at ")