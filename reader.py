import threading

import main
from database import Database
from vessel_data import VesselValues

database = Database()
vesselValues = VesselValues()

class SingletonClass:
    _instance = None
    number: int

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(SingletonClass, cls).__new__(cls)
            cls.__int__(cls._instance, 10)
        return cls._instance

    def __int__(self, numner: int):
        print("constructor executed:", numner)


if __name__ == '__main__':
    print(database.latest_value())
    print(main.Vincent.number)
    obj1 = SingletonClass()
    obj1.number = 10
    print(obj1)
    obj1.number = 50
    obj2 = SingletonClass()
    print(obj2.number)
