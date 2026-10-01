def donas_consumidas (a, b):
    
    
    if type(a) is not int:
        raise TypeError ("debe ser int")
    if type(b) is not int:
        raise TypeError ("debe ser int")
    if a < 0 or b < 0:
        raise ValueError ("a y b no pueden ser negativos")

    comidas = 0

    for x in range (b):
        comidas += a
    
    return comidas