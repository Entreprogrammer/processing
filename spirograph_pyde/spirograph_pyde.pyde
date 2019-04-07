"""By changing r2 bigger or smaller and changing the prop you
can make different designs."""

r1 = 300.0 # radius of big circle
r2 = 95.0 # radius of small circle
r3 = 5.0 # radius of drawing dot
#location of big circle
x1 = 0
y1 = 0
t = 0
prop = 0.85 #sets the drawing dot away from the edge of the inside circle
points = []

def setup():
    size(600,600)
    
def draw():
    global r1,r2,x1,x2,t,prop,points
    translate(width/2, height/2)
    background(255)
    noFill()
    #big circle
    stroke(0)
    ellipse(x1,y1,2*r1,2*r1)
    #circle 2
    x2 = (r1 - r2)*cos(t)
    y2 = (r1 - r2)*sin(t)
    ellipse(x2,y2,2*r2,2*r2)
    #drawing dot
    x3 = x2+prop*(r2 - r3)*cos(-((r1-r2)/r2)*t)
    y3 = y2+prop*(r2 - r3)*sin(-((r1-r2)/r2)*t)
    fill(255,0,0)
    ellipse(x3,y3,2*r3,2*r3)
    points = [[x3, y3]] + points[:2000]
    for i,p in enumerate(points):
        if i < len(points)-1:
            stroke(255,0,0) #draw line between points
            line(p[0],p[1],points[i+1][0],points[i+1][1])
            
    t += .2
