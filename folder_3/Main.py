from folder_3 import Trapeze as t
from folder_3 import RotatedTrapeze as rt
import shared_variable as sv

rect_width = sv.rect_width
rect_height = sv.rect_height


inter = sv.inter

def place_trapezes(B, b, b_med, h_min, h_max, radius):
    
    origin = [h_max/2, B/2]
    trapezes = []
    
    rotate180 = True
    
    while True:
        
        
        origin[0] = h_max/2
        
        while True:
            if rotate180:
                trapezes.append(t.Trapeze(B, b, b_med, h_min, h_max, origin[0], origin[1]))
                trapezes[-1].rotate180()
            else:
                trapezes.append(t.Trapeze(B, b, b_med, h_min, h_max, origin[0], origin[1]))
                
            if origin[0] + h_max + h_max/2 + inter > rect_width:
                rotate180 = not rotate180
                break
            else:
                origin[0] += h_max + inter
        if origin[1] + B + B/2 + inter - radius > rect_height:
            break
        else:
            origin[1] += B + inter - radius

    last_origin = (trapezes[-1].origin_x, trapezes[-1].origin_y)
    
    slack_y = rect_height - last_origin[1] - B/2
    slack_x = rect_width - last_origin[0] - h_max/2
    
    for trapeze in trapezes:
        trapeze.update_points(slack_x/2, slack_y/2)
    

        
    
    return trapezes


def place_rotated_trapezes(B, b, b_med, h_min, h_max, radius):

    origin = [B/2, h_max/2]
    trapezes = []

    rotate180 = True

    while True:

        origin[0] = B/2

        while True:
            if rotate180:
                trapezes.append(rt.RotatedTrapeze(B, b, b_med, h_min, h_max, origin[0], origin[1]))
                trapezes[-1].rotate180()
                rotate180 = not rotate180
            else:
                trapezes.append(rt.RotatedTrapeze(B, b, b_med, h_min, h_max, origin[0], origin[1]))
                rotate180 = not rotate180

            if origin[0] + B + B/2 + inter - radius > rect_width:
                
                break
            else:
                origin[0] += B + inter - radius
        if origin[1] + h_max + h_max/2 + inter > rect_height:
            break
        else:
            origin[1] += h_max + inter

    last_origin = (trapezes[-1].origin_x, trapezes[-1].origin_y)

    slack_y = rect_height - last_origin[1] - h_max/2
    slack_x = rect_width - last_origin[0] - B/2

    for trapeze in trapezes:
        trapeze.update_points(slack_x/2, slack_y/2)

    return trapezes
    




def main(B_max, b_min, b_med, h_max, h_min, radius):
    
    trapezes = place_trapezes(B_max, b_min, b_med, h_max, h_min, radius)

    rotated_trapezes = place_rotated_trapezes(B_max, b_min, b_med, h_max, h_min, radius)
    
    if len(rotated_trapezes) > len(trapezes):
        for rotated_trapeze in rotated_trapezes:
            rotated_trapeze.invert_trapeze()
        return rotated_trapezes
    
    else:
        for trapeze in trapezes:
            trapeze.invert_trapeze()
        return trapezes