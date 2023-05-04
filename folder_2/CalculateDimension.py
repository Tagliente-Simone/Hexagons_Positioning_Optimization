from folder_2 import Main as m



def compute(radius, min, max, rows):



    cost = 0

    if int(rows) == 5:
        cost = 8.928
    elif int(rows)  == 7:
        cost = 6.196 * 2
    elif int(rows)  == 9:
        cost = 15.85

    l = radius * cost
    L = radius * max * 2

    if l < L:
        ratio = L/l
    else:
        ratio = l/L



    if ratio > 1.14 or ratio < 1.12:
        print("ratio not good")
        return -1

    rectangle = m.main(L, l)

    total_tubes = len(rectangle) * (max * (int(int(rows) / 2)) + min * (int(rows) - int(int(rows) / 2)))
    
    

    return total_tubes

    