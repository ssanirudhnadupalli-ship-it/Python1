from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")

v1 = Car()
v2 = Bike()
v3 = Bus()

v1.start()
v2.start()
v3.start()