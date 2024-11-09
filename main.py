class Car:
    def __init__(self, make, model, speed=0):
        self.make = make
        self.model = model
        self.speed = speed

    def drive(self, person):
        return f"{person.name} is driving a {self.make} {self.model} at {self.speed} km/h."

    def stop(self):
        self.speed = 0
        return f"The car has stopped."


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


    def drive_car(self, car):
        return car.drive(self)

    def stop_car(self, car):
        return car.stop()



alice = Person("Alice", 25)
honda = Car("Honda", "Civic", 90)


print(alice.drive_car(honda))
print(alice.stop_car(honda))
