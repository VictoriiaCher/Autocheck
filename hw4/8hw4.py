def game(terra, power):
    for i in range(len(terra)):
        for j in range(len(terra[i])):
            if terra[i][j] <= power:
                power += terra[i][j]
            else:
                break
    return power


game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1)
