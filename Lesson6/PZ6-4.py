"""
Практическое задание 6-4

Реализуйте базовый класс Car.

У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат
"""
def output_car(o_car, type, speed1, direction, speed2):
    """
    Процедура вывода данных об автомобиле
    
    o_car - объект автомобиль
    type - тип автомобиля
    speed1 - скорость по прямой
    direction - направление поворота
    speed2 - скорость после поворота
    
    """
    print(f"Переданные значения.\n{type} автомобиль марки - {o_car.name}, цвет {o_car.color}, скорость движения {o_car.speed}")
    print("-" * 50)
    print(f"{o_car.go()}. {o_car.show_speed(speed1)}") 
    print(f"{o_car.turn(direction)}. {o_car.show_speed(speed2)}") 
    print(f"{o_car.stop()}")
    print("*" * 50, "\n")


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return "Автомобиль начал движение"

    def stop(self):
        return "Автомобиль остановился"

    def turn(self, direction):
        return(f"Автомобиль повернул {direction}")
        
    def show_speed(self, speed):
        return(f"Скорость автомобиля {speed} км/ч")

class TownCar(Car):
     
     def show_speed(self, speed):
        if speed <= 60:
            return(f"Скорость автомобиля {speed} км/ч")
        else:
            return(f"Скорость превысил на {(speed - 60)} км/ч")
     
class SportCar(Car):
    
     pass

class WorkCar(Car):
     
     def show_speed(self, speed):
        if speed <= 40:
            return(f"Скорость автомобиля {speed} км/ч")
        else:
            return(f"Скорость превысил на {(speed - 40)} км/ч")

class PoliceCar(Car):
     
     pass

t_car = TownCar(80, "серебристый", "Мазда", False)
if t_car.is_police == False:
    f = 'Городской'
else:
    f = 'Полицейский'
output_car(t_car, f, 50, "направо", 90)

s_car = SportCar(120, "красный", "Феррари", False)
if t_car.is_police == False:
    f = 'Спортивный'
else:
    f = 'Полицейский'
output_car(s_car, f, 150, "налево", 60)

w_car = WorkCar(50, "черный", "ВАЗ", False)
if t_car.is_police == False:
    f = 'Рабочий'
else:
    f = 'Полицейский'
output_car(w_car, f, 60, "направо", 35)

p_car = PoliceCar(100, "бело-синий", "Тойота", True)
if t_car.is_police == False:
    f = 'Служебный'
else:
    f = 'Полицейский'
output_car(p_car, f, 150, "налево",90)