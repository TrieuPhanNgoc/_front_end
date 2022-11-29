class Point():
    def __init__(self, inpt_x, input_y):
        self.x = inpt_x
        self.y = input_y


class Flight():
    # Constructor:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    # Method
    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False    
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
          
# p = Point(3,5)
# print(p.x)
# print(p.y)

flight = Flight(5)

people = ["Harry", "Ron", "Herminoe", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
