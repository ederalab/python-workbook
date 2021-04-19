# line of best fit

x = (1, 2, 3)
y = (1, 2.1, 2.9)

def bestFit(x,y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = 0
    sum_xx = 0

    n = len(x)
    avg_x = sum_x / n
    avg_y = sum_y / n

    for nx, ny in zip(x, y):
        sum_xy = sum_xy + (nx * ny)
        sum_xx = sum_xx + nx**2

    #y = mx + b
    m = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_xx) - (sum_x**2))
    b = avg_y - m * avg_x

    print("y = %.2fx + %.2f" % (m, b))


bestFit(x,y)
