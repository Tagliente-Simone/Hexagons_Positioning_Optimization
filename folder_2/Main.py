from folder_2 import Draw as d 
from folder_2 import Rectangle as r
import csv

rect_height = 105
rect_width = 125


def place_rect(L, l):

    origin = [L/2, l/2]
    rectangles = []
    
    

    while True:

        origin[0] = L/2

        while True:
            
            rectangles.append(r.Rectangle(L, l, origin[0], origin[1]))
            
            if origin[0] + L + L/2 + 0.2> rect_width:
                break
            else:
                origin[0] += L + 0.2


        if origin[1] + l + l/2 + 0.2 > rect_height:
            break
        else:
            origin[1] += l + 0.2

        
    last_origin = (rectangles[-1].center_x, rectangles[-1].center_y)

    slack_y = rect_height - last_origin[1] - l/2
    slack_x = rect_width - last_origin[0] - L/2

    for rectangle in rectangles:
        rectangle.update_points(slack_x/2, slack_y/2)


    return rectangles


def main(L, l):

    rectangles_norot = place_rect(L, l)

    rectangles_rot = place_rect(l, L)

    if(len(rectangles_norot) > len(rectangles_rot)):
        rectangles = rectangles_norot
        save_on_csv(rectangles, 'no')

    else:
        rectangles = rectangles_rot
        save_on_csv(rectangles, 'yes')

    d.draw_rectangles(rectangles)
    
    return rectangles


def save_on_csv(rectangles, rotation):
    with open('rectangles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['x', 'y', 'rotazione'])

        for rectangle in rectangles:
            writer.writerow([rectangle.center_x, rectangle.center_y, rotation])