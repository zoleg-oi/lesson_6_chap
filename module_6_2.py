# Изменять нельзя получать
class Vehicle:
    '''Данный клас обеспечивает проверку на возможность изменения цвета в каталоге
    и если возможно, меняет цвет в соответствии с каталогом, а так же может изменить владельца
    выводит данные о модели и мощности двигателя
    реализованы атрибуты
    owner - хозяин автомобиля
    model - модель автомобиля(неизменяемый)
    engine_power - мощность двигателя(неизменяемый)
    color - цвет автомобиля(неизменяемый)
    COLOR_VARIANTS - каталог цветов(неизменяемый)
    реализованы методы
    get_model - вывод модели автомобиля
    get_horsepower - вывод мощности двигателя
    get_color - вывод цвета автомобиля
    set_color - изменение цвета автомобиля в соответствии с каталогом
    print_info - печать информации об автомобиле'''

    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ['красный', 'синий', 'белый', 'зеленЫй', 'черный']

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if isinstance(new_color, str):
            nc = new_color.lower()
        else:
            nc = str(new_color).lower()
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    ''' наследует класс Vehicle
    при создании экземпляра передает данные, содержащие параметры автомобиля
    в родительский класс
    реализован атрибут
    PASSENGERS_LIMIT - количество пассажиров в салоне(неизменяемый)'''
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, horsepower):
        # Передаем данные в родительский класс
        super(Sedan, self).__init__()
        self._Vehicle__model = model
        self._Vehicle__engine_power = horsepower
        self._Vehicle__color = color
        self.owner = owner


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Розовый')
vehicle1.set_color('ЧЕРНЫй')
vehicle1.owner = 'Васёк'

# Проверяем что поменялось
vehicle1.print_info()
