import folder_4.Main as m

def calculate_asymHex_dimensions(radius, compo):
    
    if compo == "3-4-5-4":
        B_max = 10.312 * radius
        b_min = 5.156 * radius
        b_med = 7.156 * radius
        h_max = 5.654 * radius
        h_min = 2.732 * radius

        return m.main(B_max, b_min, b_med, h_min, h_max, 2*radius)