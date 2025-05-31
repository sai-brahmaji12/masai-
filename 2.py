class Device:
    def _init_(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name

    def _str_(self):
        return f"Device: {self.device_name}, ID: {self.device_id}"


class Flyer:
    def fly(self):
        print("The drone is now flying!")


class Drone(Device, Flyer):
    def _init_(self, device_id, device_name, model):
        Device._init_(self, device_id, device_name)
        self.model = model

    def capture_image(self):
        print(f"The drone {self.device_name} (Model: {self.model}) has captured an image.")

    def _str_(self):
        return f"{super()._str_()}, Model: {self.model}"