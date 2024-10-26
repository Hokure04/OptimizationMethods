import math


def get_method():
    print('\t', '1: Метод половинного деления.')
    print('\t', '2: Метод золотого сечения.')
    print('\t', '3: Метод хорд.')
    print('\t', '4: Метод Ньютона.')
    param = int(input('Введите номер метода, который хотите использовать: '))
    if param == 1:
        a, b, E = get_parametr()
        half = Half(a, b, E)
        half.check()
    elif param == 2:
        a, b, E = get_parametr()
        ratio = Golden_Ratio(a, b, E)
        ratio.first_iteration()
    elif param == 3:
        a, b, E = get_parametr()
        chord_method(a, b, E)
    elif param == 4:
        a, b, E = get_parametr()
        x0 = (a + b) / 2
        y = newton_method(E, x0)
        print(y)


def get_parametr():
    a = int(input("Введите точку a: "))
    b = int(input("Введите точку b: "))
    E = float(input("Введите точность E: "))
    return a, b, E


def newton_method(e, x0):
    df_y = df(x0)
    double_df_y = double_df(x0)
    x = x0 - df_y / double_df_y
    print('Значение x0: ' + str(x))

    while abs(df(x)) > e:
        iteration = 1
        while iteration < 100:
            x = scope(x, iteration)
            iteration += 1
            # print(iteration)
        return 'Данный метод расходится'


def scope(x, iteration):
    df_y = df(x)
    double_df_y = double_df(x)
    x = x - df_y / double_df_y
    print('Значение x' + str(iteration) + ': ' + str(x))
    return x


def chord_method(a, b, e):
    y_dfa = df(a)
    y_dfb = df(b)
    x = a - (y_dfa / (y_dfa - y_dfb)) * (a - b)
    print('Значение x: ' + str(x))

    y = df(x)
    print('Значение y: ' + str(y))

    if (abs(y) <= e):
        return x, func(x)

    if y > 0 and y < 1:
        return chord_method(a, x, e)
    elif y < 0:
        return chord_method(x, b, e)
    elif y >= 1:
        print('Данный метод расходится')
        return


def df(x):
    y = x / math.sqrt(1 + x ** 2) + 2 * math.e ** (-2 * x)
    return y


def double_df(x):
    y = -4 * math.e ** (-2 * x) + 1 / math.sqrt(x ** 2 + 1) - x ** 2 / (x ** 2 + 1) ** (3 / 2)
    return y


def func(x):
    """
    Вычисляем значение функции, в качестве примера
    """
    return math.sqrt(1 + x ** 2) - math.e ** (-2 * x)


class Half:
    a = 0
    b = 0
    E = 0

    def __init__(self, a, b, E):
        self.a = a
        self.b = b
        self.E = E

    def check(self):
        while abs(self.a - self.b) > 2 * self.E:
            self.calculate()
        xm = (self.b + self.a) / 2
        ym = func(xm)
        print('Координата xm равна: ' + str(xm))
        print('Координата ym равна: ' + str(ym))

    def calculate(self):
        x1 = (self.a + self.b - self.E) / 2
        print('Значение x1 равно:' + str(x1))
        x2 = (self.a + self.b + self.E) / 2
        print('Значение x2 равно:' + str(x2))
        y1 = func(x1)
        print('Значение y1 равно:' + str(y1))
        y2 = func(x2)
        print('Значение y2 равно:' + str(y2))
        if y2 > y1:
            print('y2 > y1 => b = ' + str(x2))
            self.b = x2
        else:
            print('y1 > y2 => b = ' + str(x1))
            self.a = x1


class Golden_Ratio:
    small_part = 0.382
    big_part = 0.618
    a = 0
    b = 0
    E = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    def __init__(self, a, b, E):
        self.a = a
        self.b = b
        self.E = E

    def first_iteration(self):
        self.x1 = self.a + self.small_part * (self.b - self.a)
        print('Значение x1 равно:' + str(self.x1))
        self.x2 = self.a + self.big_part * (self.b - self.a)
        print('Значение x2 равно:' + str(self.x2))
        self.y1 = func(self.x1)
        print('Значение y1 равно:' + str(self.y1))
        self.y2 = func(self.x2)
        print('Значение y2 равно:' + str(self.y2))
        if self.y2 > self.y1:
            self.b = self.x2
            print('y2 > y1 => b = ' + str(self.b))
            self.second_iteration_y2()
        else:
            self.a = self.x1
            print('y1 > y2 => a = ' + str(self.a))
            self.second_iteration_y1()

    def second_iteration_y2(self):
        while abs(self.a - self.b) > self.E:
            self.x2 = self.x1
            self.x1 = self.a + self.small_part * (self.b - self.a)
            print('Значение x1 равно:' + str(self.x1))
            print('Значение x2 равно:' + str(self.x2))
            self.y2 = self.y1
            self.y1 = func(self.x1)
            print('Значение y1 равно:' + str(self.y1))
            print('Значение y2 равно:' + str(self.y2))
            if self.y2 > self.y1:
                self.b = self.x2
                print('y2 > y1 => b = ' + str(self.b))
        xm = self.x2
        ym = self.y2
        print('Координата xm равна: ' + str(xm))
        print('Координата ym равна: ' + str(ym))

    def second_iteration_y1(self):
        while abs(self.a - self.b) > self.E:
            self.x1 = self.x2
            print('Значение x1 равно:' + str(self.x1))
            self.x2 = self.a + self.big_part * (self.b - self.x1)
            print('Значение x2 равно:' + str(self.x2))
            self.y1 = self.y2
            print('Значение y1 равно:' + str(self.y1))
            self.y2 = func(self.x2)
            print('Значение y2 равно:' + str(self.y2))
            if self.y1 > self.y2:
                self.a = self.x1
                print('y1 > y2 => a = ' + str(self.a))
        xm = self.x2
        ym = self.y2
        print('Координата xm равна: ' + str(xm))
        print('Координата ym равна: ' + str(ym))


get_method()
