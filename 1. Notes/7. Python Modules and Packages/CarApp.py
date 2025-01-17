from hector import Hector

if __name__ == '__main__':
    hector1 = Hector()
    hector2 = Hector()
    
    hector1.start()
    hector2.start()
    
    hector1.speed_up(30)
    hector1.show_state()
    hector2.show_state()