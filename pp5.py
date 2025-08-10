def sierpinski_carpet(n, size=3 ** 3):
    carpet = [['█' for _ in range(size)] for _ in range(size)]

    def clear_square(x, y, s):
        if s < 1:
            return
        s //= 3
        for i in range(s, 2 * s):
            for j in range(s, 2 * s):
                carpet[x + i][y + j] = ' '
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    clear_square(x + i * s, y + j * s, s)

    clear_square(0, 0, size)
    for row in carpet:
        print(''.join(row))


sierpinski_carpet(2)