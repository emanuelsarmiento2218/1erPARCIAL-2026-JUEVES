def interrupciones(a, b):

    if type(a) is not int:
        raise TypeError ("debe ser int")
    if type(b) is not int:
        raise TypeError ("debe ser int")
    if a < 0 or b < 0:
        raise ValueError ("a y b no pueden ser negativos")

    if b == 0:
        return 0
    
    return a + interrupciones(a, b - 1)
