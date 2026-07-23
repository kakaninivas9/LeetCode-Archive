class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        i = carType - 1
        if self.slots[i] == 0:
            return False
        self.slots[i] -= 1
        return True