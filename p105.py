from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Email Notification:", message)

class SMS(Notification):
    def send(self, message):
        print("SMS Notification:", message)

class Push(Notification):
    def send(self, message):
        print("Push Notification:", message)

n1 = Email()
n2 = SMS()
n3 = Push()

n1.send("Welcome!")
n2.send("Your OTP is 1234")
n3.send("New update available")