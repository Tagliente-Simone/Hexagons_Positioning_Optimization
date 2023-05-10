from folder_1 import Hexagon as hx
from folder_1 import Draw as dr
import csv
import math
## This function places the vertical line of hexagons

def place_vertical_hexagon(hexagons_no_rot, origin_x, origin_y, hex_width, hex_height, hex_side):
    
    last_origin_y = 0

    while True:
        hexagon = hx.Hexagon(origin_x, origin_y, hex_width, hex_height, hex_side)
        hexagons_no_rot.append(hexagon)

        if origin_y > last_origin_y:
            last_origin_y = origin_y
           
        origin_y += hex_height + 0.3


        ## Check if the hexagon is out of the rectangle
        if origin_y + hex_height/2 > rect_height:
            
            break
 
    return last_origin_y


def place_vertical_hexagon_rotated(hexagons_rot, origin_x, origin_y, hex_width, hex_height, hex_side):

    last_origin_y = 0

    while True:
        hexagon = hx.Hexagon(origin_x, origin_y, hex_width, hex_height, hex_side)
        hexagon.rotate90()
        hexagons_rot.append(hexagon)

        if origin_y > last_origin_y:
            last_origin_y = origin_y
        
        origin_y += hex_height + 0.3

        ## Check if the hexagon is out of the rectangle
        if origin_y + hex_height/2 > rect_width:
            break

    return last_origin_y

## Variables for the rectangle
rect_width = 125
rect_height = 105

## Variables for the hexagons
len_no_rotation = 0
len_rotation = 0



def test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side, index):

    ## Variables for the origin of the first hexagon
    start_origin_x = hex_width/2
    start_origin_y = hex_height/2 

    origin_x = start_origin_x
    origin_y = start_origin_y

    ## Variables for the index of the line
    line_index = 1

    highest_y = 0

    ## Start placing the hexagons
    while True:

        ## Check if the line is out of the rectangle
        if origin_x + hex_width/2 > rect_width:
            break

        last_origin_y = place_vertical_hexagon(hexagons_no_rot, origin_x, origin_y, hex_width, hex_height, hex_side)

        if last_origin_y > highest_y:
            highest_y = last_origin_y

        ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_x += hex_width - (hex_width - hex_side)/2 + 0.3/(math.sin(math.atan((hex_height) / ((hex_width - hex_side)))))
            origin_y = start_origin_y + hex_height/2 + 0.3/2

        else:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3
            origin_y = start_origin_y


        line_index += 1
        
    
    ## Draw the hexagons to see the result
    len_no_rotation = len(hexagons_no_rot)
    centering_no_rotation(hexagons_no_rot, highest_y, hex_width, hex_height, hex_side)
    dr.draw_rectangle(hexagons_no_rot, hex_width, hex_height, hex_side, "no_rotation", index)
    return len_no_rotation
    
def test_rotation(hexagons_rot, hex_width, hex_height, hex_side, index):

    ## Variables for the origin of the first hexagon
    start_origin_x = hex_width/2
    start_origin_y = hex_height/2

    origin_x = start_origin_x
    origin_y = start_origin_y

    ## Variables for the index of the line
    line_index = 1

    highest_x = 0

    while True:

    
        ## Check if the line is out of the rectangle
        if origin_x + hex_width/2 > rect_height:
            break
        
        ## Start placing the hexagons
        last_origin_x = place_vertical_hexagon_rotated(hexagons_rot, origin_x, origin_y, hex_width, hex_height, hex_side)

        if last_origin_x > highest_x:
            highest_x = last_origin_x

    ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3/(math.sin(math.atan((hex_height) / ((hex_width - hex_side)))))
            origin_y = start_origin_y + hex_height/2 + 0.3/2

        else:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3
            origin_y = start_origin_y

        line_index += 1

        

    ## Draw the hexagons to see the result
    len_rotation = len(hexagons_rot)
    centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side)

    dr.draw_rectangle(hexagons_rot, hex_width, hex_height, hex_side, "rotation", index)

    

    return len_rotation

def centering_no_rotation(hexagons_no_rot, highest_y, hex_width, hex_height, hex_side):
    
    last_origin_x = hexagons_no_rot[-1].origin_x
    extreme_point_x = last_origin_x + hex_width/2

    extreme_point_y = highest_y + hex_height/2



    ## Calculate the distance between the extreme point and the border of the rectangle
    distance_x = rect_width - extreme_point_x
    distance_y = rect_height - extreme_point_y
    
    for hexagon in hexagons_no_rot:
        hexagon.origin_x += distance_x/2
        hexagon.origin_y += distance_y/2
        hexagon.update_points(distance_x/2, distance_y/2)

def centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side):

    last_origin_x = hexagons_rot[-1].origin_x
    extreme_point_y = last_origin_x + hex_width/2
    extreme_point_x = highest_x + hex_height/2

    ## Calculate the distance between the extreme point and the border of the rectangle

    distance_y = rect_height - extreme_point_y
    distance_x = rect_width - extreme_point_x

    for hexagon in hexagons_rot:
        hexagon.origin_y += distance_y/2
        hexagon.origin_x += distance_x/2
        hexagon.update_points(distance_x/2, distance_y/2)


## Main Function calls

def compute(hex_width, hex_height, hex_side, index):

    hexagons_no_rot = []
    hexagons_rot = []

    len_no_rotation = test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side, index)
    len_rotation = test_rotation(hexagons_rot, hex_width, hex_height, hex_side, index)

    if(len_no_rotation > len_rotation):
        dr.draw_rectangle(hexagons_no_rot, hex_width, hex_height, hex_side, "no", index)
        save_on_csv(hexagons_no_rot, "no")
        return len_no_rotation
        
        
    else:
        dr.draw_rectangle(hexagons_rot, hex_width, hex_height, hex_side, "si", index)
        save_on_csv(hexagons_rot, "si")
        return len_rotation




def save_on_csv(hexagons, rotation):
    with open('hexagons.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['x', 'y', 'rotazione'])

        for hexagon in hexagons:
            writer.writerow([hexagon.origin_x, hexagon.origin_y, rotation])
        


        







   
