from device import Device
from typing import List


class Smart(Device):
    def __init__(self, is_enabled: bool, volume: int, app_list: List):
        self.__is_enabled: bool = False
        self.__volume: int = 100
        self.__app_list: List[str] = []

    def set_volume(self, volume: int):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_channel(self, index: int):
        return self.__chanel_list[index]
