import json


class Car:
    brand = "MG Hector"

    @classmethod
    def launch_year(cls):
        return 2020

    def __init__(self, current_state="Standing", current_speed=0):
        self.current_state = current_state
        self.current_speed = current_speed

    def start(self):
        self.current_state = "Running"
        self.current_speed = 10

    def stop(self):
        self.current_state = "Standing"
        self.current_speed = 0

    def speed_up(self, speed):
        if self.current_state == "Standing":
            self.start()
        self.current_speed += speed

    def speed_down(self, speed):
        if self.current_state == "Running":
            self.current_speed -= speed

    def show_state(self):
        print(f"{self.current_state} and current speed is {self.current_speed}")


if __name__ == "__main__":
    car1 = Car()
    car1.start()
    car1.show_state()
