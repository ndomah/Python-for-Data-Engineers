from car import Car

class Hector(Car):
    
    def show_state(self):
        print(f"Hector is {self.current_state} and current speed is {self.current_speed}")
        
    def park(self):
        self.current_state = "Parked"
        self.current_speed = 0
        
if __name__ == '__main__':
    h1 = Hector()
    h1.start()
    h1.show_state()