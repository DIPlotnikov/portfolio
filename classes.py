#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Простая программа для работы с классами. Включает функцию импорта данных из csv таблиц.

# D.Plotnikov 2021

import os
import csv


class CarBase:
    """Базовый класс для всех типов машин"""

    def __init__(self, brand, photo_file_name, carrying):
        if os.path.splitext(photo_file_name)[1] in [".jpg", ".jpeg", ".png", ".gif"]:
            self.photo_file_name = photo_file_name
        else:
            print("error")
        if brand != "":
            self.brand = brand
        else:
            print("error")
        if carrying != "0":
            self.carrying = float(carrying)
        else:
            print("error")


    def get_photo_file_ext(self):
        """Возвращает расширения файла изображения."""
        return os.path.splitext(self.photo_file_name)[1]


class Truck(CarBase):
    """Класс для работы с грузовыми машинами"""

    def __init__(self, brand, photo_file_name, carrying, body_whl="0x0x0"):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.whl = list(map(float, body_whl.split("x")))
            self.body_whl = body_whl
            if len(self.whl) != 3:
                print("error")
        except:
            self.whl = [0.0, 0.0, 0.0]
            self.body_whl = "0x0x0"
        self.car_type = "truck"
        self.body_length = self.whl[0]
        self.body_width = self.whl[1]
        self.body_height = self.whl[2]

    def get_body_volume(self):
        """возвращает объем кузова"""
        return self.whl[0] * self.whl[1] * self.whl[2]


class Car(CarBase):
    """Класс для работы с легковыми автомобилями"""

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class SpecMachine(CarBase):
    """Класс для работы со спецмашинами"""

    def __init__(self, brand, photo_file_name, carrying, extra=""):
        super().__init__(brand, photo_file_name, carrying)
        if extra != "":
            self.extra = extra
        else:
            print("error")
        self.car_type = "spec_machine"





def get_car_list(csv_filename):
    """
    Функция для работы с csv таблицами.
    Импортирует информацию из таблицы и создаёт соответствующие классы.
    Пример:
    cars = get_car_list("cars.csv")
    print(car.brand)
    for car in cars:
        print(car.brand)

    результат:
    Nissan xTtrail
    Honda
    """

    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row == []:
                    return car_list
                if len(row) == 7:
                    if row[0] == "car":
                        obj = Car(row[1], row[3], row[5], row[2])
                        car_list.append(obj)

                    elif row[0] == "truck":
                        obj = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(obj)

                    elif row[0] == "spec_machine":
                        obj = SpecMachine(row[1], row[3], row[5], row[6])
                        car_list.append(obj)
            except:
                print("invalid_input")
        return car_list

if __name__ == "__main__":
    cars = get_car_list("cars.csv")
    for car in cars:
        print(car.brand)


