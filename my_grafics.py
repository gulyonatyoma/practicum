import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation

# Несоотвествие:
# dpi = 300 в обоих случаях и размеры на А6 (как в нашем случае)
# Линии траекторий цели и ракеты. Сплошные чёрные линии толщиной 0,5 мм
# Четверка в interval лишняя


def Grafics(my_table, Is_anim):
    # Функция строить как анимированную траекторию, так и статическую

    x_b, y_b = my_table["initial"]["baseX"], my_table["initial"]["baseY"]

    x_c, y_c = [x_b], [y_b]
    x_aim, y_aim = [], []

    for i in my_table["fly"]:
        x_c.append(i["catcherX"])
        y_c.append(i["catcherY"])
        x_aim.append(i["aimX"])
        y_aim.append(i["aimY"])

    if Is_anim == True:
        fig, ax = plt.subplots(figsize=(4.13*1.25, 5.83*1.25))

        def init():
            ax.set_xlim(0, 100000)
            ax.set_ylim(0, 32000)
            return fig,
        x1, y1, x2, y2 = [], [], [], []

        def animate(i):
            x1.append(x_c[i])
            y1.append(y_c[i])
            x2.append(x_aim[i])
            y2.append(y_aim[i])

            plt.plot(x1, y1, color="red", linewidth=1)
            plt.plot(x2, y2, color="blue", linewidth=1)

        res = FuncAnimation(
            fig, animate, init_func=init, interval=my_table["initial"]["oneTimeInterval"]*1000/8)
        # res.save('animation.gif')

    else:

        fig = plt.figure(figsize=(6, 8), linewidth=500000.0)
        plt.xlim([0, 100000])
        plt.ylim([0, 32000])
        for i in range(0, len(x_aim), 10):
            plt.plot([x_b, x_aim[i]], [y_b, y_aim[i]],
                     color="black", linewidth=0.15)

        plt.plot(x_c, y_c, color="red", linewidth=1,
                 marker='o', markeredgecolor='black', markersize=2, markerfacecolor='white', markeredgewidth=0.5)
        plt.plot(x_aim, y_aim, color="blue", linewidth=1,)

    plt.scatter(x_b, y_b, c='red')
    plt.show()
