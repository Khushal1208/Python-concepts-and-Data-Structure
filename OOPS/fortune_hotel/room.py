# Abstract Room Class
class Room(ABC):
    counter = 1

    def __init__(self, price):
        self.room_id = Room.counter
        Room.counter += 1
        self.price = price
        self.customer = None

    def get_room_id(self):
        return self.room_id

    def get_price(self):
        return self.price

    def get_customer(self):
        return self.customer

    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_price(self, price):
        self.price = price

    def set_customer(self, customer):
        self.customer = customer

    @abstractmethod
    def calculate_room_rent(self, no_of_days):
        pass

# LuxuryRoom Class
class LuxuryRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.free_wifi = True

    def get_free_wifi(self):
        return self.free_wifi

    def set_free_wifi(self, free_wifi):
        self.free_wifi = free_wifi

    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days

# StandardRoom Class
class StandardRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.comfortable_desk = True

    def get_comfortable_desk(self):
        return self.comfortable_desk

    def set_comfortable_desk(self, comfortable_desk):
        self.comfortable_desk = comfortable_desk

    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days
