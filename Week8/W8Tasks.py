import matplotlib.pyplot as plt


def display_line(xvals, yvals):
    plt.plot(xvals, yvals)
    plt.show()


def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)


# run_task1()

# ----------

def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'ro:')
    #plt.show()


def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'gs--')
    #plt.show()


def large():
    x = [1, 6, 6, 1, 1]
    y = [1, 1, 6, 6, 1]
    plt.plot(x, y, 'bs-')
    #plt.show()


def display_squares():
    small()
    medium()
    large()
    plt.show()


display_squares()
