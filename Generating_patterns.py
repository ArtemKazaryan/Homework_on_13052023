
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!

# Домашняя работа на 13.05.2023.

# Модуль 12. Паттерны проектирования
# Тема: Паттерны проектирования. Часть 1


# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №1:', '*'*11)

class Sandwich:
    def __init__(self):
        self.sandwich_basis = None
        self.first_top_layer = None
        self.second_top_layer = None

    def __str__(self):
        print('- '*25)
        return f'Жена принесла мне бутерброд и сказала, что сделала всё как я просил:\n' \
               f'- она взяла {self.sandwich_basis},\n' \
               f'- сверху положила {self.first_top_layer},\n' \
               f'- и всё это покрыла {self.second_top_layer}.\n' \
               f'И пожелала мне приятного аппетита!\n' \
               f'Умничка!'

class SandwichMaker:
    def __init__(self):
        self.delicious_sandwich_in_front_of_me = Sandwich()

    def take_sandwich_basis(self, sandwich_basis):
        self.delicious_sandwich_in_front_of_me.sandwich_basis = sandwich_basis

    def as_the_first_layer_put(self, first_top_layer):
        self.delicious_sandwich_in_front_of_me.first_top_layer = first_top_layer

    def as_the_second_layer_put(self, second_top_layer):
        self.delicious_sandwich_in_front_of_me.second_top_layer = second_top_layer

    def give_me_a_readymade_sandwich(self):
        return self.delicious_sandwich_in_front_of_me

class HusbandOrderIs:
    @staticmethod
    def make_me_tender_sandwich(wife):
        wife.take_sandwich_basis('кусочек белого хлеба 5x8x1.5')
        wife.as_the_first_layer_put('кусочек варёной колбасы 5x8x0.5')
        wife.as_the_second_layer_put('кусочком голандского сыра 5x8x0.2')

    @staticmethod
    def make_me_smoked_sandwich(wife):
        wife.take_sandwich_basis('кусочек чёрного хлеба 10x8x1.5')
        wife.as_the_first_layer_put('кусочек копчёной колбасы 5x8x0.5')
        wife.as_the_second_layer_put('кусочком свежего томата 5x8x0.2 с зеленью')

    @staticmethod
    def make_me_spicy_sandwich(wife):
        wife.take_sandwich_basis('половинку гамбургерной булочки')
        wife.as_the_first_layer_put('кусочек ветчины по размеру основы')
        wife.as_the_second_layer_put('острым томатным соусом с оливками')

if __name__ == '__main__':
    wife = SandwichMaker()

    HusbandOrderIs.make_me_tender_sandwich(wife)
    delicious_sandwich_in_front_of_me = wife.give_me_a_readymade_sandwich()
    print(delicious_sandwich_in_front_of_me)

    HusbandOrderIs.make_me_smoked_sandwich(wife)
    delicious_sandwich_in_front_of_me = wife.give_me_a_readymade_sandwich()
    print(delicious_sandwich_in_front_of_me)

    HusbandOrderIs.make_me_spicy_sandwich(wife)
    delicious_sandwich_in_front_of_me = wife.give_me_a_readymade_sandwich()
    print(delicious_sandwich_in_front_of_me)


# Задание 2
# Создайте приложение для приготовления пасты.
# Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №2:', '*'*11)

class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.fillings = []
        self.add_ons = []

    def prepare(self):
        print(f"Приготовить {self.type} пасту с соусом {self.sauce} ...")
        if self.fillings:
            print("Добавление начинок:")
            for filling in self.fillings:
                print(f"- {filling}")
        if self.add_ons:
            print("Дополнительные добавки:")
            for add_on in self.add_ons:
                print(f"- {add_on}")
        print("Паста готова!")


class Spaghetti(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Спагетти"
        self.sauce = "Помидор"
        self.fillings = ["Фрикадельки"]
        self.add_ons = ["Сыр Пармезан"]

class Fettuccine(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Феттучини"
        self.sauce = "Альфредо"
        self.fillings = ["Курица"]
        self.add_ons = ["Чесночный хлеб"]

class Penne(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Пенне"
        self.sauce = "Песто"
        self.fillings = ["Грибы"]
        self.add_ons = ["Листья базилика"]

class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "Спагетти":
            return Spaghetti()
        elif pasta_type == "Феттучини":
            return Fettuccine()
        elif pasta_type == "Пенне":
            return Penne()
        else:
            return None

if __name__ == '__main__':
    pasta_type = input("Введите тип пасты, которую вы хотите приготовить (Спагетти, Феттучини, Пенне): ")
    pasta = PastaFactory.create_pasta(pasta_type)
    if pasta:
        pasta.prepare()
    else:
        print("Недопустимый тип пасты!")

# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №3:', '*'*11)

import copy

class Prototype:
    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        self.objects[name] = obj

    def unregister_object(self, name):
        del self.objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(kwargs)
        return obj

class Car:
    def __init__(self):
        self.color = None
        self.wheels = None
        self.engine = None

    def __str__(self):
        return f'Color: {self.color}, Wheels: {self.wheels}, Engine: {self.engine}'


if __name__ == '__main__':
    prototype = Prototype()

car = Car()
car.color = 'Red'
car.wheels = 4
car.engine = 'V8'

print(f'Оригинал объекта car: {car}')

prototype.register_object('Red sports car', car)

car_clone = prototype.clone('Red sports car', color='Blue')
print(f'Клон объекта car: {car_clone}')