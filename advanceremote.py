from remote import Remote


class Advacedremote(Remote):

    def __init__(self, device: Remote):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volumen_down(self):
        vol: int = self.device.get_volume()
        vol = vol - 1
        self.device.set_volume(vol)

    def volumen_up(self):
        vol: int = self.device.get_volume()
        vol = vol + 1
        self.device.set_volume(vol)

    def channel_down(self):
        position: int = self.device.get_channel()
        position = position - 1
        self.device.set_channel(position)

    def channel_up(self):
        position: int = self.device.get_channel()
        position = position + 1
        self.device.set_channel(position)
