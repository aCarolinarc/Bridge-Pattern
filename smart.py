from device import Device
from typing import List


class Smart(Device):
    def __init__(self, is_enabled: bool, volume: int, app_list: List):
        self.__is_enabled: bool = False
        self.__volume: int = 100
        self.__app_list: List[str] = []
        self.__type: str = "Radio"
        self.__chanel: int = 0

    def get_type(self):
        return self.__type

    def is_enabled(self):
        return self.__is_enabled

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = True

    def get_channel(self):
        return self.__chanel

    def set_channel(self, index: int):
        self.__chanel = index
        return self.__app_list[index]

    def set_volume(self, volume: int):
        self.__volume = volume

    def get_volume(self):
        return self.__volume
