# Зачем нужно наследование
class Animal:
    ''' Класс имеет следующие атрибуты
    name - Имя животного
    alive - определяет его состояние жив или нет
    fed - определяет сытость животного
    класс имеет следующие методы
    eat в данном методе определяется какая пища попала животному
    и как он реагирует на это
    класс получает параметр - наименование животного'''
    name = ''
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            self.alive = True
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            self.fed = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    ''' Клас имеет следующие атрибуты
    name название растения
    edible съедобность данного растения
    класс получает параметр наименование растения'''
    name = ''
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    '''Класс наследует методы и атрибуты класса - Animal'''
    pass


class Mammal(Animal):
    '''Класс наследует методы и атрибуты класса - Animal'''
    pass


class Flower(Plant):
    '''Класс наследует методы и атрибуты класса - Plant
    и изменяет атрибут edible(съедобность)'''
    edible = False


class Fruit(Plant):
    '''Класс наследует методы и атрибуты класса - Plant
    и изменяет атрибут edible(съедобность)'''
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal("Хатико")
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
