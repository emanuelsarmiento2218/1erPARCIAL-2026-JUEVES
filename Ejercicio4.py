def funcion(eventos, expresion_booleana):
    if type(eventos) is not list:
        raise TypeError ("eventos debe ser uina lista")
    if type(expresion_booleana) is not bool:
        raise TypeError ("debe ser booleano")

    if expresion_booleana == False:
        return sorted (eventos)
    else:
        return sorted (eventos, reverse =True)
