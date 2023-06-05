from folder_3 import Trapeze as t

rect_height = 104
rect_width = 124

def place_trapezes(B, b, h):
    
    origin = [B/2, h/2]
    trapezes = []
    
    while True:
        
        origin[0] = B/2
        
        while True:
            
            trapezes.append(t.Trapeze(B, b, h, origin[0], origin[1]))
            if origin[0] + B + B/2 + 0.2> rect_width:
                break
            else:
                origin[0] += B + 0.2
                
        if origin[1] + h + h/2 + 0.2 > rect_height:
            break
        else:
            origin[1] += h + 0.2

    last_origin = (trapezes[-1].origin_x, trapezes[-1].origin_y)
    
    slack_y = rect_height - last_origin[1] - h/2
    slack_x = rect_width - last_origin[0] - B/2
    
    for trapeze in trapezes:
        trapeze.update_points(slack_x/2, slack_y/2)
        
    
    return trapezes
    




def main(B, b, h):
    
    trapezes = place_trapezes(B, b, h)
    
    return trapezes