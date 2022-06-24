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

    def create_device_menu(self):
        print('***********************************')
        print('1. crear tv')
        print('2. crear smart')
        print('3. crear radio')
        
    def create_device(self):
        pass

    def create_remote(self):
        pass

    def show_devices(self):
        pass

    def show_remotes(self):
        pass

    def create_device(self):
        pass

    def assign_device_to_remote(self):
        pass

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

