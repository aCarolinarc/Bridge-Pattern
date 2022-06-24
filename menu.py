from device import Device
from typing import List
from remote import Remote
from radio import Radio
from tv import Tv
from smart import Smart
from advanceremote import Advacedremote


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

    def create_remote(self):
        print('***********************************')
        print('1. crear un control normal')
        print('2. crear un control avanzado')
        optionmenu = int(input("Porfavor coloque el numero de las opciones"))
        if optionmenu == 1:
            #  device: Device
            print("1. ANTES DE CREAR UN CONTROL, TENEMOS QUE ASIGNARLE UN DISPOSITIVO")
            self.show_devices()
            devices_pos = input("por favor coloque el numero del dipositivo que quiera asignar")
            remote = Remote(self.__device_list[devices_pos])
            self.__remote_list.append(remote)
            print("control remoto creado")
        if optionmenu == 2:
            print("1. ANTES DE CREAR UN CONTROL, TENEMOS QUE ASIGNARLE UN DISPOSITIVO")
            self.show_devices()
            devices_pos = input("por favor coloque el numero del dipositivo que quiera asignar")
            a_remote = Advacedremote(self.__device_list[devices_pos])
            self.__remote_list.append(a_remote)
            print("control avanzado creado")

    def show_devices(self):
        x = 0
        for i in self.__device_list:
            print(str(x) + " -> " + str(i.get_type()))
            x = x + 1

    def show_remotes(self):
        x = 0
        for i in self.__remote_list:
            print(str(x) + " -> " + i.device.get_type())
            x = x + 1

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
        if option == 3:
            tv_smart = Smart(False, 100, self.smart_apps)
            print("smart creada de forma exitosa")

    def create_device_menu(self):
        print('***********************************')
        print('1. crear una tv')
        print('2. crear una radio')
        print('3. crear tv smart')
        optionmenu = int(input("Porfavor coloque el numero de las opciones"))
        if optionmenu == 1:
            self.create_device(1)
        if optionmenu == 2:
            self.create_device(2)
        if optionmenu == 3:
            self.create_device(3)

    def real_control_device(self, option: int, remote: Remote):
        if option == 1:
            remote.enable()
        if option == 2:
            remote.disable()
        if option == 3:
            remote.channel_up()
        if option == 4:
            remote.channel_down()
        if option == 5:
            remote.volumen_up()
        if option == 6:
            remote.volumen_down()

    def control_device(self):
        print("--------------------------")
        self.show_remotes()
        option_control = int(input("por favor coloque el numero del control que desea usar"))
        control_using = self.__remote_list[option_control]
        print("1. prender el dispositivo")
        print("2. apagar dispositivo")
        print("3. subir de canal")
        print("4. bajar de canal")
        print("5. subir volumen")
        print("6. bajar volumen")
        do: int = int(input("porfavor elgia una opcion"))
        self.real_control_device(do, control_using)

    def main_menu(self):
        option = 0

        while option != 6:
            print("*************************************")
            print("1. crear un control remoto")
            print("2. crear un dispositivo")
            print("3. ver lista de dispositivos")
            print("4. ver lista de controles")
            print("5. Controlar un dispositivo")
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
                self.control_device()
