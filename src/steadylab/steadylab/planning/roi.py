from typing import List, Tuple, Sequence, Union

def roi(imgsz: Union[int, int], ratio: Union[float, float]):
    """
    coords -> [x1, y1, x2, y2, x3, y3, x4, y4]
    """
    w, h = imgsz
    r = ratio
    x1, y1, x2, y2, x3, y3, x4, y4 = \
        [int(w*(1 - r[0])*0.5), h // 2,     # upper left
         int(w - w*(1 - r[0])*0.5), h // 2, # upper right
         int(w*(1 - r[1])*0.5), h,     # upper left
         int(w - w*(1 - r[1])*0.5), h] # upper right
    
    print(imgsz)
    print(ratio)
    print(x1, y1, x2, y2, x3, y3, x4, y4)
    min_x = min(x1, x2, x3, x4)
    max_x = max(x1, x2, x3, x4)
    min_y = min(y1, y2, y3, y4)
    max_y = max(y1, y2, y3, y4)

    roi_coordinates = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (
                (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) >= 0 and
                (x3 - x2) * (y - y2) - (x - x2) * (y3 - y2) >= 0 and
                (x4 - x3) * (y - y3) - (x - x3) * (y4 - y3) >= 0 and
                (x1 - x4) * (y - y4) - (x - x4) * (y1 - y4) >= 0
            ):
                roi_coordinates.append((x, y))
    return roi_coordinates