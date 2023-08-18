def compute_poly(poly_list, x):
    result = int(poly_list[0])
    size = len(poly_list)
    for i in range(1, size):
        result = result * x + int(poly_list[i])
    return result