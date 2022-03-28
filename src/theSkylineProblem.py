def skyline(predios):
    n = len(predios)
    if n == 0:
        return []
    if n == 1:
        L, R, altura = predios[0]
        return [[L, altura], [R, 0]]

    L = skyline(predios[:n // 2])
    R = skyline(predios[n // 2:])
   
    return merge(L, R)


def merge(L, R):
    lista = []
    i = 0  
    j = 0  
    LY = 0
    RY = 0

    while i < len(L) and j < len(R):
       
        if L[i][0] < R[j][0]:
            LY = L[i][1]  
            addPonto(lista, L[i][0], max(L[i][1], RY))
            i += 1
        else:
            RY = R[j][1]  
            addPonto(lista, R[j][0], max(R[j][1], LY))
            j += 1

    while i < len(L):
        addPonto(lista, L[i][0], L[i][1])
        i += 1

    while j < len(R):
        addPonto(lista, R[j][0], R[j][1])
        j += 1

    return lista
