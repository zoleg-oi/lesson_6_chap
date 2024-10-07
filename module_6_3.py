# Мифическое наследование

# Данное решение использует super()
# Но можно подойти и другим образом
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        mx = super().run(dx)
        my = super().fly(dy)

    def get_pos(self):
        x = self.x_distance
        y = self.y_distance
        return (x, y)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# Вариант два без использования super()
print()
print('Вариант два, без использования super()')
print()


class Horse2:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle2:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus2(Horse2, Eagle2):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle2.sound)


p2 = Pegasus2()

print(p2.get_pos())
p2.move(10, 15)
print(p2.get_pos())
p2.move(-5, 20)
print(p2.get_pos())

p2.voice()
