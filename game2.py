from graphics import *
import time
import random

#someimage = Image(Point(790, 790), 'bucket.pgn')
win = GraphWin("My Circle", 800, 800)
c = Image(Point(780, 790), 'thisbucket.gif')
#c.setFill("#000000")
#c.draw(win)
message = Text(Point(400, 400), "")
message.draw(win)
message.undraw()
count = 0
count2 = 0
circlelist = []
win.setBackground('#ffffff')



def main():
    global count
    global count2
    score = Text(Point(720, 720), count)
    highscoretext = Text(Point(655, 700), "High Score: ")
    regularscoretext = Text(Point(660, 720), "Score: ")
    highscore = Text(Point(720, 700), count2)
    highscoretext.draw(win)
    regularscoretext.draw(win)
    score.draw(win)
    highscore.draw(win)
    randx = random.randrange(20, 780, 20)
    o = Image(Point(randx, 0), 'apple.gif')
    circlelist.append(o)
    o.draw(win)
    c.draw(win)
    while True:
        o.move(0, 2)
        time.sleep(0.005)
        keypressed = win.checkKey()
        if keypressed == "Left":
            c.move(-20, 0)
        elif keypressed == "Right":
            c.move(20, 0)
        centerofo = o.getAnchor()
        ox = centerofo.getX()
        oy = centerofo.getY()
        centerofcircle = c.getAnchor()
        cx = centerofcircle.getX()
        cy = centerofcircle.getY()

        if oy == 300:
            circlelist.pop(0)
            for circle in circlelist:
                circle.draw(win)
                circle.move(0, 1)

        if oy == 790 and ox != cx:
            count = 0
            global message
            message.undraw()
            message = Text(Point(400, 400), "Missed!")
            message.draw(win)
            o.undraw()
            score.undraw()
            highscore.undraw()
            highscoretext.undraw()
            regularscoretext.undraw()
            break
        elif ox == cx and oy == cy:
            global message
            global count
            message.undraw()
            message = Text(Point(400, 400), "Got it!")
            message.draw(win)
            o.undraw()
            count = count + 1
            if count > count2:
                highscore.undraw()
                count2 = count
                highscore.draw(win)
                highscoretext.undraw()
            score.undraw()
            highscore.undraw()
            highscoretext.undraw()
            regularscoretext.undraw()
            break
    c.undraw()

        
        
        
                
        
    
while True:
    main()


