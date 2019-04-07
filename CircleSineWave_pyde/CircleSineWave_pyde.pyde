r1 = 100 #radius of circle 1
r2 = 10 #radius of circle 2
t = 0 #time variable
circleList = []

def setup():
    size(600,600)
    
def draw():
    global t, circleList
    background(200) #gray screen
    #move to left center of screen
    translate(width/4,height/2)
    noFill() #dont color in the shape
    stroke(0) # black line
    ellipse(0,0,2*r1,2*r1)
    
    #circling ellipse:
    fill(255,0,0) #red dot
    y = r1*sin(t)
    x = r1*cos(t)
    #add points to the list
    circleList = [y] + circleList[:249] 
    #adding points to list but only 250 or it will add points forever.
    ellipse(x,y,r2,r2)
    stroke(0,255,0) # green for the line
    line(x,y,200,y)
    fill(0,255,0) # green for the ellipse
    ellipse(200,y,10,10)
    #loop over circleList to leave a trail
    for i,c in enumerate(circleList):
        #small circle for trail
        ellipse(200+i,c,5,5)
    t += 0.05
