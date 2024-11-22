# Parent class representing a general electronic device
class Device:
    def __init__(self, brand, model):
        self.brand = brand  # Brand of the device
        self.model = model  # Model of the device
        self.__is_on = False  # Private attribute to track if the device is on
    
    def turn_on(self):
        self.__is_on = True
        print(f"{self.model} is now turned on.")
    
    def turn_off(self):
        self.__is_on = False
        print(f"{self.model} is now turned off.")
    
    def is_on(self):
        return self.__is_on


# Child class representing a smartphone, inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, battery_percentage):
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.battery_percentage = battery_percentage  # Battery percentage specific to smartphones
    
    def make_call(self, number):
        if self.is_on():
            print(f"Calling {number} from {self.model}...")
        else:
            print("Turn the phone on first.")
    
    def send_message(self, number, message):
        if self.is_on():
            print(f"Sending message to {number}: {message}")
        else:
            print("Turn the phone on first.")
    
    def charge_battery(self, amount):
        if self.is_on():
            self.battery_percentage += amount
            if self.battery_percentage > 100:
                self.battery_percentage = 100  # Battery can't exceed 100%
            print(f"Charging... Battery at {self.battery_percentage}%")
        else:
            print("Turn the phone on first to charge.")
    
    def display_battery(self):
        print(f"Battery percentage: {self.battery_percentage}%")
    
    # Polymorphism: Overriding the turn_on method for Smartphone-specific behavior
    def turn_on(self):
        super().turn_on()  # Call the parent class's turn_on method
        print(f"{self.model} is ready for use, welcome!")

# Create a Smartphone object
my_phone = Smartphone("Apple", "iPhone 14", 50)

# Interact with the Smartphone object
my_phone.turn_on()  # Turn on the phone
my_phone.make_call("123-456-7890")  # Make a call
my_phone.send_message("123-456-7890", "Hello!")  # Send a message
my_phone.charge_battery(20)  # Charge the battery
my_phone.display_battery()  # Display battery status
my_phone.turn_off()  # Turn off the phone
