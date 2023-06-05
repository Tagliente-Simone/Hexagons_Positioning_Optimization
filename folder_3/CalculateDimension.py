import folder_3.Main as m

def calculate_trapeze_dimensions(radius):
    
    B_max = 9.468 * radius
    b_min = 5.158 * radius
    h = 3.723 * radius
    
    return m.main(B_max, b_min, h)
    
    