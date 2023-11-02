from tkinter import *
import time
import random
import os
import sys

window = Tk()
window.geometry("500x500")

direction = "d"
tick = 0
fruit_exists = 0
segments = []
segment_move = [""]
segment_move_temp = [""]
lastmove = ""
death = 0
speed = 0.1

def move_up(event):
    global direction
    global tick
    direction = "w"
    if tick == 0:
        timer()
def move_down(event):
    global direction
    global tick
    direction = "s"
    if tick == 0:
        timer()
def move_right(event):
    global direction
    global tick
    direction = "d"
    if tick == 0:
        timer()
def move_left(event):
    global direction
    global tick
    direction = "a"
    if tick == 0:
        timer()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<d>",move_right)
window.bind("<a>",move_left)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

fruit = PhotoImage(file="Img\Apple_big.png")
photoimage=PhotoImage(file="Img\Head_big_v2.png")
bodyimg=PhotoImage(file="Img\Body_big_v2.png")
deadimg=PhotoImage(file="Img\You_died_v3.png")
buttonimg=PhotoImage(file=r"Img\restart_button.png")
poleimg=PhotoImage(file=r"Img\Pole.png")
Pole = canvas.create_image(250,250,image=poleimg)
myimage = canvas.create_image(40,40,image=photoimage)

img0 = PhotoImage(file=r"Img\Numbers\0.png")
img1 = PhotoImage(file=r"Img\Numbers\\1.png")
img2 = PhotoImage(file=r"Img\Numbers\\2.png")
img3 = PhotoImage(file=r"Img\Numbers\\3.png")
img4 = PhotoImage(file=r"Img\Numbers\\4.png")
img5 = PhotoImage(file=r"Img\Numbers\\5.png")
img6 = PhotoImage(file=r"Img\Numbers\\6.png")
img7 = PhotoImage(file=r"Img\Numbers\\7.png")
img8 = PhotoImage(file=r"Img\Numbers\\8.png")
img9 = PhotoImage(file=r"Img\Numbers\\9.png")

def move():
    global direction
    global lastmove
    global segment_move
    global segment_move_temp

    if len(segments)>1:
        for n in reversed(range(len(segments)-1)):
            match segment_move[n]:
                case "w":
                    canvas.move(segments[n+1],0,-40)
                    segment_move[n+1]="w"
                case "s":
                    canvas.move(segments[n+1],0,40)
                    segment_move[n+1]="s"
                case "d":                   
                    canvas.move(segments[n+1],40,0)
                    segment_move[n+1]="d"
                case "a":
                    canvas.move(segments[n+1],-40,0)
                    segment_move[n+1]="a"

    if len(segments)>0:
        match lastmove:
            case "w":
                canvas.move(segments[0],0,-40)
                segment_move[0]="w"
                segment_move_temp[0]="w"
            case "s":
                canvas.move(segments[0],0,40)
                segment_move[0]="s"
                segment_move_temp[0]="s"
            case "d":
                canvas.move(segments[0],40,0)
                segment_move[0]="d"
                segment_move_temp[0]="d"
            case "a":
                canvas.move(segments[0],-40,0)
                segment_move[0]="a"
                segment_move_temp[0]="a"

    match direction:
        case "w":
            canvas.move(myimage,0,-40)
            lastmove = "w"
        case "s":
            canvas.move(myimage,0,40)
            lastmove = "s"
        case "d":
            canvas.move(myimage,40,0)
            lastmove = "d"
        case "a":
            canvas.move(myimage,-40,0)
            lastmove = "a"

    window.update()

def fate():
    spawn = random.randrange(9)
    global fruit_exists
    if (spawn > 5)&(fruit_exists==0):
        global myfruit
        myfruit = canvas.create_image(random.randrange(40,480,40),random.randrange(40,480,40),image=fruit)
        fruit_exists = 1

def check():
    global fruit_exists
    global death
    if fruit_exists == 1:
        if ((canvas.coords(myimage)[0]==canvas.coords(myfruit)[0]) & (canvas.coords(myimage)[1]==canvas.coords(myfruit)[1])):
            canvas.delete(myfruit)
            fruit_exists = 0
            procreate()
    
    for n in segments:
        if ((canvas.coords(myimage)[0]==canvas.coords(n)[0]) and (canvas.coords(myimage)[1]==canvas.coords(n)[1])):
            death = 1
    
    if (canvas.coords(myimage)[0]>=500) or (canvas.coords(myimage)[0]<=0) or (canvas.coords(myimage)[1]>=500) or ((canvas.coords(myimage)[1]<=0)):
        death = 1

    
def procreate():
    if len(segments)==0:
        match lastmove:
            case "w":
                segment = canvas.create_image(canvas.coords(myimage)[0],canvas.coords(myimage)[1]+40,image=bodyimg)
            case "s":
                segment = canvas.create_image(canvas.coords(myimage)[0],canvas.coords(myimage)[1]-40,image=bodyimg)
            case "d":
                segment = canvas.create_image(canvas.coords(myimage)[0]-40,canvas.coords(myimage)[1],image=bodyimg)
            case "a":
                segment = canvas.create_image(canvas.coords(myimage)[0]+40,canvas.coords(myimage)[1],image=bodyimg)
        segments.append(segment)
    else:
        match segment_move[-1]:
            case "w":
                segment = canvas.create_image(canvas.coords(segments[-1])[0],canvas.coords(segments[-1])[1]+40,image=bodyimg)
                segment_move.append("w")
            case "s":
                segment = canvas.create_image(canvas.coords(segments[-1])[0],canvas.coords(segments[-1])[1]-40,image=bodyimg)
                segment_move.append("s")
            case "d":
                segment = canvas.create_image(canvas.coords(segments[-1])[0]-40,canvas.coords(segments[-1])[1],image=bodyimg)
                segment_move.append("d")
            case "a":
                segment = canvas.create_image(canvas.coords(segments[-1])[0]+40,canvas.coords(segments[-1])[1],image=bodyimg)
                segment_move.append("a") 
        segments.append(segment)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def die():
    canvas.create_image(250,250,image=deadimg)

    if tick<10:
        numbers_mason(str(tick)[0],0,0)
    elif tick>10 and tick<100:
        numbers_mason(str(tick)[0],0,0)
        numbers_mason(str(tick)[1],30,0)
    elif tick>100 and tick<999:
        numbers_mason(str(tick)[0],0,0)
        numbers_mason(str(tick)[1],30,0)
        numbers_mason(str(tick)[2],60,0)
    else:
        numbers_mason(str(tick)[0],0,0)
        numbers_mason(str(tick)[1],30,0)
        numbers_mason(str(tick)[2],60,0)
        numbers_mason(str(tick)[3],90,0)

    rank = ranking(tick)

    if rank<10:
        numbers_mason(str(rank)[0],0,50)
    elif rank>10 and rank<100:
        numbers_mason(str(rank)[0],0,50)
        numbers_mason(str(rank)[1],30,50)
    elif rank>100 and rank<999:
        numbers_mason(str(rank)[0],0,50)
        numbers_mason(str(rank)[1],30,50)
        numbers_mason(str(rank)[2],60,50)
    else:
        numbers_mason(str(rank)[0],0,50)
        numbers_mason(str(rank)[1],30,50)
        numbers_mason(str(rank)[2],60,50)
        numbers_mason(str(rank)[3],90,50)

    B = Button(window, image=buttonimg, command = lambda: restart())
    B.place(x=200,y=400)

def ranking(tick):
    r = open("ranking.txt","r")
    if int(r.read()) < tick :
        w = open("ranking.txt","w")
        w.write(str(tick))
        return tick
    r = open("ranking.txt","r")
    return int(r.read())

def numbers_mason(number,posx,posy):
    match number:
        case "0":
            canvas.create_image(250+posx,250+posy,image=img0)
        case "1":
            canvas.create_image(250+posx,250+posy,image=img1)
        case "2":
            canvas.create_image(250+posx,250+posy,image=img2)
        case "3":
            canvas.create_image(250+posx,250+posy,image=img3)
        case "4":
            canvas.create_image(250+posx,250+posy,image=img4)
        case "5":
            canvas.create_image(250+posx,250+posy,image=img5)
        case "6":
            canvas.create_image(250+posx,250+posy,image=img6)
        case "7":
            canvas.create_image(250+posx,250+posy,image=img7)
        case "8":
            canvas.create_image(250+posx,250+posy,image=img8)
        case "9":
            canvas.create_image(250+posx,250+posy,image=img9)

def going_fast():
    global speed

    match tick:
        case 50:
            speed=0.09
        case 100:
            speed=0.085
        case 200:
            speed=0.08
        case 300:
            speed=0.075
        case 400:
            speed=0.07
        case 500:
            speed=0.065
        case 600:
            speed=0.06
        case 700:
            speed=0.055
        case 800:
            speed=0.05
        case 900:
            speed=0.045
        case 1000:
            speed=0.04
        case 1200:
            speed=0.035
        case 1400:
            speed=0.03

def timer():
    global death
    global speed
    while True:
        global tick
        tick +=1
        window.update()
        move()
        fate()
        print(tick)
        check()
        time.sleep(speed)
        going_fast()
        if death == 1:
            die()
            return



window.mainloop()





