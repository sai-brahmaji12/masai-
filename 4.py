class Appliance:
    def status(self):
        print("This is a generic appliance.")

class Fan(Appliance):
    def status(self):
        print("The fan is running at medium speed.")

class Light(Appliance):
    def status(self):
        print("The light is turned on.")

class AC(Appliance):
    def status(self):
        print("The AC is set to 22°C and cooling.")