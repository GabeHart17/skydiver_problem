import matplotlib.pyplot as plt
import numpy as np


# change these to fit problem

# x is time
# y is velocity


x_0 = 0
x_max = 50
delta_x = 0.05
y_0 = 0

def diff_eq(x, y):
    k = (0.57 * 1.3 * 0.7) / (2 * 75)
    return -9.8 + k * (y ** 2)



# don't change this
x = [x_0]
y = [y_0]

h = [2000]

def de_step():
    y.append(y[-1] + delta_x * diff_eq(x[-1], y[-1]))
    x.append(x[-1] + delta_x)

if __name__ == "__main__":
    for i in range(round((x_max - x_0) / delta_x)):
        de_step()
        h.append(h[-1] + y[-1] * delta_x)

    for i in range(len(h) - 1):
        if h[i] >= 0 and h[i+1] < 0:
            print(f'at ground:\nvelocity: {y[i]}, time: {x[i]}')
            break

    fig, plts = plt.subplots(1, 2)
    hplt = plts[0]
    yplt = plts[1]
    hplt.plot(x, h, 'b.')
    yplt.plot(x, y, 'b.')
    hplt.set_xlabel('time')
    hplt.set_ylabel('height')
    yplt.set_xlabel('time')
    yplt.set_ylabel('velocity')
    # plt.title(f'initial: ({x[0]}, {y[0]})     final: ({x[-1]}, {y[-1]})')

    plt.show()
