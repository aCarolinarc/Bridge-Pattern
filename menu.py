from device import Device
from typing import List
from remote import Remote
from radio import Radio
from tv import Tv
from smart import Smart


class Menu:
    def __init__(self):
        self.__device_list: List[Device] = []
        self.__remote_list: List[Remote] = []
        self.tv_chanels = {
            1: "Deporte",
            2: "La lucha",
            3: "CartoonNetwork",
            4: "Noticias7"
        }
        self.radio_chanels = {
            90.1: "Exa",
            90.2: "Stereo",
            90.3: "Rancheras",
            90.4: "Noticias7"
        }
        self.smart_apps = {
            1: "Netflix",
            2: "Youtube",
            3: "Vim",
            4: "Google Chrome"
        }

    def create_device(self):
        print('***********************************')
        print('1. crear una tv')
        print('2. crear una radio')
        optionmenu = int(input("Porfavor coloque el numero de las opciones"))
        if optionmenu == 1:
            self.create_device(1)
        if optionmenu == 2:
            self.create_device(2)

    def create_remote(self):
        print('***********************************')
        print('1. crear un control normal')
        print('2. crear un control avanzado')
        optionmenu = int(input("Porfavor coloque el numero de las opciones"))
        if optionmenu == 1:
            self.create_device(1)
        if optionmenu == 2:
            self.create_device(2)

    def show_devices(self):
        pass

    def show_remotes(self):
        pass

    def create_device(self, option: int):
        if option == 1:
            # is_enabled: bool, volume: int, chanel_list: Dict
            tv = Tv(False, 100, self.tv_chanels)
            self.__device_list.append(tv)
            print("tv creada de forma exitosa")
        if option == 2:
            radio = Radio(False, 100, self.radio_chanels)
            self.__device_list.append(radio)
            print("radio creada de forma exitosa")

    def assign_device_to_remote(self):
        pass

    def create_device_menu(self):
        print('***********************************')
        print('1. crear un control remoto')
        print('2. crear un dispositivo')
        optionmenu = int(input("Porfavor coloque el numero de las opciones"))
        if optionmenu == 1:
            self.create_remote()
        if optionmenu == 2:
            self.create_device()

    def main_menu(self):
        option = 0

        while option != 6:
            print("*************************************")
            print("1. crear un control remoto")
            print("2. crear un dispositivo")
            print("3. ver lista de dispositivos")
            print("4. ver lista de controles")
            print("5. Asignar un control remoto a  un dispositivo")
            print("6. Salir")
            option = int(input('eliga una opcion: '))
            if option == 1:
                self.create_remote()
            if option == 2:
                self.create_device()
            if option == 3:
                self.show_devices()
            if option == 4:
                self.show_remotes()
            if option == 5:
                self.assign_device_to_remote()

