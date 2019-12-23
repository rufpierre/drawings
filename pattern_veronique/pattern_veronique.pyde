size(304, 304)
#size(604, 604)
noStroke()

square_width = 16
square_count = 19

def rect_by_pos(i, j):
    rect(i*square_width, j*square_width, square_width, square_width)

def sym(i):
    return square_count - (i+1)

def quad(i, j):
    rect_by_pos(i, j)
    rect_by_pos(sym(i), j)
    rect_by_pos(sym(i), sym(j))
    rect_by_pos(i, sym(j))

def pattern(offset, color):
    fill(color)
    for i in range(int((square_count+1)/2)):
        j = i + offset
        quad(i, i+offset)
        quad(i+offset, i)
    

blue = "#3399FF"
lilac = "#6666CC"
orange = "#FF9966"
green = "#009999"
yellow = "#FFFF66"
pink = "#FF99CC"
deep_blue = "#003399"
red = "#FF3333"
light_green = "#CCFF99"
light_grey = "#EEEEEE"
    
pattern(9, light_grey)
pattern(8, light_green)
pattern(7, red)
pattern(6, deep_blue)
pattern(5, pink)
pattern(4, yellow)
pattern(3, green)
pattern(2, orange)
pattern(1, lilac)
pattern(0, blue)
    
            
#for i in range(19):
#    rect(i*square_width, i*square_width, square_width, square_width)
