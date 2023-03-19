import math
import matplotlib.pyplot as plt
import draw as dr
from collections import namedtuple as nt
import Hexagon as hx

hex_height = 7
hex_width = 3

hexagon = hx.Hexagon(hex_width/2, hex_height/2, hex_width, hex_height)
ob_side = math.sqrt((hexagon.x1-hexagon.x2)**2 + ((hexagon.y1-hexagon.y2))**2)
short_side = math.sqrt((ob_side)**2 - ((hex_height/2))**2)

hexagons = []


rect_width = 120
rect_height = 100



if hex_height < hex_width:
    ny_hexagons = math.floor(rect_height / hex_height)

    origin_y = hex_height/2
    origin_x = hex_width/2

    new_origin_x = origin_x
    new_origin_y = origin_y

    from_base = True

    while True:

        total_length = 0

        for n in range(ny_hexagons):
            if from_base == 1:
                total_length += hex_height
                if(total_length >= rect_height):
                    break
            else:
                total_length += hex_height
                if(total_length >= rect_height - hex_height/2):
                    break
            hexagon = hx.Hexagon(new_origin_x, new_origin_y, hex_width, hex_height)
            hexagons.append(hexagon)
            new_origin_y += hex_height
            
        if from_base:
            new_origin_y = origin_y + origin_y
            from_base = False
        else:
            new_origin_y = origin_y
            from_base = True

        new_origin_x = new_origin_x + origin_x + (origin_x - short_side)

        last_position = new_origin_x + hex_width/2

        if last_position >= rect_width:
            break

    dr.draw_rectangle(hexagons, False)


else:
    nx_hexagons = math.floor(rect_width / hex_width)

    origin_y = hex_height/2
    origin_x = hex_width/2

    new_origin_x = origin_x
    new_origin_y = origin_y

    from_base = True

    while True:

        total_length = 0

        for n in range(nx_hexagons):
            if from_base == 1:
                total_length += hex_height
                if(total_length >= rect_height):
                    break
            else:


                total_length += hex_height
                if(total_length >= rect_height - hex_height/2):
                    break
            hexagon = hx.Hexagon(new_origin_x, new_origin_y, hex_width, hex_height)
            hexagons.append(hexagon)
            new_origin_y += hex_height
            
        if from_base:
            new_origin_y = origin_y + origin_y
            from_base = False
        else:
            new_origin_y = origin_y
            from_base = True

        new_origin_x = new_origin_x + origin_x + (origin_x - short_side)

        last_position = new_origin_x + hex_width/2

        if last_position >= rect_width:
            remaining = rect_width - hexagons[-1].origin_x - hex_width/2
            for hexagon in hexagons:

                hexagon.origin_x += remaining/2

                ## ------- this is for drawing purposes only
                hexagon.x1 += remaining/2
                hexagon.x2 += remaining/2
                hexagon.x3 += remaining/2
                hexagon.x4 += remaining/2
                hexagon.x5 += remaining/2
                hexagon.x6 += remaining/2
                
            break

    dr.draw_rectangle(hexagons, False)

    








