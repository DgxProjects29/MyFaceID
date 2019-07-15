import os
import pickle
import serial
import time


class BluePy:

    def __init__(self):
        self.port = None

    def start(self):
        parent = os.path.abspath(os.path.join('classes', os.pardir))
        data_settings = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        print(data_settings['blue_com'], data_settings['blue_bauds'])
        self.port = serial.Serial(data_settings['blue_com'], data_settings['blue_bauds'])

        time.sleep(2)

    def is_connected(self):
        return self.port.isOpen()

    def send_open_message(self):
        self.port.write(b'1')

    def send_change_message(self):
        self.port.write(b'2')

    def close(self):
        self.port.close()

    def reset_buffer(self):
        self.port.flushInput()

    def read_bytes(self):
        data_int = 2
        try:
            data = (self.port.readline())
            data_dec = data.decode('utf-8')
            if len(data_dec) != 0:
                data_int = int(data_dec)

        except:
            print("ERROR-READING")

        return data_int
