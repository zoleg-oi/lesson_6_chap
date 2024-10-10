# Они все так похожи
from math import sqrt


class Figure:
    '''Данный клас реализует проверку, запись, вывод параметров геометрических фигур
    реализованы атрибуты
    sides_count - количество сторон фигуры
    filled - заливка
    __sides - хранит длины сторон геометрических фигур в формате list
    __color - хранит цвет геометрической фигуры в формате tuple
    реализованы методы
    Основные:

    __init__
        в данном методе реализована дополнительная проверка вводимых параметров
    __is_valid_color
        данный метод проверяет вводимые параметры по цвету
        по критериям:
        параметры должны быть целыми положительными числами
        параметры должны входить в диапазон определения RGB
    __is_valid_sides
         в данный метод проверяет вводимые параметры по длинам и количеству сторон
         геометрической фигуры по критериям:
         количество параметров должно соответствовать количеству сторон геометрической фигуры
         параметры должны быть положительными целыми числами
    set_color
        метод реализует запись данных цвета, с предварительной проверкой
    set_sides
        метод реализует запись данных геометрической фигуры с предварительной проверкой
    get_color
        метод выводит данные по цвету геометрической фигуры
    get_sides
        метод выводит данные о длине сторон геометрической фигуры
    __len__
        метод выводит длину периметра геометрической фигуры

    Дополнительные методы
    __save_color
        данный метод осуществляет сохранение параметров цвета в формате (R,G,B)
        осуществляется дополнительная проверка корректности ввода параметров цвета
        по критериям заполненности параметров RGB.
        проверяется количество введенных параметров на соответствие RGB формату, а так же
        корректность ввода значений формата RGB. Если присутствует ошибка, запись не производится
    __save_sides
     с помощью данного метода идет сохранение сторон геометрических фигур
     осуществляется дополнительная проверка корректности ввода данных
     по следующим параметрам
     соответствие количества параметров сторонам геометрической фигуры
     возможность построения геометрических фигур на основе этих параметров
     если присутствуют ошибки запись не осуществляется
     __check_val
     данный метод вызывается при создании объекта
     осуществляет проверку ввода данных параметров, отвечающих за ввод сторон геометрической фигуры
     по критериям
     количество параметров
     возможность создания геометрической фигуры на основе данных параметров
     при возникновении ошибок записывает число - 1 в соответствии с количеством сторон

    '''

    sides_count = 0
    filled = False
    __sides = []
    __color = ()

    def __init__(self, *param):  # параметры принимаем:  кортеж RGB (int,int,int), далее длины сторон (int)
        if len(param) <= 1:  # проверим корректность ввода
            print(f'Недостаточно параметров, {'\n'}1 параметр - цвет, имеет вид:(int,int,int) {'\n'}'
                  f'далее параметры, определяющие длины сторон геометрических фигур, имеют формат - int')

            return
        else:
            param_sides = list(param)
            param_sides.pop(0)
            self.__check_val(*param_sides)
            self.set_sides(*param_sides)
            if (isinstance(param[0], tuple) and len(
                    param[0]) == 3) == False:  # проверим корректность ввода параметров цвета
                print(f'Введен неправильный параметр цвета - {param[0]}, требуется ввод вида - (int,int,int)')
                return
            else:
                self.set_color(*param[0])

    def __check_val(self, *param):
        lp = len(param)
        flag = False
        if self.sides_count == 1:  # circle
            if lp != 1:
                # Если количество переданных параметров для круга отличается от одного, то заполнить единицей
                self.__sides.append(1)
        elif self.sides_count == 3:  # triangle
            if lp != 3:
                # Если количество переданных параметров для треугольника отличается от трех, то заполнить стороны единицей
                flag = True
            else:
                # Проверить возможность существования треугольника
                # Если треугольник невозможно построить по заданным отрезкам
                # заполнить длины сторон - 1
                if (param[0] + param[1] > param[2] and param[0] + param[2] > param[1] and param[1] + param[2] > param[
                    0]) != True:
                    flag = True
        elif self.sides_count == 12:  # cube
            if lp != 1:
                # Если количество переданных параметров отлично от 1 то заполнить стороны единицей
                flag = True

        if flag:  # Если все неправильно, заполнить единицами.
            for i in range(0, self.sides_count):
                self.__sides.append(1)

    def __save_color(self, paramRGB):
        if isinstance(paramRGB, tuple) and len(paramRGB) == 3:
            self.__color = paramRGB
        else:
            print(f'Параметр, определяющий цвет {paramRGB} введен неправильно, должен иметь вид - (int,int,int) ')
            return

    def __save_sides(self, param):
        lp = len(param)
        flag = False
        if self.sides_count == 1 and lp == 1:  # circle
            flag = True
        elif self.sides_count == 3:  # triangle
            if lp == 3:
                # Проверить возможность существования треугольника
                # Если треугольник невозможно построить по заданным отрезкам
                # заполнить длины сторон - 1
                if param[0] + param[1] > param[2] and param[0] + param[2] > param[1] and param[1] + param[2] > param[0]:
                    flag = True
        elif self.sides_count == 12:  # cube
            if lp == 1:
                flag = True
        if flag:
            self.__sides = []
            if self.sides_count == 12 and lp == 1:
                for i in range(0, self.sides_count):
                    self.__sides.append(param[0])
            else:
                self.__sides = list(param)

    def __is_valid_color(self, paramRGB):
        value = False
        for ic in paramRGB:
            if isinstance(ic, int) and ic >= 0 and ic <= 255:
                value = True
            else:
                return False
        if value:
            return True

        return value

    def __is_valid_sides(self, param_sides):
        value = False
        if len(param_sides) != self.sides_count:
            value = False
            # Для обработки сторон куба считаем, что больше одного параметра не принимаем
            if (self.sides_count == 12 and len(param_sides) == 1) != True:
                value = False
        for ip in param_sides:
            if isinstance(ip, int) and ip >= 0:
                value = True
            else:
                return False
        return value

    def __len__(self):
        summa = 0
        if len(self.__sides) != 0:
            for i in range(0, self.sides_count):
                summa += self.__sides[i]
        return summa

    def set_color(self, *paramRGB):
        if self.__is_valid_color(paramRGB):  # Проверить данные
            self.__save_color(paramRGB)  # Записать данные

    def set_sides(self, *param_sides):
        if self.__is_valid_sides(param_sides):  # Проверить данные
            self.__save_sides(param_sides)  # Записать данные

    def get_color(self):
        if len(self.__color):
            return (self.__color)
        else:
            return ('Цвет не определен')

    def get_sides(self):
        return (self.__sides)


class Circle(Figure):
    ''' Класс осуществляет ввод данных по окружности'''

    def __init__(self, *param):
        self.sides_count = 1
        super().__init__(*param)


class Triangle(Figure):
    ''' Класс осуществляет ввод данных по треугольнику
    методы
    get_square
        Метод вычисляет площадь треугольника'''

    def __init__(self, *param):
        self.sides_count = 3
        super().__init__(*param)

    def get_square(self):
        if len(self._Figure__sides) == 3:  # проверяем наличие требуемых данных
            pp = self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]
            pp = pp / 2
            return round(sqrt(
                pp * (pp - self._Figure__sides[0]) * (pp - self._Figure__sides[1]) * (pp - self._Figure__sides[2])), 2)
        else:
            return 0


class Cube(Figure):
    ''' Класс осуществляет вывод данных по кубу
    методы
    get_volume
        вычисляет объем куба'''

    def __init__(self, *param):
        self.sides_count = 12
        super().__init__(*param)

    def get_volume(self):
        if len(self._Figure__sides) > 0:
            return self._Figure__sides[0] ** 3
        else:
            return 0


# Проверки действия кода по заданию
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle((255, 255, 255), 15, 17, 18)
print(triangle1.get_sides())
print(triangle1.get_square())
