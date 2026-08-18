class Vehicle():

    def __init__(self):
        self.vehicle_name = 'tatta'
        print('Car name defined')

    def can_ride(self):
        print('i can ride')

class Car(Vehicle):

    # def __init__(self, vehicle_name):
    #     super().__init__(vehicle_name)
    def __init__(self, gps,vehicle_name):
        if gps:
            super().__init__()
        else:
            print("Child vehicle name")

    def get_car(self):
        print("GET car name")