import Hexagon as hx
import Draw as dr
import ResultPrinter as rp
import csv
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
rect_width = 120
rect_height = 100

## Variables for the hexagons



len_no_rotation = 0
len_rotation = 0



def test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side):

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

       

        last_origin_y = place_vertical_hexagon(hexagons_no_rot, origin_x, origin_y, hex_width, hex_height, hex_side)

        if last_origin_y > highest_y:
            highest_y = last_origin_y

        ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_x += hex_width - (hex_width - hex_side)/2 + 0.3
            origin_y = start_origin_y + hex_height/2 + 0.3/2

        else:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3
            origin_y = start_origin_y


        line_index += 1
        ## Check if the line is out of the rectangle
        if origin_x + hex_width/2 > rect_width:
            break
    
    ## Draw the hexagons to see the result
    len_no_rotation = len(hexagons_no_rot)
    centering_no_rotation(hexagons_no_rot, highest_y, hex_width, hex_height, hex_side)
    
    dr.draw_rectangle(hexagons_no_rot)

    return len_no_rotation
    
def test_rotation(hexagons_rot, hex_width, hex_height, hex_side):

    ## Variables for the origin of the first hexagon
    start_origin_x = hex_width/2
    start_origin_y = hex_height/2

    origin_x = start_origin_x
    origin_y = start_origin_y

    ## Variables for the index of the line
    line_index = 1

    highest_x = 0

    while True:
    ## Start placing the hexagons
        last_origin_x = place_vertical_hexagon_rotated(hexagons_rot, origin_x, origin_y, hex_width, hex_height, hex_side)

        if last_origin_x > highest_x:
            highest_x = last_origin_x

    ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3
            origin_y = start_origin_y + hex_height/2 + 0.3/2

        else:
            origin_x += hex_width - (hex_width - hex_side)/2  + 0.3
            origin_y = start_origin_y

        line_index += 1

        ## Check if the line is out of the rectangle
        if origin_x + hex_width/2 > rect_height:
            break

    ## Draw the hexagons to see the result
    len_rotation = len(hexagons_rot)
    centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side)

    dr.draw_rectangle(hexagons_rot)

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
        hexagon.update_x_points(distance_x/2)
        hexagon.origin_y += distance_y/2
        hexagon.update_y_points(distance_y/2)

def centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side):

    last_origin_x = hexagons_rot[-1].origin_x
    extreme_point_y = last_origin_x + hex_width/2
    extreme_point_x = highest_x + hex_height/2

    ## Calculate the distance between the extreme point and the border of the rectangle

    distance_y = rect_height - extreme_point_y
    distance_x = rect_width - extreme_point_x

    for hexagon in hexagons_rot:
        hexagon.origin_y += distance_y/2
        hexagon.update_y_points(distance_y/2)
        hexagon.origin_x += distance_x/2
        hexagon.update_x_points(distance_x/2)


## Main Function calls

def compute(hex_width, hex_height, hex_side):

    hexagons_no_rot = []
    hexagons_rot = []

    len_no_rotation = test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side)

    len_rotation = test_rotation(hexagons_rot, hex_width, hex_height, hex_side)

    print(len_no_rotation)
    print(len_rotation)

    if(len_no_rotation > len_rotation):
        print("Parallel to x-axis is better ")
        print("Origin of the first hexagon = " + str(120 - hexagons_no_rot[0].origin_x) + " " + str(100 - hexagons_no_rot[0].origin_y))
        create_csv_result(120 - hexagons_no_rot[0].origin_x, 100 - hexagons_no_rot[0].origin_y, "parallela")
        
    else:
        print("Perpendicular to x-axis is better")
        print("Origin of the first hexagon = " + str(120 - hexagons_rot[0].origin_x) + " " + str(100 - hexagons_rot[0].origin_y))
        create_csv_result(120 - hexagons_rot[0].origin_x, 100 - hexagons_rot[0].origin_y, "perpendicolare")


def create_csv_result(x, y, orientation):
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([x, y, orientation])












   
