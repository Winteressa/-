"""2)	Создайте базовый класс Vehicle, который будет иметь атрибуты make, model и year.
Затем создайте подклассы Car и Truck, добавив атрибуты, специфичные для каждого типа
(например, passenger_capacity для автомобиля и payload_capacity для грузовика).
Реализуйте метод для отображения информации о транспортном средстве."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"вы купили: {self.make} , модель: {self.model}, год производства:{self.year} "

    def getinf(self):
        return self.__str__()

class Car(Vehicle):
    def __init__(self, make, model, year, passenger_capacity):
        super().__init__(make, model, year)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"{super().__str__() } пассажирской вместимостью {self.passenger_capacity} "


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return f"{super().__str__() } с загрузкой {self.payload_capacity} "


Vehicle = Car("China", "xiaoumi", "2012", "200")
print(Vehicle)

Vehicle = Truck("russia", "zil", "1991", "1000")
print(Vehicle)
zil = Truck("russia", "zil", "1991", "1000")
print(zil.getinf())

"""3)	Создайте базовый класс Animal, который будет иметь атрибуты name и species. 
Затем создайте подклассы Mammal и Bird, добавив методы, специфичные для каждого класса 
(например, метод make_sound() для млекопитающих и метод fly() для птиц)."""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"перед вами: {self.name} , вид: {self.species}"

class Mammal(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species)
        self.sound = sound

    def Make_sound(self):
        return f"{super().__str__() } и издает следующийй звук: {self.sound} "


class Bird(Animal):
    def __init__(self, name, species, fly_or_not):
        super().__init__(name, species)
        self.fly_or_not = fly_or_not

    def fly(self):
        return f"{super().__str__() } и это чудовище {self.fly_or_not} "

    # def getinf(self):
    #     return self.__str__()


cow = Mammal("корова", "альпийская", "мууууу")
print(cow.Make_sound())
chiken = Bird("курица", "домашняя", ",слава богу, не летает")
print(chiken.fly())

"""5)	Создайте базовый класс Event, который будет иметь атрибуты event_name, date и location. 
Затем создайте подклассы Concert и Conference, добавив атрибуты, специфичные для каждого типа 
(например, performer для концерта и speakers для конференции). 
Реализуйте метод для отображения информации о событии."""

class Event:
    def __init__(self, event_name, date, location):
        self.event_name = event_name
        self.date = date
        self.location = location

    def __str__(self):
        return f"вы хотите пойти на: {self.event_name} , которое состоится {self.date}, пройдет {self.location}"

    def AboutEvent(self):
        return f"{self.__str__() }"
class Consert(Event):
    def __init__(self, event_name, date, location, performer):
        super().__init__(event_name, date, location)
        self.performer = performer

    def __str__(self):
        return f"{super().__str__() } , и перед вами выступит {self.performer}"


class Conference(Event):
    def __init__(self, event_name, date, location, speaker):
        super().__init__(event_name, date, location)
        self.speaker = speaker

    def __str__(self):
        return f"{super().__str__() } , и спикером будет {self.speaker}"




JesusAppearance = Conference("Явление Христа народу", "25.12.3000", "на краю земли", "Джисус собственной персоной")
print(JesusAppearance.AboutEvent())
jacksonConcert = Consert("Концерт под Луной", "сегодня и прямо сейчас", "у тебя под окном", "Майкл Джексон")
print(jacksonConcert.AboutEvent())


