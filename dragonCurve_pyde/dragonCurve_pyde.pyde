RED = color(255,0,0)
BLACK = color(0)

def setup():
    global theLevel,size1
    size(600,600)
    theLevel = 13
    size1 = 4
    
def draw():
    global theLevel
    background(255)
    translate(width/2, height/2)
    angle = map(mouseX,0,width,0,2*PI)
    stroke(RED)
    strokeWeight(3)
    pushMatrix()
    leftDragon(size1,theLevel)
    popMatrix()
    leftDragon(size1,theLevel-1)
    rotate(angle)
    stroke(BLACK)
    rightDragon(size1,theLevel-1)
    
def leftDragon(size1,theLevel):
    if theLevel == 0:
        line(0,0,size1,0)
        translate(size1,0)
    else:
        leftDragon(size1,theLevel-1)
        rotate(radians(-90))
        rightDragon(size1,theLevel-1)
        
def rightDragon(size1,theLevel):
    if theLevel == 0:
        line(0,0,size1,0)
        translate(size1,0)
    else:
        leftDragon(size1,theLevel-1)
        rotate(radians(90))
        rightDragon(size1,theLevel-1)
        
def keyPressed():
    global theLevel,size1
    if key == CODED:
        if keyCode == UP:
            theLevel += 1
        if keyCode == DOWN:
            theLevel -= 1
        if keyCode == LEFT:
            size1 += 5
        if keyCode == RIGHT:
            size1 -= 5
