def skyline(predios):
    n = len(predios) # Retorna o número de itens da lista
    if n == 0:
        return []
    if n == 1:
        L, R, altura = predios[0] # L: ponto à esquerda; R: ponto à direita; altura do prédio
        return [[L, altura], [R, 0]]

    L = skyline(predios[:n // 2]) 
    R = skyline(predios[n // 2:])
   
    return merge(L, R) # Chamada para função mergesort

def merge(L, R): # Função mergesort
    lista = []
    i = 0  # Índice da esquerda
    j = 0  # Índice da direita
    LY = 0
    RY = 0

    while i < len(L) and j < len(R):
       
        if L[i][0] < R[j][0]:
            LY = L[i][1]  # Atualizando o progresso da esquerda
            addPonto(lista, L[i][0], max(L[i][1], RY))
            i += 1
        else:
            RY = R[j][1]  # Atualizando o progresso da direita
            addPonto(lista, R[j][0], max(R[j][1], LY))
            j += 1

    while i < len(L):
        addPonto(lista, L[i][0], L[i][1])
        i += 1

    while j < len(R):
        addPonto(lista, R[j][0], R[j][1])
        j += 1

    return lista

def addPonto(lista, x, y): # Acrescentando mais pontos na lista
    if lista and lista[-1][0] == x:
        lista[-1][1] = y
        return
    if lista and lista[-1][1] == y:
        return
    lista.append([x, y])

# Casos de teste

# predios = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
predios = [[0,2,3],[2,5,3]]
# predios = [[1,5,7],[3,6,12],[7,11,15]]

print(skyline(predios))
