from device import Device
from typing import Dict


class Radio(Device):
    def __init__(self, is_enabled: bool, volume: int, chanel_list: Dict):
        self.__is_enabled: bool = False
        self.__volume: int = 100
        self.__chanel_list: Dict[int: str] = {}
        self.__type: str = "Radio"
        self.__chanel: int = 0

    def get_type(self):
        return self.__type

    def is_enabled(self):
        return self.__is_enabled

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = False

    def get_channel(self, chanels):
        return self.__chanel

    def set_volume(self, volume: int):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_channel(self, chanel: int):
        self.__chanel = chanel
        return self.__chanel_list[chanel]
