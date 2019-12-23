size(400, 400)

noStroke()

def triangle(x,y,a,b,c,d, color):
    fill(color)
    beginShape()
    vertex(x, y)
    vertex(a, b)
    vertex(c, d)
    endShape()
    
triangle(100, 100, 200, 200, 100, 200, "#33FF66")
triangle(100, 100, 120, 120, 100, 120, "#FF00FF")
triangle(180, 180, 200, 200, 180, 200, "#FFFF33")
triangle(100, 180, 100, 200, 120, 200, "#6633CC")
