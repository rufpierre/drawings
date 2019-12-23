size(800, 800)
noStroke()


#offset = -700
#coef = 8
offset = 0
coef = 1

noStroke()

def triangle(x,y,a,b,c,d, color):
    fill(color)
    beginShape()
    vertex(x*coef+offset, y*coef+offset)
    vertex(a*coef+offset, b*coef+offset)
    vertex(c*coef+offset, d*coef+offset)
    endShape()

def arc_wrap(x, y, w, h, start, stop):
    arc(x*coef+offset, y*coef+offset, w*coef, h*coef, start, stop)

def heart(x, y, radius, color):
    fill(color)
    #radius = 20
    arc_wrap(x, y, 2*radius, 2*radius, -3.14, 0)
    arc_wrap(x+2*radius, y, 2*radius, 2*radius, -3.14, 0)
    #     triangle(x-radius, y, x+(3*radius), y, x+radius, y+(radius*28/20), red)
    triangle(x-radius, y, x+3*radius, y, x+radius, y+(2*radius*28/20), color)
    
red = "#FF6666"
white = "#FFFFFF"
#heart(100, 100, 10, red)
#heart(95, 100, 5, white)
#heart(115, 100, 5, white)

heart(128, 128, 128, red)
heart(128-64, 128, 64, white)
heart(128+128+64, 128, 64, white)

#def recursive_heart(x, y, radius, color):
#    heart(x, y, radius, color)
#    if color == red:
#        recursive_heart(x-radius/2, y, radius/2, white)
#    else:
#        a = 1
