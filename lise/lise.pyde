size(400, 400)

offset = -100
coef = 2

noStroke()

def triangle(x,y,a,b,c,d, color):
    fill(color)
    beginShape()
    vertex(x*coef+offset, y*coef+offset)
    vertex(a*coef+offset, b*coef+offset)
    vertex(c*coef+offset, d*coef+offset)
    endShape()

def wrap_rect(x, y , a, b):
    rect(x*coef+offset, y*coef+offset, a*coef, b*coef)

def wrap_line(x, y, a, b):
    line(x*coef+offset, y*coef+offset, a*coef+offset, b*coef+offset)

background("#00FF00")

light_green = "#33FF66"
light_pink = "#FFCCFF"                                                
triangle(100, 100, 200, 200, 100, 200, light_pink)

triangle(100, 100, 120, 120, 100, 120, "#FF00FF")
triangle(180, 180, 200, 200, 180, 200, "#FFFF33")
triangle(100, 180, 100, 200, 120, 200, "#6633CC")
fill("#FF0066")
wrap_rect(100, 120, 2, 62)
fill("#FF9933")
wrap_rect(118, 198, 62, 2)

stroke("#3333FF")
strokeWeight(4)
wrap_line(120,120,180, 180)
