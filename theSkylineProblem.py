def skyline(predios):
    n = len(predios)
    if n == 0:
        return []
    if n == 1:
        L, R, altura = predios[0]
        return [[L, altura], [R, 0]]

    L = skyline(predios[:n // 2])
    R = skyline(predios[n // 2:])
    